<?php

$mysqli = new mysqli("127.0.0.1", "root", "123456", "scraper_db",3306);

$result = $mysqli->query("
  SELECT IFNULL(CONCAT('./img/',album.image_lrg),'./img/blank.svg') AS image,
  album.title AS title,
  artist.name AS artist,
  album.year AS year
  FROM artist INNER JOIN artist_album ON artist.id = artist_album.artist_id
  INNER JOIN album ON artist_album.album_id = album.id
  WHERE artist.id = 4;
");

$mysqli->close();

?>

<?php foreach ($result as $row): ?>
  <div class="grid-item" onclick="onClick(this)">
    <span class="id" hidden></span>
    <img src="<?php echo $row['image'] ?>" alt="">
    <div class="text-container">
      <p class="title"><?php echo $row['title'] ?></p>
      <p class="artist"><?php echo $row['artist'] ?></p>
      <p class="year"><?php echo $row['year'] ?></p>
    </div>
  </div>
<?php endforeach; ?>
