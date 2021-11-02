<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Album-Scraper</title>
    <script type="text/javascript" src="./js/jquery.min.js" defer></script>
    <script type="text/javascript" src="./js/isotope.pkgd.min.js" defer></script>
    <script type="text/javascript" src="./js/infinite-scroll.pkgd.min.js" defer></script>
    <script type="text/javascript" src="./js/script.js" defer></script>
    <link rel="stylesheet" href="./css/styles.css">
  </head>
  <body>
    <div class="grid">
    <?php
      $mysqli = new mysqli("127.0.0.1", "root", "123456", "scraper_db",3306);

      $statement = $mysqli->prepare("
        SELECT ROW_NUMBER() OVER (ORDER BY count(source_album.album_id),
        album.year DESC,artist.name ASC, album.title ASC) position,
        artist.id AS artist_id,
        album.id AS album_id,
        IFNULL(CONCAT('./img/',album.image),'./img/blank.svg') AS image,
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

      if (!empty($_GET['artist_id']) and !empty($_GET['album_id']) and !empty($_GET['row_num'])) {
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
      }

    ?>
    <?php foreach ($result as $row): ?>
      <div class="grid-item" onclick="single(this)" ondblclick="double(this)"
      onmousedown="press(this,event)" onmouseup="press(this,event)">
        <img src="<?php echo $row['image'] ?>" alt="">
        <div class="text-container text-container--off">
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
