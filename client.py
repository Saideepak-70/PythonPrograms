import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect((socket.gethostname(), 1234))

msg = input("You :- ")
while msg.lower().strip() != "end":
    serv.send(msg.encode())
    data = serv.recv(1024).decode()
    print("Server :- " + data)
    msg = input("You :- ")

serv.close()
message = serv.recv(1024)
print(msg.decode("utf-8"))
