# Step 2: Climate App

# import all the dependencies
import datetime as datetime
import numpy as np 
import pandas as pd 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, json, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread':False})
# reflect database into new model
Base = automap_base
# reflect tables
Base.prepare(enginge, reflect=True)

# Save references of each table
mesurement = Base.classes.measurement
station = Base.classes.station
# create session link from Python to the Database
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# define routes
@app.route("/")
def home():
    print("In & Out of Home section.")
    return (
        f"Welcome to the Hawaii Climate API!<br/>"
        f"Please select one of the available routes:<br/>""
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/
        f"/api/v1.0/
        f"/api/v1.0/
    )