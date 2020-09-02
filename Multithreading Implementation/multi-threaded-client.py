import socket
import sys 


# Global Constants 
SERVER_IP = 1
SERVER_PORT = 2


def connect_to_sever(server_ip, server_port):
	'''
	Connects to the echo server.
	'''
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	server_address = (server_ip, server_port)
	try:
		client_socket.connect(server_address)
		message = str(input('[*] Enter a message: '))
		while message != 'exit':
			client_socket.sendall(bytes(message, encoding='utf8'))
			data = client_socket.recv(1024)
			print('[-] Echoed back: {}'.format(data.decode("utf-8")))
			message = str(input('[-] Enter a message: '))
	except ConnectionRefusedError:
		print('[!] Error connecting to the server!')


def main():
	'''
	Main function.
	'''
	if len(sys.argv) != 3:
		print('Usage: multithreaded-client.py [server_ip] [server_port]') 
	else:
		connect_to_sever(str(sys.argv[SERVER_IP]), int(sys.argv[SERVER_PORT]))
	exit(-1)


if __name__ == '__main__':
	main()