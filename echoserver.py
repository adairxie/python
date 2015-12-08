import socketserver

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the Tcp socket connected to the client
        self.data = self.request.recv(1024).strip()
        print(" {} wrote:".format(self.client_address[0]))
        print(str(self.data))
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
    server.serve_forever()

