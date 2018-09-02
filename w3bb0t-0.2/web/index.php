<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>W3bb0t Botnet</title>
    <link rel="stylesheet" type="text/css" href="css/index.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <link rel="stylesheet" type="text/css" href="css/login.css">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    <script type="text/javascript" src="js/checker_bot.js"></script>
  </head>
  <body>
		<div id="wb_banner">
      <a id="link_banner" href="index.php">W3BB0T Botnet</a>
    </div>

    <div id="wb_menu">
			<div id="wb_menu_itens">
				<div class="wb_menu_buttons"><a href="?page=main.php">Main Page</a></div>
        <div class="wb_menu_buttons"><a href="?page=settings.php">Settings </a></div>
				<div class="wb_menu_buttons"><a href="?page=info.php">Info </a></div>
				<div class="wb_menu_buttons"><a href="?page=credits.php">Credits </a></div>
			</div>
    </div>

		<div id="wb_page">
      <?php
        session_start();

        $pages = array('main.php', 'info.php', 'settings.php', 'credits.html');

        if(isset($_SESSION['Login']['Loged']) and $_SESSION['Login']['Loged'] != '1'){

          include ('login.php');

        }elseif(isset($_SESSION['Login']['Loged']) and $_SESSION['Login']['Loged'] == '1'){

          if(isset($_GET['page']) and in_array($_GET['page'], $pages)){

            include ($_GET['page']);

          }elseif(!isset($_GET['page']) or $_GET['page'] == Null){

            include ('main.php');

          }

        }else{

          include ('login.php');

        }


      ?>
		</div>
  </body>
</html>
