from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

# Convert this file into application instance
app = Flask(__name__) 

# Connect to the MongoDB server (in our container 'mongo_db')
client = MongoClient('mongodb://mongo_db:27017/')

# Specify DB to connect to
db = client.user_profiles

# Specify which collection to interact with
collection = db.profiles

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/thank_you')
def thank_you():
    return "<h1> Thank you! Your profile has been created successfully!</h1>"

# GET the data from the index.html <form>
@app.route('/submit', methods = ["POST"])
def submit():
    user_name = request.form.get("name")
    user_email = request.form.get("email")
    user_age = request.form.get("age")

# This will be stored in the DB in JSON format
    user_data = {
        'name': user_name,
        'email': user_email,
        'age': user_age
    }

    # Insert our data into our collection (db.profiles)
    collection.insert_one(user_data)
    return redirect(url_for("thank_you"))


if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5000)