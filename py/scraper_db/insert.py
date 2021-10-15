import mysql.connector
import json
import config

def insert(cnx,result,source_id):

    # Keep track of how many artist and albums have been added to the database
    class Counter:
        """Keeps count of how many artists and albums
        have been added to the database."""

        def __init__(self):
            self.album_count = 0
            self.artist_count = 0

        def getAlbumCounter(self):
            return self.album_count

        def incrementAlbumCounter(self):
            self.album_count += 1

        def getArtistCounter(self):
            return self.artist_count

        def incrementArtistCounter(self):
            self.artist_count += 1

    # Returns artist id for artist name given as argument value
    # if artist is not found in db a new entry is added and the id returned
    def getArtistID(cursor,artist):

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
            counter.incrementArtistCounter()

            # return id of new row
            return cursor.lastrowid

        else:
            # if in database return artist id
            return result[0]

    # Returns album id for album name given as argument value
    # if album is not found in db a new entry is added and the id returned
    def getAlbumID(cursor,artist_id,album_title):

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
            counter.incrementAlbumCounter()

            # return album id
            return cursor.lastrowid


        else:
            # if in database return album id
            return result[0]

    # Remove all entries from source_album table for the given source id
    def resetSource(cursor,source_id):

        reset_source = (
            "DELETE FROM source_album "
            "WHERE source_id = (%s)"
        )

        cursor.execute(reset_source,(source_id,))

    # Creates an entry in the source_album table joining the source and
    # album with the given id
    def joinSourceAlbum(cursor,source_id,album_id):

        add_source_album = (
            "INSERT INTO source_album "
            "VALUES (%(source)s,%(album)s)"
        )

        cursor.execute(add_source_album,{
            'source' : source_id,
            'album' : album_id
        })

    data = json.loads(result)

    # print source
    print('\n',data['meta']['source'].upper())

    if data['meta']['status']==200:

        # create counter
        counter = Counter()

        # create cursor
        cursor = cnx.cursor()

        resetSource(cursor,source_id)

        for data in data['data']:
            artist_id = getArtistID(cursor,data['artist'])
            album_id = getAlbumID(cursor,artist_id,data['album'])
            joinSourceAlbum(cursor,album_id,source_id)

        # commnit changes to db
        cnx.commit()
        # reset cursor
        cursor.close()

        # print counters
        print(counter.getArtistCounter(),"artists added")
        print(counter.getAlbumCounter(),"albums added")

    else:
        print("** fail **")

if __name__ == '__main__':
    insert()
