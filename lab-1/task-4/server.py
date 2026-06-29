import socket

FORMAT = 'utf-8'
HEADER = 64

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4949
ADDR = (SERVER, PORT)
DISCONNECT = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print(f"Server is running on {SERVER}:{PORT}")

server.listen()
print("Waiting for connection...")

while True:

    conn, addr = server.accept()

    print(f"Connection established from {addr}")

    connected = True

    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT:

                connected = False
                conn.send("Connection Closed".encode(FORMAT))

            else:

                hours = int(msg)

                if hours <= 40:
                    salary = hours * 200

                else:
                    salary = 8000 + (hours - 40) * 300

                conn.send(f"Salary = Tk {salary}".encode(FORMAT))

    conn.close()