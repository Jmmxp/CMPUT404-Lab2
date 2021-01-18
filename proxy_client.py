# Code skeleton from official Python socket library documentation at https://docs.python.org/3/library/socket.html
import socket

HOST = "localhost" # The remote host
PORT = 8001 # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # GET request code from StackOverflow user mhawke https://stackoverflow.com/users/21945/mhawke
    # https://stackoverflow.com/a/34192144
    s.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
    data = s.recv(1024)
print("Received", repr(data))