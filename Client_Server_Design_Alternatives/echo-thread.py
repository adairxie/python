#!/usr/bin/python3

from socketserver import BaseRequestHandler, TCPServer
from socketserver import ForkingTCPServer, ThreadingTCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("got connection from", self.client_address)
        while True:
            data = self.request.recv(4096)
            print('receive', data.decode())
            if data:
                sent = self.request.send(data)
            else:
                print("disconnect", self.client_address)
                self.request.close()
                break



if __name__ == "__main__":
    listen_address = ("0.0.0.0", 9981)
    server = ThreadingTCPServer(listen_address, EchoHandler)
    server.serve_forever()
