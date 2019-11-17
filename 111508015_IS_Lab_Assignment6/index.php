<?php
include 'connection.php';
$username = $_POST['username'];
$password = $_POST['password'];

/*$username = 'vivek';
$password = 'bhave';*/
/*echo "".$username;*/
$query = "SELECT * FROM users WHERE username ='" .$username. "' AND password = '".$password."';";
$val = mysqli_query($db, $query);
$result = mysqli_fetch_array($val);
echo count($result);
if(count($result) >= 1){
	echo "<script type='text/javascript'>alert('Login successful!!');window.location = 'index.html'</script>";
}
else{
	echo "<script type='text/javascript'>alert('Username or Password maybe wrong!!');window.location = 'index.html'</script>";
}
?>
