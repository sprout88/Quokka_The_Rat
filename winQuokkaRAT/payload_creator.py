import os, subprocess

VERSION = "develop1.0 by jeho"

def print_sharp(end):
    for i in range(0,end):
        print('#',end='')
        if(i==end-1):
            print()

def check_dependancy(dependancy_list):
    for dependancy_element in dependancy_list:
        print(f"Checking if it is installed... : {dependancy_element}")
        try:
            result = subprocess.check_call(f"{dependancy_element}")

        except Exception as e:
            print(f"dependancy doesn't installed : {e}")

print(VERSION)
print_sharp(50)
print("hello, its WinQuokkaRAT payload_creator")
print("creating winQuokkaRAT payload exe...")

dependancy_list= {"pyinstaller --version"}
check_dependancy(dependancy_list)


