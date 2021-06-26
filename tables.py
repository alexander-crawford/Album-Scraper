import mysql.connector

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
    "id int UNSIGNED NOT NULL AUTO_INCREMENT,"
    "title varchar(256) NOT NULL,"
    "date DATE,"
    "PRIMARY KEY (id)"
    ") ENGINE=InnoDB"
)

# add table artist_album
TABLES['artist_album'] = (
    "CREATE TABLE IF NOT EXISTS artist_album ("
    "artist_id int UNSIGNED NOT NULL,"
    "album_id int UNSIGNED NOT NULL,"
    "FOREIGN KEY (artist_id)"
    "REFERENCES artist (id),"
    "FOREIGN KEY (album_id)"
    "REFERENCES album (id)"
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
    "PRIMARY KEY (position)"
    ") ENGINE=InnoDB"
)

# create connection to mysql database
cnx = mysql.connector.connect(user='root',password='123456', database='album_scraper')

# create cursor
cursor = cnx.cursor()

# loop over create table statements
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("{} table ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        print(' error ',err)
    else:
        print("OK")

# reset cursor
cursor.close()

# close connection to mysql database
cnx.close()
