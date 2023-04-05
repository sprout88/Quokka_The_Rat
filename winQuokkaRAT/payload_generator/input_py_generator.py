import os
import argparse

DEBUG = False
UAC_BYPASS = True
SRC_FILE = "winQuokka_payload_input_test.py"
### argparser
parser = argparse.ArgumentParser()

parser.add_argument("--ip","-i",dest='ip',help="ex) 127.0.0.1",default="127.0.0.1")
parser.add_argument("--port","-p",dest='port',help="ex) 8080",default="9001")
args = parser.parse_args()


print(f"target host's ip : {args.ip}")
print(f"target host's port : {args.port}")


filedir = os.path.dirname(os.path.abspath(__file__))
file_contents=""
print(filedir)
try:
    with open(f'{filedir}/{SRC_FILE}', 'r',encoding="utf-8") as f:    
        file_contents = f.read()
except Exception as e:
    print(f"Reading Error : {e}")

#print(file_contents)


file_contents=file_contents.replace("127.0.0.1",args.ip)
file_contents=file_contents.replace("9001",args.port)
                                      

host_ipaddr_dotReplaced = (args.ip).replace(".","-")

print(filedir)
with open(f'{filedir}/gen_payload_{host_ipaddr_dotReplaced}_{args.port}.py', 'w',encoding="utf-8") as f:
    # 코드 작성
    f.write(f"{file_contents}")

print("payload generated...")

os.system("pause")