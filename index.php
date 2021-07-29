<?php

$mysqli = new mysqli("127.0.0.1", "root", "123456", "scraper_db",3306);

$result = $mysqli->query("
  SELECT source.title AS source,
  list.position AS position,
  album.title AS album,
  album.year AS year,
  album.image_lrg AS image,
  artist.name AS artist FROM list
  INNER JOIN source ON list.source_id = source.id
  INNER JOIN album ON list.album_id = album.id
  INNER JOIN artist_album ON album.id = artist_album.album_id
  INNER JOIN artist ON artist_album.artist_id = artist.id
  ORDER BY list.position;
");

$mysqli->close();

?>

<style>
  table, td {
    border: 1px solid #333;
    border-collapse: collapse;
    padding: 5px;
  }
  img{
    max-width: 100%;
  }
</style>

<h1><?php echo $result->fetch_row()[0] ?></h1>


<table>
    <tbody>
        <tr>
            <td>Position</td>
            <td>Artist</td>
            <td>Album</td>
            <td>Year</td>
            <td>Image</td>
        </tr>
        <?php foreach ($result as $row): ?>
          <tr>
            <td><?php echo $row['position'] ?></td>
            <td><?php echo $row['artist'] ?></td>
            <td><?php echo $row['album'] ?></td>
            <td><?php echo $row['year'] ?></td>
            <td><img src="./img/<?php echo $row['image'] ?>" alt=""></td>
          </tr>
        <?php endforeach; ?>
    </tbody>
</table>
