import scraper_db
import api
import scraper as s
import json

# create connection to scraper_db
cnx = scraper_db.connect()

# pull scraper from external json file
scrapers = json.load(open('scraper.json','r'))

for scraper in scrapers:
    # for each scraper found in json get album info
    result = s.scrape(scraper['source_name'],scraper['source_url'], \
    scraper['container_tag'],scraper['container_class'], \
    scraper['position_tag'],scraper['position_class'], \
    scraper['artist_tag'],scraper['artist_class'], \
    scraper['album_tag'],scraper['album_class'],)

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
