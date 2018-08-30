# asyncore

import asyncore, asynchat
from socket import *
from collections import deque

class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(AF_INET, SOCK_STREAM)
        self.bind(('', port))
        self.listen(4096)

    def handle_accept(self):
        socket, address = self.accept()
        print ("Connection from", address)
        EchoHandler(socket)
        

class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(100000)    
        if data:
            self.send (b'Got:' + data)
    
    def handle_close (self):
        self.close ()
        print ('Connection closed')
        

if __name__ == "__main__":        
    s = Server('', 25000)
    asyncore.loop()
        
        

