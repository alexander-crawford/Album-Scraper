<?php

  $statement = $mysqli->prepare("
    SELECT IFNULL(CONCAT('./img/',album.image),'./blank.svg') AS image,
    album.title AS title,
    artist.name AS artist,
    album.year AS year
    FROM album
    INNER JOIN artist ON album.artist_id = artist.id
    WHERE artist.id = (?)
    AND album.id <> (?);
  ");

  $artist_id = $_GET["artist_id"];

  $album_id = $_GET["album_id"];

  $statement->bind_param("ii",$artist_id,$album_id);

  $statement->execute();

  $result = $statement->get_result();

  $mysqli->close();
  
?>
