import sys
import socket
import select


def start_client():
    # Connect to local host
    address = ('localhost', 1234)
    connection = socket.socket()
    connection.connect(address)
    print('connected!')


def start_server():
    print('Starting server ...')


if __name__ == '__main__':
    if sys.argv[1].lower() == 'client':
        start_client()
    else:
        start_server()
