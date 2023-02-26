<?php

if (isset($_POST["submit"])) {

	$username = $_POST["uid"];
	$pwd = $_POST["pwd"];


	require_once 'dbh.inc.php';
	require_once 'functions.inc.php';

	if (empty($username) || empty($pwd)) {
	header("location: ../index.php?error=emptyinput");
	exit();
	}
	
	if($uid && $pwd !== false) {
	header("location: ../index.php?error=invaliduserorpassword");
	exit();
	}



	if($uid && $pwd === true) {
	header("location: ../home.php?signupsuccess");
	exit();
	}


validateUser($conn, $username, $pwd);
//some how remember the user is logged in
header("location: ../index.php");
	exit();
}
