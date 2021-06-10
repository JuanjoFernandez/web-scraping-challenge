# Dependencies and libraries
from flask import Flask

app = Flask(__name__)

# Home route
@app.route("/")
def home():

# Scrape route
@app.route("/scrape")
def scrape():
    from scrape_mars import scrape
    data = scrape()

