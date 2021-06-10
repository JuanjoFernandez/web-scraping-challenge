# Dependencies and libraries
import pymongo
from flask import Flask

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.planets

from scrape_mars import scrape
data = scrape()
db.mars.insert_one(data)


