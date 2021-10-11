import mysql.connector
import json
import config

def insert(cnx,result,source_id):
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
            "VALUE (%s)"
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

    # Remove all entries from source_album table for the given source id
    def resetSource(source_id):

        reset_source = (
            "DELETE FROM source_album"
            "WHERE source_id = (%s)"
        )

        cursor.execute(reset_source,(source_id,))

    # Creates an entry in the source_album table joining the source and
    # album with the given id
    def joinSourceAlbum(source_id,album_id):
        # TODO: complete function
        pass

    data = json.loads(result)

    # print source
    print('\n',data['meta']['source'].upper())

    resetSource(source_id)

    if data['meta']['status']==200:

        # create counters to be printed on script end
        artist_count = 0
        album_count = 0

        # create cursor
        cursor = cnx.cursor()

        for data in data['data']:
            artist_id = getArtistID(data['artist'])
            album_id = getAlbumID(artist_id,data['album'])
            joinSourceAlbum(album_id,source_id)

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
