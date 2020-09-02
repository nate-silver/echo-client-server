import socket 
import multiprocessing


# Global Constants 
CLIENT_ADDR = 0
CONNECTED_PORT = 1 


def handle_incoming_connection(client_connection):
	'''
	Handles the incoming client connection.
	'''
	connection, client_addr = client_connection
	print('[!] {} has connected on port {}!'.format(client_addr[CLIENT_ADDR], client_addr[CONNECTED_PORT]))
	while True:
		data = connection.recv(1024)
		if data:
			print(multiprocessing.current_process())
			print('Echoing back: {}\n'.format(str(data)))
			connection.sendall(data)
		else:
			break


def start_echo_server():
	'''
	Starts the echo server.
	'''
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 8885)
	server_socket.bind(server_address)
	server_socket.listen()
	print('[*] Starting Echo Server...\n')
	while True:
		print('[*] Waiting for an incoming connection...')
		p = multiprocessing.Process(target=handle_incoming_connection, args=(server_socket.accept(), ))
		p.start()
		p.join()
	server_socket.close()


def main():
	'''
	Main function.
	'''
	start_echo_server()
	exit(-1)


if __name__ == '__main__':
	main()