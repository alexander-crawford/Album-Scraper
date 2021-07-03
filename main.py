import scraper_db
from scrapers import billboard
import api

# create connection to scraper_db
cnx = scraper_db.connect()

# get results from scraper
result = billboard.get()

# insert into db providing connection and results
scraper_db.insert(cnx,result)

# disconnect from scraper_db
cnx.close()
