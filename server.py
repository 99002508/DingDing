import socket
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5019# initiate port no above 1024
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
        print("from connected user: " + str(data))
        data = conn.recv(1024).decode() # Recieveing min/max/pro
        print(" " + str(data))
        package = str(data)
        if package.lower().strip() == 'min':
            rate_min = "you have to pay 100 rs per month"
            conn.send(rate_min.encode())
            ok_rec = conn.recv(1024).decode() #recieving 'ok' from client for min package")
            print(str(ok_rec))
            bill = "---------BILL-------->"\
            "received 100 rs "\
            "happy DingDing."
            conn.send(bill.encode())
        if package.lower().strip() == 'max':
            rate_min = "you have to pay 200 rs per month"
            conn.send(rate_min.encode())
            ok_rec = conn.recv(1024).decode() #recieving 'ok' from client for min package
            print(str(ok_rec))
            bill = "---------BILL-------->"\
            "received 200 rs "\
            "happy DingDing."
            conn.send(bill.encode())
        if package.lower().strip() == 'pro':
            rate_min = "you have to pay 300 rs per month"
            conn.send(rate_min.encode())
            ok_rec = conn.recv(1024).decode() #recieving 'ok' from client for min package
            print(str(ok_rec))
            bill = "---------BILL-------->"\
            "received 300 rs "\
            "happy DingDing."
            conn.send(bill.encode())    	
        if package == "min":     
            for i in range(3):
                chat_rec = conn.recv(1024).decode()
                print(chat_rec)
                chat = input(" -> ")
                conn.send(chat.encode())
        if package == "max":     
            for i in range(5):
                chat_rec = conn.recv(1024).decode()
                print(chat_rec)
                chat = input(" -> ")
                conn.send(chat.encode())
        if package == "pro":     
            for i in range(10):
                chat_rec = conn.recv(1024).decode()
                print(chat_rec)
                chat = input(" -> ")
                conn.send(chat.encode())
        return "done"   	 
        #data = input(' -> ')
       # conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection
if __name__ == '__main__':
    server_program() 
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients != connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 
  
                # if the link is broken, we remove the client 
                remove(clients)  
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection)
try:
    while True:
        conn, addr = server.accept()
        list_of_clients.append(conn)
        print(addr[0] + " connected")
        start_new_thread(clientthread, (conn, addr))
        conn.close()
        server.close()      
except NameError as eta:
	print("Client is minor")     
