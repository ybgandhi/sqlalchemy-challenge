# Step 2: Climate App

# import all the dependencies
import datetime as dt
import numpy as np 
import pandas as pd 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, json, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread':False})
# reflect database into new model
Base = automap_base()
# reflect tables
Base.prepare(engine, reflect=True)

# Save references of each table
Measurement = Base.classes.measurement
Station = Base.classes.station
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
        f"Please select one of the available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2016-01-01/<br/>"
        f"/api/v1.0/2016-01-01/2016-12-31/"
    )

# return the JSON representation of the dictionary that was created
@app.route('/api/v1.0/precipitation/')
def precipitation():
    print("In Precipitation section.")

    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_year = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

    rain_results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= last_year). \
    order_by(Measurement.date).all()

    p_dict = dict(rain_results)
    print(f"Results for Precipitation - {p_dict}")
    print(f"Out of Precipitation section.")
    return jsonify(p_dict)

# return JSON list of stations from the dataset
@app.route('/api/v1.0/stations/')
def stations():
    print()

    station_list = session.query(Station.station)\
    .order_by(Station.station).all()
    print()
    print("Station List:")
    station_list = list(np.ravel(station_list))
    print(station_list)
    print("Out of Station section.")
    return jsonify(station_list)

# return JSON list of Temperature Observations from the dataset
@app.route('/api/v1.0/tobs/')
def tobs():
    print("In TOBS section")

    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_year = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

    temp_obs = session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.date >= last_year)\
        .order_by(Measurement.date).all()

    print()
    print("Temperature Results for All Stations")
    print(temp_obs)
    print("Out of TOBS section")
    return jsonify(temp_obs)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date    
@app.route('/api/v1.0/<start_date>/')
def calc_temps_start(start_date):
    print("In start date section.")
    print(start_date)

    select = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    result_temp = session.query(*select).\
        filter(Measurement.date >= start_date).all()
    print()
    print(f"Calculated temp for start date {start_date}")
    print(result_temp)
    print("Out of start date section")
    return jsonify(result_temp)

# Return a JSON list of the minimum temperature, the average temperature, and the max remperature for the end date
@app.route('/api/v1.0/<start_date>/<end_datet>')
def calc_temps_end(start_date, end_date):
    print("In start & end date section")

    select = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    result_temp = session.query(*select).\
        filter(Measurement.date >= start_date).filter(Measurement.tobs <= end_date).all()
    print()
    print(f"Calculated temp for start date {start_date} & end date {end_date}")
    print(result_temp)
    print("Out of start & end date section.")
    return jsonify(result_temp)

if __name__ == "__main__":
    app.run(debug=True)