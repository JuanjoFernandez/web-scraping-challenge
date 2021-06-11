# Dependencies and libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/planets"
mongo = PyMongo(app)

# Home route
@app.route("/")
def home():
    query_mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=query_mars)

# Scrape route
@app.route("/scrape")
def scraper():
    from scrape_mars import scrape
    drop_collection = "mars" in db.list_collection_names()
    if drop_collection == True:
        db.mars.drop()
    data = scrape()
    db.mars.insert_one(data)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
