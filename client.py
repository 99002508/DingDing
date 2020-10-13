import socket
import os
import time

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5013  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("Are you 18 year above");
   

    message = input(" -> ")  # take input

    while message.lower().strip() != 'no':
        client_socket.send(message.encode())  # send message
        print("--------we are with 3 packages--------");
        print("MIN----MAX----PRO");
        print("select package");
        message = input(" -> ")  # again take input #sending package from client to server
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal        
        #data = client_socket.recv(1024).decode()
        #print(' ' + data)  #recieving amount of particular package
        print("press 'ok' to buy the package");
        response=input(" -> ")
        client_socket.send(response.encode()) #sending ok from client to server 
        bill= client_socket.recv(1024).decode()
        print(bill); #recieving bill
        
        '''if(inv=client_socket.recv(1024).decode()):
        	print("Choose correct package
        print(inv);'''
        print("opening chat window for your fav");
        time.sleep(1);
        os.system('clear')
        print("-----connected-----Start DingDing-------");
       #if (response==min)
        for i in range(10):
        	chat=input(" -> ")
        	client_socket.send(chat.encode())
        	chat_rec=client_socket.recv(1024).decode()
        	print(chat_rec) 
        time.sleep(5);
        
        #message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
