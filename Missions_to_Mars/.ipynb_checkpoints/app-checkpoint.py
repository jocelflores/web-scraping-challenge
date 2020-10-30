from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

# create flask and establish Mongo Connection
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# create route to render index.html

@app.route("/")

def home():
    
    # find dictionary and return
    
    html_table = mongo.db.collection.find_one()
    
    return render template('index.html', mars = html_facts)

@app.route("/scrape")
def scrape():
    
    #run scrape function
    mars_info = mars_scrape.scrape()
    
    # update db
    mongo.db.collection.update({}, mars_info, upsert=True)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)