# import flask module from Flask package
from flask import Flask

# create a function that creates a web application
# a web server will run this web application


def create_app():
    print(__name__)  # let us be curious - what is this __name__
    # this is the name of the module/package that is calling this app
    app = Flask(__name__)
    return app
