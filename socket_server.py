import socket
import threading
import time
from tkinter.tix import DisplayStyle
from xml.etree.ElementTree import TreeBuilder
FORMAT = "utf-8"
HEADER = 64
# choose a port that is unused
PORT = 5050
# chosse ipv4(localIP)
# SERVER = "140.115.214.73"
# get ipv4 automatic
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
DISCONNECT_MSG = "DISCONNTECT!"
# 第一個參數代表用哪種方式連接(這裡選的是網路，也有藍芽等等其他選項)
# 第二參數代表我們要用stream來傳遞資料
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 把server和ADDR綁在一起
server.bind(ADDR)
# 此函數負責個別的連接
def handle_client(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected")
    connected = True
    while connected:
        # blocking line of code:代表會等到有新的訊息近來才會繼續執行
        # 先接收一次訊息(此為訊息長度)，第二次接收訊息才是訊息本身
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("MSG received".encode(FORMAT))
    conn.close()


# 此函數負責所有新的client連接
def start():
    server.listen()
    
    while True:
        # wait until the server connection
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTING] {threading.activeCount() - 1}")
print("[start] server is starting")
start()