<?php
session_start();
include_once 'includes/dbh.inc.php';

?>
<!doctype html>
	<meta charset="utf-8">
	<meta lang="en">
	<link rel="stylesheet" href="style.css">
<header>
<style>
	wrapper p {
		color: white;
	}
</style>

	<div class="wrapper">
		<div class="topnav">
					<a href="rules.html">Rules</a>
					<a href="home.php">Home</a>
					<a href='index.html'>logout</a>
					
			
			</ul>
		</nav>
	
</div>
</header>
<body>
	
	<h1>customize your profile picture</h1>
	
<form action="upload.php" method="POST" enctype="multipart/form-data">
	
<input type="file" name="file">
<button type="submit" name="submit">UPLOAD</button>
</form>
 <div class="container">
 	<?php
 	
 	 ?>
 	<div class="wrapper">
 		<nav>
 		<!-- <?php


 		
 		$username = $_POST["uid"];
 		$sql = SELECT usersUid WHERE usersId = "$_SESSION['login'];";
 		$result = mysqli_query($conn, $sql);
 		$resultCheck = mysqli_num_rows($result);

 		if(!isset($_SESSION['login']) && $_SESSION['login'] != ''){

 		}

		?> -->
			<p>
                Welcome
                <strong>
                    <?php echo $_SESSION['username']; ?>
                </strong>
            </p>


			
 		</nav>
 	</div>
</div>



<script src="jquery/jquery.js"></script>
<script>
	
</script>

<script>
	
</script>
</body>
</html>