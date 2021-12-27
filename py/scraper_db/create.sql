USE scraper_db;

CREATE TABLE main AS
SELECT ROW_NUMBER() OVER (ORDER BY COUNT(source_album.album_id) DESC,
album.year DESC,artist.name ASC, album.title ASC) position,
artist.id AS artist_id,
album.id AS album_id,
IFNULL(CONCAT('./img/',album.image),'./blank.svg') AS image,
album.title AS title,
artist.name AS artist,
album.year AS year
FROM album
LEFT JOIN source_album ON album.id = source_album.album_id
INNER JOIN artist ON album.artist_id = artist.id
GROUP BY album.id;

DELETE FROM main WHERE TRUE;

INSERT INTO main
SELECT ROW_NUMBER() OVER (ORDER BY COUNT(source_album.album_id) DESC,
album.year DESC,artist.name ASC, album.title ASC) position,
artist.id AS artist_id,
album.id AS album_id,
IFNULL(CONCAT('./img/',album.image),'./blank.svg') AS image,
album.title AS title,
artist.name AS artist,
album.year AS year
FROM album
LEFT JOIN source_album ON album.id = source_album.album_id
INNER JOIN artist ON album.artist_id = artist.id
GROUP BY album.id;

SELECT * FROM main order by position;
