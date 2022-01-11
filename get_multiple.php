<?php

  $statement = $mysqli->prepare("

    SELECT * FROM main
    ORDER BY position
    LIMIT 8
    OFFSET ?;

  ");

  $page = 0;

  if (isset($_GET['page'])) {

    $page_raw = $_GET['page'];

    $page_sanitised = filter_var($page_raw,FILTER_SANITIZE_NUMBER_INT);

    if (filter_var($page_sanitised,FILTER_VALIDATE_INT)) {

      $page = ($page_sanitised * 8) - 8;

    }

  }

  $statement->bind_param("i",$page);

  $statement->execute();

  $result = $statement->get_result();

  $mysqli->close();

?>
