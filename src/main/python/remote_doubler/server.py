import socket;

host = socket.gethostname()
port = 5102

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

client, addr = server.accept()
msg = client.recv(1024)
print("Data from Client: " + bytes.decode(msg))
client.send(str(float(msg) * 2).encode("ASCII"))

client.close()
server.close()
