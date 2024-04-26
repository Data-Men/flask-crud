from app import app, db
# from flask import render_template, url_for, request, redirect, session
from app.models.user import User

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Define route
@app.route("/db")

def hello_db():
    print(db.session.query(User).all())
    return "<p>Hello, World!</p>"