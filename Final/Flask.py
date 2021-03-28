from typing import Text
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    return render_template("index.html")

@app.route("/topic", methods=["POST","GET"])
def topic():
    if request.method=="POST":
        topic = request.form["topic"]
        listings = []
        DATA = requests.get("https://www.yellowpages.ca/search/si/1/"+topic+"/Windsor+ON").text
        SOUP = BeautifulSoup(DATA, "html.parser")
        for listing in SOUP.find_all("div", class_="listing__right hasIcon"):
            NAME = listing.find("a", class_="listing__name--link listing__link jsListingName")
            ADDRESS = listing.find("span", class_="listing__address--full")
            if NAME is not None and ADDRESS is not None:
                listings.append("\n"+NAME.text+"\n"+ADDRESS.text+"\n")
        return render_template("index.html", listings=listings)

if __name__ == "__main__":
    app.run(debug=True)
