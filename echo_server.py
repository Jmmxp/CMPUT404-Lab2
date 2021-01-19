# Code skeleton from official Python socket library documentation at https://docs.python.org/3/library/socket.html
# Echo server program
import socket
from multiprocessing import Process

def handle_client(conn, addr):
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data: break

            # Print/echo anything that is sent to our server program.
            print(data)
            conn.sendall(data)

HOST = "" # Symbolic name meaning all available interfaces
PORT = 8001 # Chose this port as it is the one used in the lab questions.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    # Listen for any incoming client connections until the server is forcefully shut-down.
    while True:
        conn, addr = s.accept()
        p = Process(target=handle_client, args=(conn, addr,))
        p.daemon = True
        p.start()
    conn.close()