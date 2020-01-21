import os
#import ping
import threading        #from threading import Thread
import socket
import resource
print('Enter your ip address as 192.169.11 if you want to search 192.168.11.2/24')
ip=input('Host Subnet ')
F=open("done.txt","w")
def hosts(host):
		os.system('ping '+ ipadd+' -c 1 |grep "64 bytes"| cut -d" " -f4 | cut -d ":" -f1 >> done.txt');
for i in range(0,256):
	ipadd=ip + '.' + str(i)
	t = threading.Thread(target=hosts, args=(ipadd,))
	#Threads.append(t)
	t.start()
F.close()

resource.setrlimit(resource.RLIMIT_NOFILE,(65536, 65536))

f=open("done.txt","r")
hosts=[]
for l in f:
	hosts.append(l)
f.close()
for x in range(len(hosts)):
	print('\n')
	print((hosts[x]))
	host=str(hosts[x])
	from_port = 1
	to_port = 10000   
	counting_open = []
	counting_close = []
	threads = []
	def scan(port):
		s = socket.socket()
		result = s.connect_ex((host,port))
		if result == 0:
			counting_open.append(port)
			s.close()
		else:
			counting_close.append(port)
			s.close()
	for i in range(from_port, to_port+1):
		t = threading.Thread(target=scan, args=(i,))
		t.start()
	print('\n')
	[x.join() for x in threads]
	for url in range(0,len(counting_open)):
		print('Port %d is open'%counting_open[url])
	
