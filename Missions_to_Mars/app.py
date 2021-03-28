from flask import Flask, render_template
import scrape_mars
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_db
mars = db.mars


@app.route("/")
def index():
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars()
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
