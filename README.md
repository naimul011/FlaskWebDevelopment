# FlaskWebDevelopment
## Initialization

The name argument that is passed to the Flask application construc‐
tor is a source of confusion among new Flask developers. Flask uses
this argument to determine the root path of the application so that it
later can find resource files relative to the location of the application.

## Routes and View Functions
Clients such as web browsers send requests to the web server, which in turn sends them
to the Flask application instance. The application instance needs to know what code
needs to run for each URL requested, so it keeps a mapping of URLs to Python funct

## Server Startup
The application instance has a run method that launches Flask’s integrated development
web server:

if __name__ == '__main__':
	app.run(debug=True)

The __name__ == '__main__' Python idiom is used here to ensure that the develop‐
ment web server is started only when the script is executed directly. When the script is
imported by another script, it is assumed that the parent script will launch a different
server, so the app.run() call is skipped.

## Responses
When Flask invokes a view function, it expects its return value to be the response to the
request. In most cases the response is a simple string that is sent back to the client as an
HTML page.

But the HTTP protocol requires more than a string as a response to a request. A very
important part of the HTTP response is the status code, which Flask by default sets to
200, the code that indicates that the request was carried out successfully.
When a view function needs to respond with a different status code, it can add the
numeric code as a second return value after the response text. For example, the following
view function returns a 400 status code, the code for a bad request error:

@app.route('/')
def index():
	return '<h1>Bad Request</h1>', 400

Responses returned by view functions can also take a third argument, a dictionary of
headers that are added to the HTTP response. This is rarely needed, but you will see an
example in Chapter 14.

Instead of returning one, two, or three values as a tuple, Flask view functions have the
option of returning a Response object. The make_response() function takes one, two,
or three arguments, the same values that can be returned from a view function, and
returns a Response object. Sometimes it is useful to perform this conversion inside the
The Request-Response Cycle 15view function and then use the methods of the response object to further configure the
response. The following example creates a response object and then sets a cookie in it:
from flask import make_response

@app.route('/')
def index():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response

There is a special type of response called a redirect. This response does not include a
page document; it just gives the browser a new URL from which to load a new page.
Redirects are commonly used with web forms, as you will learn in Chapter 4.
A redirect is typically indicated with a 302 response status code and the URL to redirect
to given in a Location header. A redirect response can be generated using a three-value
return, or also with a Response object, but given its frequent use, Flask provides a
redirect() helper function that creates this response:

from flask import redirect
@app.route('/')
def index():
	return redirect('http://www.example.com')

Another special response is issued with the abort function, which is used for error
handling. The following example returns status code 404 if the id dynamic argument
given in the URL does not represent a valid user:

from flask import abort
@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
		return '<h1>Hello, %s</h1>' % user.name

Note that abort does not return control back to the function that calls it but gives control
back to the web server by raising an exception.

