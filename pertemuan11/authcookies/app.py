#!/Users/mymac/miniconda3/bin/python
import flask
from flask import request, render_template


app = flask.Flask(__name__)

token = "WVsk7KKj93mcQCbVJC0cdu0z79DEtE1BdRLaPcgA5"


@app.before_request
def is_logged():
    if request.path == "/":
        sgitstore_token = request.cookies.get("auth_sgitstore")
        if token != sgitstore_token:
            return flask.redirect("/login")


@app.route("/")
def index():
    return "login SUCCESS"


@app.get("/login")
def login():
    return render_template("login.html")


@app.post("/login")
def do_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == "admin":
        # Create cookie with flask
        response = flask.make_response(flask.redirect("/"))

        response.set_cookie("auth_sgitstore", token, max_age=60 * 60 * 24 * 7)

        # Do redirect to '/'
        return response

    return "FAILED"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001, use_reloader=True)
