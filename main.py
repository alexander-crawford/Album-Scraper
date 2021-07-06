import scraper_db
from scrapers import billboard
import api

# create connection to scraper_db
cnx = scraper_db.connect()

# get results from scraper
result = billboard.get()

# insert into db providing connection and results
scraper_db.insert(cnx,result)

# get albums where year is null
print('no year')
for item in scraper_db.getNoYear(cnx):
    print(item[0],item[1])

# get albums with no image
print('no image')
for item in scraper_db.getNoImage(cnx):
    print(item[0],item[1])

# disconnect from scraper_db
cnx.close()
