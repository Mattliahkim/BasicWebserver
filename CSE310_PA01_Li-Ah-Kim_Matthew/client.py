from socket import *
import sys

serverPort = 12000
serverName = 'localhost'
urlName = "/HelloWorld.html"

def run_client(serverName, serverPort, address):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    message = "GET "+address+" HTTP/1.1\r\n"+"Host: 10.0.0.135:12000\r\n"+"Connection: keep-alive\r\n"
    #print(message)
    #x = input("Enter name:")
    #print(x)
    #message += 
    #print(message)
    #bytes_sent = 
    clientSocket.send(message.encode())
    httpResponse = clientSocket.recv(1024)
    print("The response is: ",httpResponse.decode())
    #print("AT:", clientSocket.getpeername())
    clientSocket.close()
if __name__ == "__main__":
    sn = sys.argv[1] if len(sys.argv) > 1 else serverName
    sp = int(sys.argv[2]) if len(sys.argv) > 2 else serverPort
    name = sys.argv[3] if len(sys.argv) > 3 else urlName
    run_client(sn, sp, name)

