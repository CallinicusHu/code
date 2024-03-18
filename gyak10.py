import socket
import time
import urllib.request, urllib.parse, urllib.error

"""
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    data = mysock.recv(1000)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
"""


HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(500)
    if len(data) < 1: break
    #time.sleep(0.25)
    count = count +len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()



"""fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read()
print(type(fhand))
#for line in fhand:
#    print(line.decode(), end="")
print("corgi")
print("corgi")
"""

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
print(type(img))
fhand.write(img)
fhand.close()