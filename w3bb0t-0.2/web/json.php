<?php
  //Functions new version json.php

  //Fucntion for to save json:
  function Spend_saveFile($config_json){
    $config_file = fopen("server_/bot_ccommands", "w");

    fwrite($config_file, $config_json);
    fclose($config_file);
  }

  //Function save and encode command:
  function Spend_command($type, $command, $bots){
    if($type == "command"){
      $config_array = array(
        "command"     => $command,
        "bot"         => $bots
      );

      $config_json = json_encode($config_array);

      Spend_saveFile($config_json);

    }

  }

?>
