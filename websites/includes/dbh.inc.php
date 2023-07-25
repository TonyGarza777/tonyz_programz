<?php

$ServerName = "localhost";
$dBUsername = "root";
$dBPassword = "";
$dBName = "smashdojo";

$conn = mysqli_connect($ServerName, $dBUsername, $dBPassword, $dBName) or die();
/* if (!$conn) {
	die("connection failed: " . mysqli_connect_error());
} */