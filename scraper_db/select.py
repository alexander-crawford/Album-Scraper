if __name__ == '__main__':
    getNoYear()
    getNoImage()

def getNoYear(cnx):
    # create cursor
    cursor = cnx.cursor()

    # create select statement
    get_no_year = (
        "SELECT artist.name AS Aritst, "
        "album.title AS Album "
        "FROM album "
        "INNER JOIN artist_album ON album.id = artist_album.album_id "
        "INNER JOIN artist ON artist_album.artist_id = artist.id "
        "WHERE album.year IS NULL"
    )

    # run statement
    cursor.execute(get_no_year)

    # return result
    return cursor.fetchall()

def getNoImage(cnx):
    # create cursor
    cursor = cnx.cursor()

    # create select statement
    get_no_image = (
        "SELECT artist.name AS Aritst, "
        "album.title AS Album "
        "FROM album "
        "INNER JOIN artist_album ON album.id = artist_album.album_id "
        "INNER JOIN artist ON artist_album.artist_id = artist.id "
        "WHERE album.image_lrg IS NULL OR "
        "album.image_sml IS NULL"
    )

    # run statement
    cursor.execute(get_no_image)

    # return result
    return cursor.fetchall()

def getNoYearAndImage(cnx):
    # create cursor
    cursor = cnx.cursor()

    # create select statement
    get_no_image = (
        "SELECT artist.name AS Aritst, "
        "album.title AS Album "
        "FROM album "
        "INNER JOIN artist_album ON album.id = artist_album.album_id "
        "INNER JOIN artist ON artist_album.artist_id = artist.id "
        "WHERE album.image_lrg IS NULL AND "
        "album.image_sml IS NULL"
    )

    # run statement
    cursor.execute(get_no_image)

    # return result
    return cursor.fetchall()
