import socket
import sys
import threading
import random

localIP="127.0.0.1"
serverPort=7537
buffSize=1024
#Write your code here!
def client_handler(connection):
    client_connected = True
    client_list = []
    while client_connected:
        data = connection.recv(buffSize)
        if not data:
            client_connected = False
            break;
        msg = data.decode()
        client_list.append(int(msg))
        reply = sum(client_list)
        #print("server: " + str(reply))
        connection.sendall(str.encode(str(reply)))

    connection.close()

#def accept_connections(socket, counter_lock):

    #print("server " + counter)


def start_server():
    counter = 0
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.bind((localIP, serverPort))
    server_socket.listen()
    counter_lock = threading.Lock()
    th_list = []
    keepRunning = True
    while keepRunning:
            connection, address = server_socket.accept()
            th = threading.Thread(target=client_handler, args=(connection,))
            th_list.append(th)
            if not th_list[-1].is_alive():
                th_list[-1].start()
                counter += 1
                print ("counter :" + str(counter))
            if not counter < 25:
                keepRunning = False

    print("list: " + str(len(th_list)))
    for th in th_list:
        th.join()
    server_socket.close()
#You can utilize following client for test purposes
def client_main():
    TCPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    TCPSocket.connect((localIP, serverPort))
    rnd=random.sample(range(-30, 30), 5)
    for r in rnd:
        msg=str(r)
        print('Send:', msg)
        bytesToSend=str.encode(msg)

        TCPSocket.send(bytesToSend)

        #print('Wait message')
        data=TCPSocket.recv(buffSize)
        data=data.decode()
        data=data.splitlines()
        msg1=data[0]
        print('Received:', msg1)

    print('Close socket')
    TCPSocket.close()

    print('Got sum:'+msg1+'. Value shall be '+str(sum(rnd))+', sent data='+str(rnd))

    assert int(msg1)==sum(rnd)
    print('Test passed!')

server_th = threading.Thread(target=start_server).start()
#start_server()

#Set True to run the clients
run_client=False

if run_client:
    th_list=[]
    for i in range(20):
        th_list.append(threading.Thread(target=client_main))
        th_list[-1].start()

    for th in th_list:
        th.join()

    for i in range(5):
        th_list.append(threading.Thread(target=client_main))
        th_list[-1].start()

    for th in th_list:
        th.join()

#server_main(localIP, serverPort)
    #After 25 clients the server shall exit
