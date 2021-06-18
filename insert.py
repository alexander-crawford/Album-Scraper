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
    "INSERT INTO artist"
    "(name)"
    "VALUES (%s)"
    )
    list = []
    for data in data['data']:
        tuple = (data['artist'],)
        list.append(tuple)
    print(list)

    cursor.executemany(add_artist,list)

    cnx.commit()
    cursor.close()
    cnx.close()
