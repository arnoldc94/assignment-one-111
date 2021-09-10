



from flask import Flask    # From the flask package import the Flask class.

app = Flask(__name__)      # instantiate the Flask class with a paramater __name__ into "app".

@app.route("/")            # @app.route is a decorator that wraps the function underneath it.
def index():               # view function that is being wrapped.
    return "<h1>Hello, World!</h1>"

@app.route("/about")
def about_me():
    me ={
        "first_name": "Corey",
        "last_Name": "Arnold",
        "hobbies": "Jiu-Jitsu",
        "active": True,
    }
    return me
