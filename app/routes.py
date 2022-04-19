from flask import Flask         # From the flask module import the Flask class


app = Flask(__name__)           # Create an instance on "Flask" into app


@app.get("/")
def index():
    me = {
        "first_name": "Sebastian",
        "last_name": "Ruiz",
        "hobbies": "Guitar/Soccer",
        "activate": True
    }
    return me