Clime Analysis using SQLAlchemy

This analysis requred two Parts
    Part 1: Climate Analysis and Exploration
    Part 2: CLimate App

Part 1: Climate Analysis and Exploration
Use Python and SQLAlchemy to do basic analysis and data exploration of the database provided.

* Used [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.
* Used SQLAlchemy `create_engine` to connect to your sqlite database.
* Used SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.
* Link Python to the database by creating an SQLAlchemy session.

### Precipitation Analysis

* Start by finding the most recent date in the data set.
* Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 
* Selected only the `date` and `prcp` values.
* Loaded the query results into a Pandas DataFrame and set the index to the date column.
* Sorted the DataFrame values by `date`.
* Plotted the results using the DataFrame `plot` method.
* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis


* Designed a query to calculate the total number of stations in the dataset.
* Designed a query to find the most active stations 
* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

Part 2: Climate App

### Routes
* Use Flask to create your routes.
    * `/home`
    * `/api/v1.0/precipitation`
    * `/api/v1.0/stations`
    * `/api/v1.0/tobs`
    * `/api/v1.0/<start>`
    * `/api/v1.0/<start>/<end>`
* Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.