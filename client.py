# Code skeleton from official Python socket library documentation at https://docs.python.org/3/library/socket.html
# Echo client program
import socket

HOST = "www.google.com" # The remote host
PORT = 80 # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # GET request code from StackOverflow user mhawke 
    # https://stackoverflow.com/users/21945/mhawke
    # https://stackoverflow.com/a/34192144
    s.sendall(bytearray("GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".format(host=HOST), "utf-8"))
    data = s.recv(1024)
print("Received", repr(data))