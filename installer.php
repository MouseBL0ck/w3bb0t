<?php
  // Installer mysql_config with credentials
  // Syntax argv[0] mysql_host mysql_user mysql_pass

  // Mysql credentials:
  $mysql_host = $argv[1];
  $mysql_user = $argv[2];
  $mysql_pass = $argv[3];

  // Read mysql_config:
  $config_read = fopen("./mysql_config.php", "r");
  $config_data = fread($config_read, filesize("./config.php"));
  fclose($config_read);

  // Edit mysql values:
  $config_data = str_replace("{host}", $mysql_host, $config_data);
  $config_data = str_replace("{user}", $mysql_user, $config_data);
  $config_data = str_replace("{pass}", $mysql_pass, $config_data);

  // Write mysql_config with new values:
  $config_write = fopen("./mysql_config.php", "w");
  $config_write_data = fwrite($config_write, $config_data);
  fclose($config_read);
  
?>
