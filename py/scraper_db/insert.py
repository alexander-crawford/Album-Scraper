import mysql.connector
import json
import config

def insert(cnx,result):
    # Returns artist id for artist name given as argument value
    # if artist is not found in db a new entry is added and the id returned
    def getArtistID(artist):

        get_artist = (
            "SELECT id FROM artist "
            "WHERE name = (%s)"
        )

        add_artist = (
            "INSERT INTO artist "
            "(name) "
            "VALUES (%s)"
        )

        # check if artist is already in database
        cursor.execute(get_artist,(artist,))
        result = cursor.fetchone()

        if result==None:
            # if not in database add artist
            cursor.execute(add_artist,(data['artist'],))

            # increment counter
            artist_count += 1

            # return id of new row
            return cursor.lastrowid

        else:
            # if in database return artist id
            return result[0]

    # Returns album id for album name given as argument value
    # if album is not found in db a new entry is added and the id returned
    def getAlbumID(artist_id,album_title):

        get_album = (
            "SELECT id FROM album "
            "WHERE title = %(album)s AND artist_id = %(artist)s"
        )

        add_album = (
            "INSERT INTO album "
            "(title,artist_id) "
            "VALUES (%(album)s,%(artist)s)"
        )

        # check if album is already in database
        cursor.execute(get_album,{
            'album' : album_title,
            'artist' : artist_id
        })
        result = cursor.fetchone()

        if result==None:
            # if not in database add album
            cursor.execute(add_album,{
                'album' : album_title,
                'artist' : artist_id
            })

            # increment counter
            album_count += 1

            # return album id
            return cursor.lastrowid


        else:
            # if in database return album id
            return result[0]

    data = json.loads(result)

    # print source
    print('\n',data['meta']['source'].upper())

    if data['meta']['status']==200:

        # create counters to be printed on script end
        artist_count = 0
        album_count = 0

        # create cursor
        cursor = cnx.cursor()

        add_artist_album = (
            "INSERT INTO artist_album "
            "(artist_id,album_id) "
            "VALUES (%(artist)s,%(album)s)"
        )

        for data in data['data']:
            artist_id = getArtistID(data['artist'])
            album_id = getAlbumID(data['album'])

            # join album and artist
            cursor.execute(add_artist_album,{
            'artist' : artist_id,
            'album' : album_id
            })

            # add album into position list
            cursor.execute(add_to_list,{
            'position' : data['position'],
            'source_id' : source_id,
            'album_id' : album_id
            })


        # commnit changes to db
        cnx.commit()
        # reset cursor
        cursor.close()

        # print counters
        print(artist_count,"artists added")
        print(album_count,"albums added")

    else:
        print("** fail **")

if __name__ == '__main__':
    insert()
