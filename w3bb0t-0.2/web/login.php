<form action="" method="post" id="wb_login_form">
  <div id="wb_login_input">
    <label class="wb_login_text">User </lable><input type="text" name="user_login"><br>
    <label class="wb_login_text">Password </label><input type="password" name="pass_login"><br><br>
    <input type="submit" id="wb_login_submit" name="submit_login" value="submit">
  </div>
</form>
<?php
  include 'config.php';
  include 'mysql_config.php';

  $m_connection = mysql_connect($mysql_host, $mysql_user, $mysql_pass);
  mysql_select_db($mysql_db, $m_connection);

  if(isset($_SESSION['Login']) and $_SESSION['Login']['Loged'] != '1'){

    $user_login = $_SESSION['Login']['user_login'];
    $pass_login = $_SESSION['Login']['pass_login'];

    $bd_session_login = mysql_query("SELECT web_user, web_pass FROM Web_Login WHERE web_user='$user_login' AND web_pass='$pass_login' LIMIT 1", $m_connection);

    if(mysql_num_rows($bd_session_login) == 1){

      $_SESSION['Login']['Loged'] = 1;

      header('Location: index.php');

    }else{

      session_destroy();

    }

  }elseif(isset($_SESSION['Login']) and $_SESSION['Login']['Loged'] == '1'){

    header('Location: index.php');

  }elseif(isset($_POST['user_login']) and isset($_POST['pass_login'])){

    $user_login = md5($_POST['user_login']);
    $pass_login = md5($_POST['pass_login']);

    $bd_login = mysql_query("SELECT web_user, web_pass FROM Web_Login WHERE web_user='$user_login' AND web_pass='$pass_login' LIMIT 1", $m_connection);

    if(mysql_num_rows($bd_login) == 1){

      session_start();

      $_SESSION['Login']['user_login'] = $user_login;
      $_SESSION['Login']['pass_login'] = $pass_login;
      $_SESSION['Login']['Loged'] = '1';

      print_r($_SESSION['Login']);

      header('Location: index.php');

    }
  }

  mysql_close($m_connection);

?>
