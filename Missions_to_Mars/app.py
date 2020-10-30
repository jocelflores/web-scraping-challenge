from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import mars_scrape

# create flask and establish Mongo Connection
app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_app
collection = db.mars_app
mars_app = db.mars_app

# create route to render index.html

@app.route("/")

def home():

    # find dictionary and return

    mars_info = collection.find_one()

    return render_template('index.html', mars_app = mars_info)

@app.route("/scrape")
def scrape():



    #run scrape function
    mars_info = mars_scrape.scrape()

    # update db
    # Drops collection if available to remove duplicates
    mars_app.drop()
    mars_app.insert_many(mars_info)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)