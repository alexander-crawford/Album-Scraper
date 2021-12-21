use scraper_db;

INSERT INTO source (title,url,container_tag,container_class,artist_tag,artist_class,album_tag,album_class) VALUES ('pitchfork','https://pitchfork.com/reviews/albums','div','review','ul','artist-list review__title-artist','h2','review__title-album');

insert into api (name) values ("discogs");
