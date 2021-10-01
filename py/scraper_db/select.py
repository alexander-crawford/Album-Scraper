def getDiscogsAlbums(cnx):
    # create cursor
    cursor = cnx.cursor()

    # create select statement
    get_no_image = (
        "SELECT album.id, "
        "album.title, "
        "artist.name, "
        "album.year, "
        "album.image_lrg "
        "FROM album "
        "INNER JOIN artist_album ON album.id = artist_album.album_id "
        "INNER JOIN artist ON artist_album.artist_id = artist.id "
        "WHERE (album.image_lrg IS NULL OR "
        "album.year IS NULL) "
        "AND album.discogs_api = 0"
    )

    # run statement
    cursor.execute(get_no_image)
    result = cursor.fetchall()

    # print statements for log
    print("\n DISCOGS")
    print(cursor.rowcount,"covers or years required")

    # return result
    return result

def getSources(cnx):
    # create cursor
    cursor = cnx.cursor(dictionary=True)

    # create select statement
    get_sources = (
        "SELECT title as source,"
        "url,"
        "container_tag,"
        "container_class,"
        "artist_tag,"
        "artist_class,"
        "album_tag,"
        "album_class "
        "FROM source"
    )

    # run statement
    cursor.execute(get_sources)
    result = cursor.fetchall()

    # return result
    return result
