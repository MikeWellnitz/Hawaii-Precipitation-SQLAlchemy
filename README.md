# Analyzing Precipitation in Hawaii

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Data Analysis](#data-analysis)
- [Software and Languages](#software-and-languages)
- [Acknowledgements](#acknowledgements)

## About

Leaning into SQLAlchemy, this project takes a look at how much precipitation was recorded in Hawaii. Includes some data manipulation and visualizations, and a very modest and basic Flask application.


## Getting Started

I used Jupyter Notebook/Python 3.10 and coded my analysis in "climate_starter.ipynb". This pulls in the data from "hawaii.sqlite", which is a database containing data from the two CSV files (all of which are located in the "Resources" folder). 
For the Flask application, I used Visual Studio Code for coding "app.py". To run this application in Visual Studio Code, I opened a Terminal and ran "$ python app.py" which resulted in a browser window opening with the routes being listed to show data gathered. 

## Data Analysis

Most of this project was to test out knowledge of data manipulation using SQLAlchemy in addition to practice using Matplotlib. Data that had been gathered only went until August 2017, so much of the analysis went up until that date as "most recent". It was also intended to check out my beginning skills with creating a Flask application.

This is the information I retrieved: 
* Find the most recent date in the dataset
* Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data
* Load the query results into a Pandas DataFrame. Explicitly set the column names
* Sort the DataFrame values by "date"
* Plot the results by using the DataFrame plot method
* Use Pandas to print the summary statistics for the precipitation data
* Design a query to calculate the total number of stations in the dataset.
* Design a query to find the most-active stations
* Which station id has the greatest number of observations?
* Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
* Design a query to get the previous 12 months of temperature observation (TOBS) data.
* Query the previous 12 months of TOBS data for that station.
* Plot the results as a histogram with bins=12, 


## Software and Languages

Full Listing:
* Jupyter Notebook/Python
* SQLAlchemy
* Pandas
* Numpu
* Datetime
* Matplotlib
* SQLite
* Excel
* Visual Studio Code
* GitHub


## Acknowledgements

This project was derived from my Data Analytics and Visualization Bootcamp from the University of Minnesota, Module 10, March 2023 cohort.