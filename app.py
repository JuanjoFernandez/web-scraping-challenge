# Dependencies and libraries
import pymongo
from flask import Flask

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.planets

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    
    return "blah"

# Scrape route
@app.route("/scrape")
def scrape():
    from scrape_mars import scrape
    drop_collection = "mars" in db.list_collection_names()
    if drop_collection == True:
        db.mars.drop()
    data = scrape()
    db.mars.insert_one(data)
    return "done"

if __name__ == "__main__":
    app.run(debug=True)

