from scraper_db import connect
from scrapers import billboard

# create connection to scraper_db
cnx = connect.connect()

# get resuts from scraper
result = billboard.get()
