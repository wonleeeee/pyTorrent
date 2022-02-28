import socket

class Server:

    def __init__(self) -> None:
        self.host = '127.0.0.1'
        self.port = 65432
        self.is_started = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def start(self):
        self.is_started = True
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        conn, addr = self.sock.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
