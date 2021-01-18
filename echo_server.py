# Code skeleton from official Python socket library documentation at https://docs.python.org/3/library/socket.html
# Echo server program
import socket

HOST = "" # Symbolic name meaning all available interfaces
PORT = 8001 # Chose this port as it is the one used in the lab questions.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data: break

            # Print anything that is sent to our server program.
            print(data)
            conn.sendall(data)