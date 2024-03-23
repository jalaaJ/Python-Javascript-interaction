from flask import Flask
from flask_sqlalchemy import SQLAchemy
from flask_cors import CORS

# Initiate the Flask app
app = Flask(__name__)

# To enable sending cross-origin requests to our server
CORS(app)

# Initialize the sqlite database, and provide the location of the local database on our machine
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create an instance of the database
db = SQLAchemy(app)
