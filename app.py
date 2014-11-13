# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask

#create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!?!?"

# dynamic route
@app.route("/test/<value>")
def search(value):
    return value

# dynamic rout with explicit status codes
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404

# start the development server using the run() method
if __name__ == "__main__":
    app.run()