import socket
import sys

sock = socket.socket()
sock.connect(('192.168.1.22', 43000))
# sock.send("hello".encode())
# data = sock.recv(1024)

while True:
    message = input('Enter some laters :').encode()
    try :
        sock.sendall(message)
        print (sock.recv(1024))
    except socket.error:
        print ('Send failed')
        sys.exit()

