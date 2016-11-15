import socket

host = socket.gethostname()
port = 5102

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

number = float(input("Bitte geben Sie eine Zahl ein: "))
number = str(number)
msg = number.encode("ASCII")

client.send(msg)
msg = client.recv(1024)

client.close()

print("Der Server sendete: " + bytes.decode(msg))
