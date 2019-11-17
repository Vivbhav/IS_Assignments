<?php

$message = '';
$username = 'root';
$password = 'vivbhav97';
$db = new mysqli('localhost', $username, $password, 'injection');
if ($db->connect_error){
	$message = $db->connect_error;
}
else{
	echo $message;
}
?>
