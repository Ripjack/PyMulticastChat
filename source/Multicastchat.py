from socket import *
import threading, os, struct
MGRP_IP = '225.100.1.1'
MGRP_PRT = 3515

def listen():
	while True:
		data, addr = listensock.recvfrom(1024)
		data = str(data.decode('utf-8', 'ignore'))
		historylist.append(data)
		history()
		print('\n' + user)

def history():
	os.system('cls')
	for item in historylist:
		print(item)



listensock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
transsock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
listensock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
transsock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 2)
mreq = struct.pack("4sl", inet_aton(MGRP_IP), INADDR_ANY)
listensock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
listensock.bind(('', MGRP_PRT))



#RECVIP = input("local IP: ")
#RECVPRT = int(input("local port: "))
#SENDIP = input("remote ip: ")
#SENDPRT = int(input("remote port: "))
USER = input('Username: ')
os.system('cls')
historylist = []
user = USER + ": "
print('\n' + user)

passivelistener = threading.Thread(target=listen)
passivelistener.start()

while True:
	message = input()
	message = user + message
	transsock.sendto(message.encode('utf-8', 'ignore'), (MGRP_IP, MGRP_PRT))