import socket
import threading
# Choosing Nickname
nickname = input("Choose your nickname: ")
print("WHEN YOU WANT TO CLOSE ENTER CLOSE123123")
# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
client.send(nickname.encode())
msg=client.recv(1024).decode()
print(msg)
# Listening to Server
def receive():
    while True:
        try:
           #msg_to_send=input()
            #client.send(msg_to_send.encode())
            msg=client.recv(1024).decode()
            print(msg)
        except:
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        s=input('')
        if s=="CLOSE123123":
            client.close()
            break
        message = '{}: {}'.format(nickname, s)
        try:
            client.send(message.encode())
        except:
            client.close()
            break
# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()