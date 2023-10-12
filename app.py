# Import the dependencies.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
# Precipitation = Base.classes.prcp
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def route_welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/r>"
    )



@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    
    date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    
    
    precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > '2016-08-22').order_by(Measurement.date).all()
   

    results = []
    for date, prcp in precip:
        dateprecip = {}
        dateprecip["date"] = date
        dateprecip["prcp"] = prcp
        results.append(dateprecip)

    return jsonify(results)




@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine) 
    stations = session.query(Station.station).all()  

    results = []
    for place in stations:
        results.append(list(place)[0])

    return jsonify(results)




@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    active = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date > '2016-08-22').order_by(Measurement.station).all()

    results2 = []
    for temps in active:
        results2.append(list(temps)[0])

    return jsonify(results2)




@app.route("/api/v1.0/<start>")
def calc_temps_start(start):

    try:
        # Convert the 'start' parameter from the URL to a datetime object
        start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD format.'}), 400



    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    dict = {
        'TMIN': results[0][0],
        'TAVG': results[0][1],
        'TMAX': results[0][2]
    }

    session.close()
    
    return jsonify(dict)


@app.route("/api/v1.0/<start>/<end>")
def calc_temps_start_end(start, end):

    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    dict = {
        'TMIN': results[0][0],
        'TAVG': results[0][1],
        'TMAX': results[0][2]
    }

    session.close()
    
    return jsonify(dict)












if __name__ == "__main__":
    app.run(debug=True)