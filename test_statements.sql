INSERT INTO source (title,url,container_tag,container_class,artist_tag,artist_class,album_tag,album_class) VALUES ('billboard','https://www.billboard.com/charts/top-album-sales','div','chart-list-item','div','chart-list-item__artist','span','chart-list-item__title-text')

select count(source_album.album_id) as Position,artist.name as Artist, album.title as Album, album.year as Year from source_album left join album on source_album.album_id = album.id left join artist on album.artist_id = artist.id group by album.id order by Position,Year desc;

insert into api (name) values ("discogs");
insert into api (name) values ("amazon");

insert into album_api values (12,1);
insert into album_api values (12,2);
