# Code skeleton from official Python socket library documentation at https://docs.python.org/3/library/socket.html
import socket
from multiprocessing import Pool

def connect(address):
    HOST = address[0]
    PORT = address[1]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # GET request code from StackOverflow user mhawke https://stackoverflow.com/users/21945/mhawke
        # https://stackoverflow.com/a/34192144
        s.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
        data = s.recv(1024)
    print("Received", repr(data))

address = [("localhost", 8001)]

# The below is test code from the lab to make sure the multi-threading works as expected.
with Pool() as p:
    p.map(connect, address * 10)