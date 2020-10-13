import socket
import sys


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5012 # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        #print("from connected user: " + str(data))
        elif (data.lower().strip() == 'no'):
            data="You are Minor."
            conn.send(data.encode())
        else:
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
  
"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 
  
                # if the link is broken, we remove the client 
                remove(clients) 
  
"""The following function simply removes the object 
from the list that was created at the beginning of  
the program"""
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
try:  
    while True:
       conn, addr = server.accept()
       list_of_clients.append(conn)
       print(addr[0] + " connected")
       start_new_thread(clientthread,(conn,addr))
       conn.close()
       server.close()   

except NameError as e:
    print("Client is a minor") 


