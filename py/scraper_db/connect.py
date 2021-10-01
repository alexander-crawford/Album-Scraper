import mysql.connector
from mysql.connector import errorcode
import config

if __name__ == '__main__':
    connect()

def connect():
    # create table dictionary
    TABLES = {}

    # add table artist
    TABLES['artist'] = (
        "CREATE TABLE IF NOT EXISTS artist ("
        "id int UNSIGNED NOT NULL AUTO_INCREMENT,"
        "name varchar(256) NOT NULL,"
        "PRIMARY KEY (id),"
        "UNIQUE KEY (name)"
        ") ENGINE=InnoDB"
    )

    # add table album
    TABLES['album'] = (
        "CREATE TABLE IF NOT EXISTS album ("
        "id smallint UNSIGNED NOT NULL AUTO_INCREMENT,"
        "artist_id int UNSIGNED NOT NULL,"
        "title varchar(256) NOT NULL,"
        "year YEAR,"
        "image varchar(256),"
        "PRIMARY KEY (id,artist_id),"
        "UNIQUE KEY (image),"
        "FOREIGN KEY (artist_id)"
        "REFERENCES artist (id)"
        ") ENGINE=InnoDB"
    )

    # add table source
    TABLES['source'] = (
        "CREATE TABLE IF NOT EXISTS source ("
        "id int UNSIGNED NOT NULL AUTO_INCREMENT,"
        "title varchar(256) NOT NULL,"
        "PRIMARY KEY (id)"
        ") ENGINE=InnoDB"
    )

    # add table list
    TABLES['list'] = (
        "CREATE TABLE IF NOT EXISTS list ("
        "position smallint UNSIGNED NOT NULL,"
        "source_id int UNSIGNED,"
        "album_id int UNSIGNED,"
        "FOREIGN KEY (source_id)"
        "REFERENCES source (id),"
        "FOREIGN KEY (album_id)"
        "REFERENCES album (id),"
        "PRIMARY KEY (position, source_id)"
        ") ENGINE=InnoDB"
    )
    # create connection to mysql database
    cnx = mysql.connector.connect(user=config.mysql_username,password=config.mysql_password)

    # create cursor
    cursor = cnx.cursor()

    # set database name
    DB_NAME = "scraper_db"

    # create database if not existing
    try:
        cursor.execute("USE {}".format(DB_NAME))
        print(DB_NAME," OK")
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            try:
                cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
            except mysql.connector.Error as err:
                print("Failed creating database: {}".format(err))
                exit()
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(' error ',err)
            exit()


    # loop over create table statements
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("{} table ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            print(' error ',err)
            exit()
        else:
            print("OK")

    # reset cursor
    cursor.close()

    # reutrn connection to db
    return cnx
