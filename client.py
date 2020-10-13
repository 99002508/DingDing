import socket
import os
import time
import csv
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5019  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("Are you 18+?")
    message = input(" -> ")  # take input
    if message.lower().strip() == 'no':
        print("You are Minor")
    print("let us know your Gender")
    gender = input('->')
    while message.lower().strip() != 'no':
        client_socket.send(message.encode())  # send message
        print("--------We are with 3 packages--------")
        print("1.MIN\n2.MAX\n3.PRO")
        print("Select package")
        message = input(" -> ")  # again take input #sending package from client to server
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server:' + data)  # show in terminal        
        #data = client_socket.recv(1024).decode()
        #print(' ' + data)  #recieving amount of particular package
        print("press 'ok' to buy the package");
        response = input(" -> ")
        client_socket.send(response.encode()) #sending ok from client to server 
        bill = client_socket.recv(1024).decode()
        print(bill) #recieving bill
        if gender.lower().strip() == 'male':
            with open('female.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        if gender.lower().strip() == 'female':
            with open('male.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)      
        print("opening chat window for your fav")
        time.sleep(10)
        os.system('clear')
        print("-----connected-----Start DingDing-------")
        if message == "min":
            for chat in range(3):
                chat = input(" -> ")
                client_socket.send(chat.encode())
                chat_rec = client_socket.recv(1024).decode()
                print(chat_rec)
        if message == "max":
            for chat in range(5):
                chat = input(" -> ")
                client_socket.send(chat.encode())
                chat_rec = client_socket.recv(1024).decode()
                print(chat_rec)
        if message == "pro":
            for chat in range(10):
                chat = input(" -> ")
                client_socket.send(chat.encode())
                chat_rec = client_socket.recv(1024).decode()
                print(chat_rec)
        time.sleep(5)
        return "done"
        break   
        #message = input(" -> ")  # again take input
    client_socket.close()  # close the connection
if __name__ == '__main__':
    client_program()
