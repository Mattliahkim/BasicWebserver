#import socket module
from socket import *
import threading
import sys

#Prepare a sever socket
#Fill in start
serverPort = 12000

def client_handler(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode(encoding="ASCII")
        print("NEW CONNECTION FROM CLIENT AT:", addr[0], addr[1])
        print("HANDLED ON:", threading.currentThread())
        print("FROM CLIENT:", message)
        filename = message.split()[1]
        #print(filename)
        f = open(filename[1:])
        outputdata = []
        for line in f:
            outputdata.append(line)
        html_response = "HTTP/1.1 200 OK\r\n"
        
        #blah = message.split('\r\n')
        #for i in range(1,len(blah)): #for copying original message
          #  html_response += blah[i]+'\r\n'
        

        #Fill in end

        #Send the content of the requested file to the client
        blahString = ""
        for i in range(0, len(outputdata)):
            blahString+=outputdata[i]

        html_response += "Content-Length: "+str(len(blahString))+"\r\n\r\n"
        print(html_response)
        connectionSocket.send(html_response.encode(encoding="ASCII"))
        
        connectionSocket.send(blahString.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        error = "HTTP/1.1 404 Not Found\r\nContent-Length: 59\r\n\r\n"
        print(error)  
        connectionSocket.send(error.encode(encoding="ASCII"))
        errorPage ="<html><body><h1>Error 404 File Not Found</h1></body></html>"
        connectionSocket.send(errorPage.encode(encoding="ASCII"))

        connectionSocket.close()

def run_server(serverPort):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    #Fill in end
    threads = []
    loop = True
    while loop:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            t = threading.Thread(target = client_handler, args = (connectionSocket, addr))
            threads.append(t)
            #print(threads)
            t.start()
        except KeyboardInterrupt:
            loop = False  
            serverSocket.close()
    print("Server is closing...")
    #Terminate the program after sending the corresponding data

if __name__ == "__main__":
    serverPort = int(sys.argv[1]) if len(sys.argv) > 1 else serverPort
    run_server(serverPort)