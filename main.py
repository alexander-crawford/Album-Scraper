import scraper_db
from scrapers import billboard
import api

# create connection to scraper_db
cnx = scraper_db.connect()

# get results from scraper
# result = billboard.get()

# insert into db providing connection and results
# scraper_db.insert(cnx,result)

# get albums with no year and image
print('no year and image')
for item in scraper_db.getNoYearAndImage(cnx):
    print(api.getAlbumInfo(item[0] + " " + item[1]))

# disconnect from scraper_db
cnx.close()
