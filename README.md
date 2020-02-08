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

## Templates

Imagine having to build the HTML code for a large table by concatenating
data obtained from the database with the necessary HTML string literals. Moving the
presentation logic into templates helps improve the maintainability of the application.
A template is a file that contains the text of a response, with placeholder variables for
the dynamic parts that will be known only in the context of a request. The process that
replaces the variables with actual values and returns a final response string is called
rendering. For the task of rendering templates, Flask uses a powerful template engine
called Jinja2.

## Variables
The {{ name }} construct used in the template shown in Example 3-2 references a
variable, a special placeholder that tells the template engine that the value that goes in
that place should be obtained from data provided at the time the template is rendered.
Jinja2 recognizes variables of any type, even complex types such as lists, dictionaries
and objects. The following are some more examples of variables used in templates:
<p>A
<p>A
<p>A
<p>A
value
value
value
value
from
from
from
from
a dictionary: {{ mydict['key'] }}.</p>
a list: {{ mylist[3] }}.</p>
a list, with a variable index: {{ mylist[myintvar] }}.</p>
an object's method: {{ myobj.somemethod() }}.</p>
Variables can be modified with filters, which are added after the variable name with a
pipe character as separator. For example, the following template shows the name variable
capitalized:
Hello, {{ name|capitalize }}
Table 3-1 lists some of the commonly used filters that come with Jinja2.
Table 3-1. Jinja2 variable filters
Filter name Description
safe Renders the value without applying escaping
capitalize Converts the first character of the value to uppercase and the rest to lowercase
lower Converts the value to lowercase characters
upper Converts the value to uppercase characters
title Capitalizes each word in the value
trim Removes leading and trailing whitespace from the value
striptags Removes any HTML tags from the value before rendering

## Twitter Bootstrap Integration with Flask-Bootstrap

Bootstrap is an open source framework from Twitter that provides user interface com‐
ponents to create clean and attractive web pages that are compatible with all modern
web browsers.
Bootstrap is a client-side framework, so the server is not directly involved with it. All
the server needs to do is provide HTML responses that reference Bootstrap’s cascading
style sheets (CSS) and JavaScript files and instantiate the desired components through
HTML, CSS, and JavaScript code. The ideal place to do all this is in templates.
The obvious way to integrate Bootstrap with the application is to make all the necessary
changes to the templates. A simpler approach is to use a Flask extension called Flask-
Bootstrap to simplify the integration effort. Flask-Bootstrap can be installed with pip:
(venv) $ pip install flask-bootstrap
