import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip_address = '127.0.0.1'
port = 4444

server_socket.bind((ip_address, port))

server_socket.listen(1)

# client_message = server_socket.accept()

# client_socket = client_message[0]
# client_address = client_message[1]

client_socket, client_address = server_socket.accept()

while True:
    command = input("Enter command: ")
    if not command:
        break
    elif command.lower().strip() == "exit":
        client_socket.send(command.encode())
        break
    client_socket.send(command.encode())
    output = client_socket.recv(4096).decode()
    print(output)

    cwd = client_socket.recv(1024).decode()
    dir_name = os.path.basename(cwd)
    print(f"Current directory: /{dir_name}")








# client_message = client_socket.recv(1024)
# print(client_message.decode())

# client_socket.send(b"Hello from server")
