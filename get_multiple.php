<?php

  $statement = $mysqli->prepare("

    SELECT * FROM main
    ORDER BY position
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

?>
