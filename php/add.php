<?php
if (!mysql_connect("localhost", "root", "12345"))
    die("Error Username or Password");
if (!mysql_select_db("foo"))
    die("Error Database");

echo "Merhaba" . $_POST["ad"];
mysql_query("insert into kul (name) values('" . $_POST["ad"] . "')");

echo "Kaydınız tamamlandı...";
?>

