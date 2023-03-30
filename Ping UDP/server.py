import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
port = 12000
serverSocket.bind(('127.0.0.1',port ))
print("Server respondendo a porta ", port)

while True:
  
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    print("Mensagem:", message.decode())
    print("Endereço:", address)
    print('---------------------')
    
    if rand < 4:
        continue
    serverSocket.sendto(message, address)
    