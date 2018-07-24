#!/bin/sh

W3BB0T_folder="w3bb0t/";
WWW_instalation="/var/www/html/";
SERVER_path="/opt/w3bb0t_server/";

SQL_user=$1;
SQL_pass=$2;

SQL_query="DROP DATABASE w3bbot;";

if [ $LOGNAME != "root" ]
then
	echo "[~] E necessário executar como Root\n";
elif [ $LOGNAME = "root" ] && [ $# != "0" ] && [ $# = "2" ]
then
	echo "[!] Deletando Diretorios\n";
	rm -R $WWW_instalation$W3BB0T_folder;
	rm -R $SERVER_path;
	
	echo "[!] Deletando Database\n";
	mysql -u $SQL_user -p $SQL_pass -e "$SQL_query";

else
	echo "[+] Syntax: $0 SQL_Username SQL_Password ";

fi
