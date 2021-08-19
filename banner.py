#Banner Grab

import sys
socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("<en_IP>, 80))
s.send(("GET / HTTP/1.1\r\n\r\n").encode())
           
#convert response to bytes
response = b""
while True:
           data = s.recv(4096)
           response += data
           if not data:
              break
s.close()
