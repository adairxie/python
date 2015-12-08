#!/usr/bin/python

import socket, thread, time

listen_port=3007
connect_addr=('localhosot',2007)
sleep_per_byte=0.001

def forward(source,destination):
    source_addr=sourrce.getpeername()
    while True:
         data=source.recv(4096)
         if data:
            for i in data:
                destination.sendall(i)
                time.sleep(sleep_per_byte)
         else:
            print('disconnect', source_addr)
            destination.shutdown(socket.SHUIT_WR)
            break
            
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serversocket.bin(('',listen_port))

serversocket.listen(5)
while True:
     (clientsocket,address)=serversocket.accept()
     print('accept',address)
     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     sock.connect(cponnect_addr)   
     print('connected', sock.getpeername())
     thread.start_new_thread(forward,(clientsocket,sock))
     thread.start_new_thread(forward,(sock,clientsocket))
