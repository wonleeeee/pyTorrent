import socket
from server import Server
# HOST = '127.0.0.1'
# PORT = 65432

class Client:

    def __init__(self) -> None:
        self.host = '127.0.0.1'
        self.port = 8001
        self.is_started = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.is_started = True
        self.sock.connect((self.host, self.port))
        self.sock.sendall(b'Hello, world')
        data = self.sock.recv(1024)

    # print('Received', str(data))

class Peer:
    def __init__(self) -> None:
        self.server = None # Server()
        self.client = None # Client()
        self.is_server = False
        self.is_client = False

    def 
    
    def start_server(self) -> None:
        self.is_server = True
        self.server = Server()
        self.server.start()

    def start_client(self) -> None:
        self.is_client = True
        self.client = Client()
        self.client.start()

ser = Peer()
ser.start_server()
cli = Peer()
cli.start_client()