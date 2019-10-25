import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:

    full_message = ''
    new_msg = True
    while True:
        message = s.recv(10)
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
        full_message += message.decode("utf-8")

    print(full_message)