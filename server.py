import socket
# part of standard library

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
creating a socket object:

AF_INET: corresponds to ipv4
SOCK_STREAM: corresponds to tcp
"""
s.bind((socket.gethostname(), 1234))
"""
gethostname() is the equivalent of localhost
"""
s.listen(5)

while True:
    clientsocket, address = s.accept()
    """
    allow incoming connections and store them into clientsocket object 
    """
    print(f'Connection from {address} has been established')
    clientsocket.send(bytes("Welcome", "utf-8"))  # sending information to the client socket
