import socket
import time

IP = "127.0.0.1"
PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
meaning_word = "null"

while True:
	msg = raw_input("enter the word :")
	sock.sendto(msg,(IP,PORT))
	time.sleep(2)
	if(meaning_word == "null"):
		print "fuck"
	meaning = sock.recvfrom(1024)
	meaning_word=meaning[0]
	meaning_addr=meaning[1]
	print "server reply :" + meaning_word
