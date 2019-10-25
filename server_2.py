import socket

"""
using a header to handler sockets that exceed 
the buffer size without closing the connection
"""

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f'Connection {address} has been established!')

    msg = "Welcome to the server"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes('Welcome to the server!', 'utf-8'))
    clientsocket.close()
