import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	host = socket.gethostbyname('0.0.0.0')
	port = 1234 # change the port
	s.bind((host,port))
	s.listen()
	c, addr = s.accept()
	def write_log(logs):
		with open('log','a') as file:
			file.write(logs)
	while True:
		data = c.recv(1024)
		if data:
			write_log(data.decode('ascii'))
