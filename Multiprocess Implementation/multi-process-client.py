import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8885)
try:
	client_socket.connect(server_address)
	message = b'This is a message'
	client_socket.sendall(message)
	data = client_socket.recv(1024)
	print(data)
except ConnectionRefusedError:
	print('[!] Error connecting to the server!')
