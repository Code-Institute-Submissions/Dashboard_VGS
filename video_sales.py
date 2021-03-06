from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
import os
 
app = Flask(__name__)
 
# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017
# DBS_NAME = 'videogamessales'
# COLLECTION_NAME = 'sales'

MONGODB_URI = os.environ.get('MONGODB_URI')
DBS_NAME = os.environ.get('MONGO_DB_NAME' , 'videogamesales')
COLLECTION_NAME = os.environ.get('MONGO_COLLECTION_NAME', 'vgsales')

 
 
@app.route("/")
def index():
    """
    A Flask view to serve the main dashboard page.
    """
    return render_template("index.html")
 
 
@app.route("/videogamessales/sales")
def videogamessales_sales():
    """
    A Flask view to serve the project data from
    MongoDB in JSON format.
    """
 
    # A constant that defines the record fields that we wish to retrieve.
    FIELDS = {
        '_id': False, 'Name': True, 'Year': True, 'Platform': True, 'Rank': True, 'Genre': True, 
        'Global_Sales': True, 'Publisher': True, 'NA_Sales': True, 'EU_Sales': True, 'JP_Sales': True, 'Other_Sales': True, 'Global_Sales': True
    }
 
    # Open a connection to MongoDB using a with statement such that the
    # connection will be closed as soon as we exit the with statement
    with MongoClient(MONGODB_URI) as conn:
        # Define which collection we wish to access
        collection = conn[DBS_NAME][COLLECTION_NAME]
        # Retrieve a result set only with the fields defined in FIELDS
        # and limit the the results to 55000
        projects = collection.find(projection=FIELDS, limit=1000)
        # Convert projects to a list in a JSON object and return the JSON data
        return json.dumps(list(projects))
 
 
if __name__ == "__main__":
    app.run(debug=True)