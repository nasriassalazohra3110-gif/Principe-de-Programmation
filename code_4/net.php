<?php
  $url = "https://localhost:5000/students";
  $response = file_get_contents($url);
  
  echo "<pre>";
  echo $response;
  echo "</pre>";
?>