import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
# sys.path.append('../../Software/Python/')

# from grovepi import *

import socket

def Process1():
	# Change the host and port as needed. For ports, use a number in the 9000 
	# range. 
	host = '10.0.2.15'
	port = 9000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	print("Process Ultrasonic Server Started")
	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		print("Distance: " + data)
	c.close()

if __name__ == '__main__':
	Process1()


#use UDP