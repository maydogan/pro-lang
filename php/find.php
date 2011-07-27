<?php
if (!mysql_connect("localhost", "root", "12345"))
	die("Error Username or Password");
if (!mysql_select_db("foo"))
	die("Error Database");

$result= mysql_query("select * from kul where name = '" . $_POST["ad"] . "'");
$row = mysql_fetch_assoc($result);

if ($row) {
	echo $row["name"];
	echo $row["id"];
} 
else
	echo "Boyle bir kullanici yok";
?>
