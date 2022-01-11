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

  $artist_id_raw = $_GET["artist_id"];

  $artist_id_sanitised = filter_var($artist_id_raw,FILTER_SANITIZE_NUMBER_INT);

  if (filter_var($artist_id_sanitised,FILTER_VALIDATE_INT)) {

    $artist_id = $artist_id_sanitised;

  }

  $album_id_raw = $_GET["album_id"];

  $album_id_sanitised = filter_var($album_id_raw,FILTER_SANITIZE_NUMBER_INT);

  if (filter_var($album_id_sanitised,FILTER_VALIDATE_INT)) {

    $album_id = $album_id_sanitised;

  }

  $statement->bind_param("ii",$artist_id,$album_id);

  $statement->execute();

  $result = $statement->get_result();

  $mysqli->close();

?>
