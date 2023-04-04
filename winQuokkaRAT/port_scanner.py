import os, subprocess, socket

LINE_LENGTH = 50
PREFIX_PORT_START = 9000
PREFIX_PORT_END = 10000

def print_sharp(end):
    for i in range(0,end):
        print('-',end='')
        if(i==end-1):
            print()

def is_port_available(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind to create socket
        try:
            s.bind(("0.0.0.0", port))
        except OSError:
            # return False if port in use.
            return False
        else:
            # return True if port is Available.
            return True
def ret_first_free_port(start,end):
    for port in range(start,end+1):
        if(is_port_available(port)):
            return port
        else:
            return False

def print_all_free_port(start,end):
    for port in range(start,end+1):
        if(is_port_available(port)):
            print(f"{port} ",end='')
        else:
            pass
        
def print_all_port(start,end):
    for port in range(start,end+1):
        if(is_port_available(port)):
            print("port : {port} status : FREE")
        else:
            print("port : {port} status : BINDED")

print_sharp(LINE_LENGTH)
print_sharp(LINE_LENGTH)
print("PORT SCANNER")
print_sharp(LINE_LENGTH)


while(True):
    print("select jobs...")
    print(f"1. available port random({PREFIX_PORT_START}~{PREFIX_PORT_END}) return")
    print("2. print all free port by range")
    print("3. print all free/binded port by range")

    user_input = input(":")
    if(user_input=="1"):
        print("you choose 1...")
        print(f"first free port in range({PREFIX_PORT_START}~{PREFIX_PORT_END}")
        print(f"free port : {ret_first_free_port(PREFIX_PORT_START,PREFIX_PORT_END)}")
        os.system('pause')
    if(user_input=="2"):
        print("you choose 2...")
        try:
            start_input = int(input("input start port num :"))
            end_input = int(input("input end port num :"))
            print_all_free_port(start_input,end_input)
        except Exception as e:
            print("wrong integer...")
        os.system('pause')
    if(user_input=="3"):
        print("you choose 3...")
        try:
            start_input = int(input("input start port num :"))
            end_input = int(input("input end port num :"))
            print_all_port(start_input,end_input)
        except Exception as e:
            print("wrong integer...")
        
        