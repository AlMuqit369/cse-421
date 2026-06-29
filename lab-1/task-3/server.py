import socket 
import threading

FORMAT='utf-8'
HEADER= 64

SERVER= socket.gethostbyname(socket.gethostname())
PORT=4949
ADDR=(SERVER,PORT)
DISCONNECT="End"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
print(f"Server is running on {SERVER}:{PORT}")

server.listen()
print(f"Server is listen on {SERVER}:{PORT}")

def handle_client(conn,addr):
    print(f"connection from {addr} has been established")
    connected= True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT:
                connected=False
                conn.send('Connection closed'.encode(FORMAT))
            else:
                print("Client Message:", msg)
                vowels = 0
                for ch in msg.lower():
                    if ch in "aeiou":
                        vowels += 1
                if vowels == 0:
                    conn.send("Not enough vowels".encode(FORMAT))
                elif vowels <= 2:
                    conn.send("Enough vowels I guess".encode(FORMAT))
                else:
                    conn.send("Too many vowels".encode(FORMAT))
    conn.close()
    
while True:
    conn,addr=server.accept()
    thread= threading.Thread(target=handle_client,args=(conn,addr))
    thread.start()