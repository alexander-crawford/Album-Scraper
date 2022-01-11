<?php foreach ($result as $row): ?>

  <?php if ($row['image'] == './blank.svg'): ?>

    <div class="grid-item" ondblclick="double(this)">
      <img class="img--off" src="<?php echo $row['image'] ?>" alt="">
      <div class="text-container text-container--on">

  <?php else: ?>

    <div class="grid-item" onclick="single(this)" ondblclick="double(this)">
      <img src="<?php echo $row['image'] ?>" alt="">
      <div class="text-container text-container--off">

  <?php endif; ?>

        <span class="artist_id" hidden><?php echo $row['artist_id'] ?></span>
        <span class="album_id" hidden><?php echo $row['album_id'] ?></span>

        <?php if (empty($_GET['position'])): ?>

        <p class="position"><?php echo $row['position'] ?></p>

        <?php else: ?>

        <p class="position" hidden><?php echo $_GET['position'] ?></p>

        <?php endif; ?>

        <p class="title"><?php echo $row['title'] ?></p>
        <p class="artist"><?php echo $row['artist'] ?></p>
        <p class="year"><?php echo $row['year'] ?></p>

      </div>
    </div>

<?php endforeach; ?>
