import socket
from random import randint

host = socket.gethostname()
port = 5102

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

client, addr = server.accept()



loopsDice = 1200
min = 0
max = 5
numbers = [0, 0, 0, 0, 0, 0]

for i in range(loopsDice):
    rnd = randint(min, max)
    numbers[rnd] += 1

client.send(str(numbers).encode("ASCII"))

client.close()
server.close()
