import socket
import threading 
import queue 
import sys 


# Global Constants 
SERVER_IP = 1
SERVER_PORT = 2

IP = 0
PORT = 1 


class Worker(threading.Thread):
	def __init__(self, c_socket, ip, port):
		threading.Thread.__init__(self)
		self.c_socket = c_socket
		self.ip = ip
		self.port = port
		

	def run(self):
		while True:
			print('[!] {} has connected on port {}!'.format(self.ip, self.port))
			while True:
				data = self.c_socket.recv(1024)
				if data:
					print('[{}:{}] Echoing back: {}'.format(self.ip, self.port, data))
					self.c_socket.sendall(data)
				else:
					break
			print('[!] {} connected on port {} is terminating!'.format(self.ip, self.port))
			return 

def start_echo_server(server_ip, server_port):
	'''
	Starts the echo server.
	'''
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (server_ip, server_port)
	server_socket.bind(server_address)
	print('[*] Starting Echo Server...')
	print('[*] Waiting for an incoming connection...\n')
	while True:
		server_socket.listen()
		connection, client_addr = server_socket.accept()
		new_thread = Worker(connection, client_addr[IP], client_addr[PORT])
		new_thread.start()
	server_socket.close()


def main():
	'''
	Main function.
	'''
	if len(sys.argv) != 3:
		print('Usage: multithreaded-server.py [server_ip] [server_port]') 
	else:
		start_echo_server(str(sys.argv[SERVER_IP]), int(sys.argv[SERVER_PORT]))
	exit(-1)


if __name__ == '__main__':
	main()