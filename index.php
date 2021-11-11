<?php if (count($_GET) == 0): ?>
  <!DOCTYPE html>
  <html lang="en" dir="ltr">
  <?php require 'head.php'; ?>
  <body>
    <div class="grid">
<?php endif; ?>
    <?php
      $mysqli = new mysqli("127.0.0.1", "root", "123456", "scraper_db",3306);

      if (!empty($_GET['artist_id']) and !empty($_GET['album_id']) and !empty($_GET['position'])) {
        $statement = $mysqli->prepare("
          SELECT IFNULL(CONCAT('./img/',album.image),'./img/blank.svg') AS image,
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
      }else{
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
      }

    ?>
    <?php foreach ($result as $row): ?>
      <div class="grid-item" onclick="single(this)" ondblclick="double(this)">
        <img src="<?php echo $row['image'] ?>" alt="">
        <div class="text-container text-container--off">
          <span class="artist_id" hidden><?php echo $row['artist_id'] ?></span>
          <span class="album_id" hidden><?php echo $row['album_id'] ?></span>
          <?php if (empty($_GET['position'])): ?>
            <p class="position"><?php echo $row['position'] ?></p>
          <?php else: ?>
            <p class="position"><?php echo $_GET['position'] ?></p>
          <?php endif; ?>
          <p class="title"><?php echo $row['title'] ?></p>
          <p class="artist"><?php echo $row['artist'] ?></p>
          <p class="year"><?php echo $row['year'] ?></p>
        </div>
      </div>
    <?php endforeach; ?>
<?php if (count($_GET) == 0): ?>
    </div>
  </body>
</html>
<?php endif; ?>
