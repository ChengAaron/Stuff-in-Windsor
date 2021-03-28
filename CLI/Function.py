from bs4 import BeautifulSoup
import requests

def displayResults(topic):
    DATA = requests.get("https://www.yellowpages.ca/search/si/1/"+topic+"/Windsor+ON").text
    SOUP = BeautifulSoup(DATA, "html.parser")
    for listing in SOUP.find_all("div", class_="listing__right hasIcon"):
        NAME = listing.find("a", class_="listing__name--link listing__link jsListingName")
        ADDRESS = listing.find("span", class_="listing__address--full")
        if NAME is not None and ADDRESS is not None:
            print("\n"+NAME.text+ADDRESS.text)
