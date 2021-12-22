import scraper_db
import api
import scraper

# create connection to scraper_db
cnx = scraper_db.connect()

# get source information from database
sources = scraper_db.getSources(cnx)

for source in sources:
    # for each source scrape site
    result = scraper.scrape(source['title'],source['url'], \
    source['container_tag'],source['container_class'],source['artist_tag'], \
    source['artist_class'],source['album_tag'],source['album_class'])

    # insert into db providing connection and results
    scraper_db.insert(cnx,result,source['id'])

# get albums where image or year is missing
for item in scraper_db.getDiscogsAlbums(cnx):

    result = api.getAlbumInfo(item['artist'] + " " + item['album'])

    if result!=None:

        # addYear(cnx,year,album_id)
        scraper_db.addYear(cnx,result['album_year'],item['id'])
        # addImage(cnx,url,album_id)
        scraper_db.addImage(cnx,result['album_cover_url'],item['id'])

    # discogsApiCalled(cnx,album_id)
    scraper_db.discogsApiCalled(cnx,item['id'])

# get images that need to be resized
for item in scraper_db.getLargeImages(cnx):

    # resize each image
    scraper_db.resizeImage(cnx,item['id'],item['image'])

# disconnect from scraper_db
cnx.close()
