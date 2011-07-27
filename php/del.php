<?php
if (!mysql_connect("localhost", "root", "12345"))
	die("Error Username or Password");
if (!mysql_select_db("foo"))
	die("Error Database");

$result = mysql_query("select * from kul where name = '" . $_POST["ad"]. "'");
$row = mysql_fetch_assoc($result);

if ($row){
	mysql_query("delete from kul where name = '".$_POST["ad"]."'");
	echo $row["name"]. "adlı kullanıcı veritabanindan silindi...";
}
else
	echo "Bu kullanici kayitlarda bulunmamaktadir...";
?>

