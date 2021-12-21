def getDiscogsAlbums(cnx):
    # create cursor
    cursor = cnx.cursor(dictionary=True)

    # create select statement
    get_no_image = (
        "SELECT album.id, "
        "album.title as album, "
        "artist.name as artist "
        "FROM album "
        "INNER JOIN artist ON album.artist_id = artist.id "
        "LEFT JOIN album_api ON album.id = album_api.album_id "
        "WHERE (album.year IS NULL OR album.image IS NULL) "
        "AND (album_api.api_id <> 1 or album_api.api_id IS NULL)"
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
        "SELECT * FROM source"
    )

    # run statement
    cursor.execute(get_sources)
    result = cursor.fetchall()

    # return result
    return result

def getLargeImages(cnx):
    # create cursor
    cursor = cnx.cursor(dictionary=True)

    # create select statement
    get_large_images = (
        "SELECT id,image FROM album WHERE resized IS FALSE"
    )

    # run statement
    cursor.execute(get_large_images)
    result = cursor.fetchall()

    # return result
    return result
