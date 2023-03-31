from socket import *
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect(('127.0.0.1', 12000))
clientSocket.settimeout(1)

for x in range(9):
    message = "Testando"
    msg = message.encode()
    pingStart = time.time()
    address = clientSocket.send(msg)
    try:
        responseServer = clientSocket.recvfrom(1024)
    except timeout:
        print("Tempo limite para conexão")
        continue
    pingEnd = time.time()
    if message != '':
        print(message)
        rtt = pingEnd - pingStart
        print("Resposta do ping: ", rtt)    
clientSocket.close()
