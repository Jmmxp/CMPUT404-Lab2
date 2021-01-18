# Code skeleton from official Python socket library documentation at https://docs.python.org/3/library/socket.html
import socket

HOST = "www.google.com" # The remote host
PORT = 80 # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((HOST, PORT))

    PROXY_HOST = "" # Symbolic name meaning all available interfaces
    PROXY_PORT = 8001 # Chose this port as it is the one used in the lab questions.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy:
        proxy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy.bind((PROXY_HOST, PROXY_PORT))
        proxy.listen(1)
        conn, addr = proxy.accept()
        with conn:
            print("Incoming connection from", addr)
            while True:
                # Get data from the client
                client_data = conn.recv(1024)
                if not client_data: break

                # Forward that data to the server
                server.sendall(client_data)

                # Take the servers's response and return it back to the client
                server_data = server.recv(1024)
                if not server_data: break

                conn.sendall(server_data)