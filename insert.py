import mysql.connector
import billboardHot100 as billboard
import json


data =  json.loads(billboard.get())
if data['meta']['status']==200:

    # create connection to mysql database
    cnx = mysql.connector.connect(user='root',password='123456', database='album_scraper')

    # create cursor
    cursor = cnx.cursor()

    add_artist = (
        "INSERT INTO artist "
        "(name) "
        "VALUES (%s)"
    )
    get_artist = (
        "SELECT id FROM artist "
        "WHERE name = (%s)"
    )
    add_album = (
        "INSERT INTO album "
        "(title) "
        "VALUES (%s)"
    )
    get_album = (
        "SELECT album.id FROM album "
        "INNER JOIN artist_album ON album.id = artist_album.album_id "
        "INNER JOIN artist ON artist_album.artist_id = artist.id "
        "WHERE artist.id = %(artist)s AND album.title = %(album)s"
    )
    add_artist_album = (
        "INSERT INTO artist_album "
        "(artist_id,album_id) "
        "VALUES (%(artist)s,%(album)s)"
    )
    for data in data['data']:
        artist_id = ''
        album_id = ''

        # check if artist is already in database
        cursor.execute(get_artist,(data['artist'],))
        result = cursor.fetchone()
        if result==None:
            # if not in database add artist
            cursor.execute(add_artist,(data['artist'],))
            # get id of new row
            artist_id = cursor.lastrowid
        else:
            # if in database get artist id
            artist_id = result[0]

        # check if album is already in database
        cursor.execute(get_album,{
            'artist' : artist_id,
            'album' : data['album']
        })
        result = cursor.fetchone()
        if result==None:
            # if not in database add album
            cursor.execute(add_album,(data['album'],))
            album_id = cursor.lastrowid

            # join album and artist
            cursor.execute(add_artist_album,{
                'artist' : artist_id,
                'album' : album_id
            })

    cnx.commit()
    cursor.close()
    cnx.close()
