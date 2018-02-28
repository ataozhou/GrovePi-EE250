import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

from grovepi import *


import socket

led = 3

pinMode(led,"OUTPUT")

def Main():
	host = '192.168.1.144'
	port = 8000

	s = socket.socket()
	s.bind((host,port))

	s.listen(1)
	c, addr = s.accept()
	while True:
		data = c.recv(1024).decode('utf-8')
		print(data)
		if str(data) == "LED_ON":
			digitalWrite(led,1)
			print("fucking turn on")
		elif str(data) == "LED_OFF":
			digitalWrite(led,0)
	c.close()

if __name__ == '__main__':
	Main()

# use TCP
