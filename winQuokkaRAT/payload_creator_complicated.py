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
            return False
def isfile_indir(filename):
    if(os.path.isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)),filename))):
        return True
    else:
        return False

print(VERSION)
print_sharp(LINE_LENGTH)
print("hello, its WinQuokkaRAT payload_creator")
print("creating winQuokkaRAT payload exe...")

dependancy_dict= {"pyinstaller":"pyinstaller --version"}
check_dependancy(dependancy_dict)

print_sharp(LINE_LENGTH)
print("create payload...")

file_found=False
src_input = ""
while(True):
    while(not file_found): #if there is no file
        src_input = input(f"input src file's name ('0' to set default) : {SRC_NAME_DEFAULT}) : ")
        src_input = src_input.replace(" ","")
        if(src_input==""):
            print("input is empty... re-input")
            continue
        if(src_input=="0"):
            print(f"you select default... default src : {SRC_NAME_DEFAULT}")
            src_input=SRC_NAME_DEFAULT
        if(isfile_indir):
            print(f"file found!! : {src_input}")
            break


    while(True):
        try:
            port_input = int(input("input target host port ('0' to set default, free port alloc) : "))
            print(f"input:{port_input}")
        except ValueError:
            print("Invalid input. Please enter an integer for port number.")
            continue

        if (port_input==0):
            print("you select default...free port alloc")
            port_input=port_scan(9000,10000)
            if(not port_input):
                print("no port available...")
                os.system('pause')
            break
        else:
            print(f"your port : {port_input}")
            break
    print("check your input...")
    print(f"port : {port_input} ip : ip_input")
    confirm_input=input("(re-input : 'r' confirm : 'c' :")
    if(confirm_input=='r'):
        print("you choose re-input...")
        print_sharp(LINE_LENGTH)
        continue
    elif(confirm_input=='c'):
        break

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