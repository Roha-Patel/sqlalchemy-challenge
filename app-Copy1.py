# Import the dependencies.
from flask import Flask, jesonify

# Create a Flask app
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# Import necessary dependencies for database setup
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create engine to connect to SQLite database
engine = create_engine("sqlite:///your_database_name_here.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################



#################################################
# Flask Routes
#################################################

@app.route('/')
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt/&lt;end&gt"
    )

if __name__ == '__main__':
    app.run(debug=True)
