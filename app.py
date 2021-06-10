# Dependencies and libraries
import pymongo
from flask import Flask

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    
    return "blah"

# Scrape route
@app.route("/scrape")
def scrape():
    from scrape_mars import scrape
    data = scrape()
    db.insert_one(data)
    return

if __name__ == "__main__":
    app.run(debug=True)

