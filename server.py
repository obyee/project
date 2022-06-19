import socket
import threading
# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client,i):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024).decode()
            if message=="CLOSE123123":
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast('{} left!'.format(nickname).encode())
                nicknames.remove(nickname)
                print('{} left!'.format(nickname))
                break

            broadcast(message.encode())
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode())
            nicknames.remove(nickname)
            print('{} left!'.format(nickname))
            break

# Receiving / Listening Function

while True:
    # Accept Connection
    client, address = server.accept()
    print("Connected with {}".format(str(address)))

    # Request And Store Nickname
    nickname = client.recv(1024).decode()
    nicknames.append(nickname)
    clients.append(client)

    # Print And Broadcast Nickname
    print("Nickname is {}".format(nickname))
    broadcast("{} joined!".format(nickname).encode())
    client.send('Connected to server!'.encode())

    # Start Handling Thread For Client
    thread = threading.Thread(target=handle, args=(client,address))
    thread.start()

