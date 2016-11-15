import socket

host = socket.gethostname()
port = 5102

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

msg = client.recv(1024)

client.close()

print("Der Server sendete: " + bytes.decode(msg))
