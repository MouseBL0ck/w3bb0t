#!/bin/sh

Package_array="apache2 libapache2-mod-php5 php5 php5-common php5-mysql php5-json mysql-server python2.7 python-mysqldb";

W3BB0T_folder="w3bb0t/";
WWW_instalation="/var/www/html/";
SERVER_path="/opt/w3bb0t_server/";

SQL_host=$1;
SQL_user=$2;
SQL_pass=$3;

SQL_query="CREATE DATABASE W3BB0t;";


if [ $LOGNAME != "root" ]
then
	echo "[~] E necessário executar como Root";

else

	if [ $# != "3"]
	then
		echo "[+] Syntax: $0 SQL_Host SQL_Username SQL_Password ";

	else
		apt-get update -y;

		for package in $Package_array; do
       			dpkg -s "$package" >/dev/null 2>&1 &&{
        		        echo "[*] $package ja esta instalado.";
        		} || {
                		apt-get install -y $package ;
        		}
		done

		echo "[!] Configurando Arquivos\n";
		php5 installer.php $SQL_host $SQL_user $SQL_pass;

		echo "[!] Criando Diretorios\n";
		mkdir $WWW_instalation$W3BB0T_folder;
		mkdir $SERVER_path;

		echo "[!] Criando Database\n";
		mysql -u $SQL_user -p$SQL_pass -e "$SQL_query";
		mysql -u $SQL_user -p$SQL_pass W3BB0t < w3bb0t.sql;

		echo "[!] Iniciando a instalacao\n";
		mv mysql_config.php $WWW_instalation$W3BB0T_folder/web/;

		cp -R bot_/ $WWW_instalation$W3BB0T_folder;
		cp -R bot_path/ $WWW_instalation$W3BB0T_folder;
		cp -R web/ $WWW_instalation$W3BB0T_folder;
		
		cp -R server_/ $SERVER_path;

		echo "[!] Dando as permicoes\n";

		chmod 774 $WWW_instalation$W3BB0T_folder/web/index.php;
		chmod 774 $WWW_instalation$W3BB0T_folder/web/login.php;
		chmod 774 $WWW_instalation$W3BB0T_folder/web/main.php;
		chmod 774 $WWW_instalation$W3BB0T_folder/web/settings.php;
		chmod 774 $WWW_instalation$W3BB0T_folder/web/info.php;
		chmod 774 $WWW_instalation$W3BB0T_folder/web/credits.php;

		chmod 774 $WWW_instalation$W3BB0T_folder/web/mysql_config.php;
		chmod 774 $WWW_instalation$W3BB0T_folder/web/config.php;
		chmod 774 $WWW_instalation$W3BB0T_folder/web/json.php;

		chmod 755 -R $WWW_instalation$W3BB0T_folder/bot_path/;

		chmod 775 -R $WWW_instalation$W3BB0T_folder/web/images/;
		chmod 775 -R $WWW_instalation$W3BB0T_folder/web/css/;
		chmod 775 -R $WWW_instalation$W3BB0T_folder/web/js/;

		chmod 770 -R $SERVER_path/server_/;

		chmod 777 $SERVER_path/server_/bot_ccommands;

		echo "[!] Instalado com sucesso\n";

	fi

fi

