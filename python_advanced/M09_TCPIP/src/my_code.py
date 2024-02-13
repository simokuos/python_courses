import socket
import sys
import threading
import random
import time

localIP="127.0.0.1"
serverPort=7538
buffSize=1024


#Write your code here!
def client_handler(connection):
    client_connected = True
    while client_connected:
        data = connection.recv(buffSize)
        if not data:
            client_connected = False
            break
        msg = data.decode()
        client_number = int(msg)
        reply = random.randint(0, client_numbe - 1)
        #print("server: " + str(reply))
        connection.sendall(str.encode(str(reply)))

    connection.close()   

def server_main():
    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPSocket.bind((localIP, buffSize))
    
    while True:
        #conn, addr = UDPSocket.accept()
        th = threading.Thread(target=client_handler, args=(UDPSocket,))
        if not th.is_alive():
            th.start() 


#You can utilize following client for test purposes
def client_main():
    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    #No bindig => Pick random port

    for i in range(10):
        msg=str(4+3*i)
        bytesToSend=str.encode(msg)
        serverAddressPort=(localIP, serverPort)
        UDPSocket.sendto(bytesToSend, serverAddressPort)
        bytesAddressPair=UDPSocket.recvfrom(buffSize)
        message=bytesAddressPair[0]

        print(msg+' :',message.decode())
        #time.sleep(1.0)

    UDPSocket.close()


server_th = threading.Thread(target=server_main).start()
#Set True to run the clients
run_client=False

if run_client:
    th_list=[]
    for i in range(10):
        th_list.append(threading.Thread(target=client_main))
        th_list[-1].start()

    for th in th_list:
        th.join()

