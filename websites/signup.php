<!doctype html>
<html lang="en">
<meta charset="utf-8">
<head>
	<title>Welcome to Smash Dojo</title>
	<link rel="stylesheet" type="text/css" href="css/styles.css">
</head>

<style>
  p {
    color: white;
  }
  body p {
    text-align: center;
  }
</style>

	<body>
		<h1>Signup here and climb the ranks.</h1>
		
<form action="includes/signup.inc.php" method="post">
  <div class="container">
    <h1>Sign Up</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" required>

	<label for="uid"><b>username</b></label>
    <input type="text" placeholder="Enter Username" name="uid" required>


    <label for="pwd"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="pwd" required>

    <label for="pwd-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Repeat Password" name="pwdRepeat" required>

    <label>
      <input type="checkbox" checked="checked" name="remember" style="margin-bottom:15px"> Remember me
    </label>

    <p>By creating an account you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn" name="submit">Sign Up</button>
    </div>
  </div>
</form>
		<video autoplay muted loop class="myvideo">
			<source src="videos/fd.mp4">
			<source src="background.ogg">
			<p>This is not accesible</p>
		</video>
<?php
   if (isset($_GET["error"])) {
      if ($_GET["error"] == "emptyinput") {
          echo "<p>Fill in all fields</p>";
      }
      
      else if ($_GET["error"] == "invaliduid") {
          echo "<p>Invalid Username</p>";
      }
      else if ($_GET["error"] == "invalidemail") {
          echo "<p>Invalid Email</p>";
      }
      else if ($_GET["error"] == "passwordsdontmatch") {
          echo "<p>wrong password</p>";
      }
      else if ($_GET["error"] == "stmtfailed") {
          echo "<p>Invalid Username</p>";
      }
      else if ($_GET["error"] == "usernametaken") {
          echo "<p>Username taken!</p>";
      }
      else if ($_GET["error"] == "none") {
          echo "<p>You have signed up!</p>";
      }
   }
?>

	</body>
</html>