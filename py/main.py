import scraper_db
from scrapers import billboard_top_album_sales as  b_top
from scrapers import billboard_top_rnb_hiphop_albums as  b_top_rnb_hiphop
import api

# create connection to scraper_db
cnx = scraper_db.connect()

# get results from scraper
result = b_top.get()

# insert into db providing connection and results
scraper_db.insert(cnx,result)

# get results from scraper
result = b_top_rnb_hiphop.get()

# insert into db providing connection and results
scraper_db.insert(cnx,result)

# get albums where image or year is missing
for item in scraper_db.getDiscogsAlbums(cnx):

    result = api.getAlbumInfo(item[1] + " " + item[2])

    if result!=None:

        # addYear(cnx,year,album_id)
        scraper_db.addYear(cnx,result['album_year'],item[0])
        # addImage(cnx,url,album_id)
        scraper_db.addImage(cnx,result['album_cover_url'],item[0])

    # discogsApiCalled(cnx,album_id)
    scraper_db.discogsApiCalled(cnx,item[0])

# disconnect from scraper_db
cnx.close()
