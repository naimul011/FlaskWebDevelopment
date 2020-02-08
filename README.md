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
