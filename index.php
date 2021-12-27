<!-- Required on first request of page only -->
<?php if (count($_GET) == 0): ?>
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
<?php endif; ?>

<?php

  // create connection to sql database
  $mysqli = new mysqli("127.0.0.1", "root", "123456", "scraper_db",3306);

  if (!empty($_GET['artist_id']) and !empty($_GET['album_id']) and !empty($_GET['position'])) {
    require 'get_single.php';
  }else{
    require 'get_multiple.php';
  }

?>
<?php require 'print_album.php'; ?>

<!-- Close tags required on first request of page -->
<?php if (count($_GET) == 0): ?>
  </div>
</body>
</html>
<?php endif; ?>
