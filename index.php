<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Album-Scraper</title>
    <script type="text/javascript" src="./js/isotope.pkgd.min.js" defer></script>
    <script type="text/javascript" src="./js/imagesloaded.pkgd.min.js" defer></script>
    <script type="text/javascript" src="./js/script.js" defer></script>
    <link rel="stylesheet" href="./css/styles.css">
  </head>
  <body>
      <?php if (is_null($_SERVER['QUERY_STRING'])): ?>
        <?php

        $mysqli = new mysqli("127.0.0.1", "root", "123456", "scraper_db",3306);

        $result = $mysqli->query("
          SELECT source.title AS source,
          artist.id AS artist_id,
          album.id AS album_id,
          IFNULL(CONCAT('./img/',album.image_lrg),'./img/blank.svg') AS image,
          list.position AS position,
          album.title AS title,
          artist.name AS artist,
          album.year AS year FROM list
          INNER JOIN source ON list.source_id = source.id
          INNER JOIN album ON list.album_id = album.id
          INNER JOIN artist_album ON album.id = artist_album.album_id
          INNER JOIN artist ON artist_album.artist_id = artist.id
          ORDER BY list.position;
        ");

        $mysqli->close();

        ?>
        <div class="grid">
          <div class="stamp">
            <h1><?php echo ucfirst($result->fetch_row()[0]) ?></h1>
          </div>
          <?php foreach ($result as $row): ?>
            <div class="grid-item" onclick="single(this)" ondblclick="double(this)">
              <span class="artist_id" hidden><?php echo $row['artist_id'] ?></span>
              <span class="album_id" hidden><?php echo $row['album_id'] ?></span>
              <img class="test" src="<?php echo $row['image'] ?>" alt="">
              <div class="text-container--off">
                <p class="position"><?php echo $row['position'] ?></p>
                <p class="title"><?php echo $row['title'] ?></p>
                <p class="artist"><?php echo $row['artist'] ?></p>
                <p class="year"><?php echo $row['year'] ?></p>
              </div>
            </div>
          <?php endforeach; ?>
        </div>
      <?php else: ?>
        <?php

        $mysqli = new mysqli("127.0.0.1", "root", "123456", "scraper_db",3306);

        $statement = $mysqli->prepare("
          SELECT IFNULL(CONCAT('./img/',album.image_lrg),'./img/blank.svg') AS image,
          album.title AS title,
          artist.name AS artist,
          album.year AS year
          FROM artist INNER JOIN artist_album ON artist.id = artist_album.artist_id
          INNER JOIN album ON artist_album.album_id = album.id
          WHERE artist.id = (?) AND album.id <> (?);
        ");

        $artist_id = $_GET["artist_id"];

        $album_id = $_GET["album_id"];

        $statement->bind_param("ii",$artist_id,$album_id);

        $statement->execute();

        $result = $statement->get_result();

        $mysqli->close();

        ?>

        <?php foreach ($result as $row): ?>
          <div class="grid-item" onclick="single(this)" >
            <span class="id" hidden></span>
            <img src="<?php echo $row['image'] ?>" alt="">
            <div class="text-container--off">
              <p class="position" hidden><?php echo $_GET["position"] ?></p>
              <p class="title"><?php echo $row['title'] ?></p>
              <p class="artist"><?php echo $row['artist'] ?></p>
              <p class="year"><?php echo $row['year'] ?></p>
            </div>
          </div>
        <?php endforeach; ?>
      <?php endif; ?>
  </body>
</html>
