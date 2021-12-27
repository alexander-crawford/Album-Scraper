<?php
  $statement = $mysqli->prepare("
    SELECT ROW_NUMBER() OVER (ORDER BY count(source_album.album_id),
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
    GROUP BY album.id
    LIMIT 8
    OFFSET ?;
  ");

  $page = 0;

  if (!empty($_GET['page']) and filter_var($_GET['page'],FILTER_VALIDATE_INT)) {

    $page = ($_GET['page'] * 8) - 8;

  }

  $statement->bind_param("i",$page);

  $statement->execute();

  $result = $statement->get_result();

  $mysqli->close();
?>
