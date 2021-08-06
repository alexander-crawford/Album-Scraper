<?php

$mysqli = new mysqli("127.0.0.1", "root", "123456", "scraper_db",3306);

$result = $mysqli->query("
  SELECT source.title AS source,
  list.position AS position,
  album.title AS title,
  album.year AS year,
  IFNULL(CONCAT('./img/',album.image_lrg),'./img/blank.svg') AS image,
  artist.name AS artist FROM list
  INNER JOIN source ON list.source_id = source.id
  INNER JOIN album ON list.album_id = album.id
  INNER JOIN artist_album ON album.id = artist_album.album_id
  INNER JOIN artist ON artist_album.artist_id = artist.id
  ORDER BY list.position;
");

$mysqli->close();

?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Album-Scraper</title>
    <script type="text/javascript" src="./js/masonry.pkgd.min.js" defer></script>
    <script type="text/javascript" src="./js/imagesloaded.pkgd.min.js" defer></script>
    <script type="text/javascript" src="./js/script.js" defer></script>
    <link rel="stylesheet" href="./css/styles.css">
  </head>
  <body>
    <div class="grid">
      <?php foreach ($result as $row): ?>
        <div class="grid-item">
          <img src="<?php echo $row['image'] ?>" alt="">
          <div class="text-container">
            <p class="position"><?php echo $row['position'] ?></p>
            <p class="title"><?php echo $row['title'] ?></p>
            <p class="artist"><?php echo $row['artist'] ?></p>
            <p class="year"><?php echo $row['year'] ?></p>
          </div>
        </div>
      <?php endforeach; ?>
    </div>
  </body>
</html>
