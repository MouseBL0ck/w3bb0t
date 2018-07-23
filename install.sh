#!/bin/sh


#Ainda falta instalar o modulos do python

Package_array="apache2 libapache2-mod-php5 php5 php5-common php5-mysql php5-json mysql-server python2.7 python-pip";

W3BB0T_folder="w3bb0t/";
WWW_instalation="/var/www/html/";
SERVER_path="/opt/w3bb0t_server/";

SQL_user=$1;
SQL_pass=$2;

SQL_query="CREATE DATABASE w3bbot;";


if [ $LOGNAME != "root" ]
then
	echo "[~] E necessário executar como Root";

else
	if [ $# = "0" ]
	then
		echo "[+] Syntax: $0 SQL_Username SQL_Password ";

	elif [ $# != "0" ]
	then

		for package in $Package_array; do
       			dpkg -s "$package" >/dev/null 2>&1 &&{
        		        echo "[*] $package ja esta instalado.";
        		} || {
                		apt-get install -y $package ;
        		}
		done

		echo "[!] Criando Diretorios\n";
		mkdir $WWW_instalation$W3BB0T_folder;
		mkdir $SERVER_path;

		echo "[!] Criando Database\n";
		mysql -u $SQL_user -p$SQL_pass -e "$SQL_query";
		mysql -u $SQL_user -p$SQL_pass w3bbot < w3bbot.sql;

		echo "[!] Iniciando a instalacao\n";
		cp -R bot_/ $WWW_instalation$W3BB0T_folder;
		cp -R bot_path/ $WWW_instalation$W3BB0T_folder;
		cp -R Documentation/ $WWW_instalation$W3BB0T_folder;
		cp -R images/ $WWW_instalation$W3BB0T_folder;

		cp -R index.php $WWW_instalation$W3BB0T_folder;
		cp -R json.php $WWW_instalation$W3BB0T_folder;
		cp -R rg.php $WWW_instalation$W3BB0T_folder;

		cp -R server_/ $SERVER_path;

		echo "[!] Dando as permicoes\n";

		chmod 770 $WWW_instalation$W3BB0T_folder/index.php;
		chmod 770 $WWW_instalation$W3BB0T_folder/rg.php;
		chmod 770 $WWW_instalation$W3BB0T_folder/json.php;

		chmod 755 $WWW_instalation$W3BB0T_folder/bot_path/*;
		chmod 770 $WWW_instalation$W3BB0T_folder/images/*;

		chmod 770 -R $SERVER_path/server_/;

		echo "[!] Instalado com sucesso\n";


	fi

fi
