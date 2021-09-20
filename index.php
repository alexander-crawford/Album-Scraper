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
          ORDER BY source.title,list.position;
        ");

        $mysqli->close();

        ?>

        <?php
          function printHeading($source)
          {
            echo "<div class=\"grid-item grid-item--heading\">";
            echo "<h1>" . $source . "</h1>";
            echo "</div>";
          }
        ?>

        <?php
          function printAlbum($artist_id,$album_id,$image,$position,$title,$artist,$year)
          {
            echo "<div class=\"grid-item\" onclick=\"single(this)\" ondblclick=\"double(this)\" onmousedown=\"press(this,event)\" onmouseup=\"press(this,event)\">";
            echo "<span class=\"artist_id\" hidden>" . $artist_id . "</span>";
            echo "<span class=\"album_id\" hidden>" . $album_id . "</span>";

            if ($image == './img/blank.svg') {
              echo "<img class=\"img--off\" src=\"" . $image . "\"alt=\"\">";
              echo "<div class=\"text-container text-container-on\">";
            } else {
              echo "<img src=\"" . $image . "\"alt=\"\">";
              echo "<div class=\"text-container text-container--off\">";
            }
            echo "<p class=\"position\">" . $position . "</p>";
            echo "<p class=\"title\">" . $title . "</p>";
            echo "<p class=\"artist\">" . $artist . "</p>";
            echo "<p class=\"year\">" . $year . "</p>";
            echo "</div>"; // grid-item
            echo "</div>"; // text-container
          }
        ?>

        <div class="grid">
          <?php
          // TODO: use row number as hidden span and use grid layout to sort by this value
            $row_number = 0;
            $source = $result->fetch_row()[0];
            printHeading($source);
            foreach ($result as $row) {
              $row_number++;
              if ($source == $row['source']) {
                printAlbum($row['artist_id'],$row['album_id'],$row['image'],$row['position'],$row['title'],$row['artist'],$row['year']);
              }else {
                $source = $row['source'];
                printHeading($source);
                printAlbum($row['artist_id'],$row['album_id'],$row['image'],$row['position'],$row['title'],$row['artist'],$row['year']);
              }
            }
          ?>
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
          <?php // TODO: alter here to make use of print functions  ?>
          <div class="grid-item" onclick="single(this)" >
            <span class="id" hidden></span>
            <img src="<?php echo $row['image'] ?>" alt="">
            <div class="text-container text-container--off">
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
