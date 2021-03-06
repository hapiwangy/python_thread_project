import socket, threading, pickle
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNTECT!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(name, msg):
    msg = (name, msg)
    message = pickle.dumps(msg)
    client.send(message)
    '''
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode()
    # 把長度拉長到64
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    '''
if __name__ == "__main__":
    name = input("輸入您的名稱:")
    while True:
        send_msg = input("輸入想傳送的msg:")
        send(name, send_msg)
        if send_msg == 'exit':
            break
    send(name, DISCONNECT_MSG)