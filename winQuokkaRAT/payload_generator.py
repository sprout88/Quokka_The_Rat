import os
import argparse

### argparser
parser = argparse.ArgumentParser()
parser.add_argument("--port","-p",dest="host_port",help="host's port number",type=int,)
parser.add_argument("--ipaddr","-i",dest="host_ipaddr",help="host's ip address string")
args = parser.parse_args()
if(args.host_port==None):
    print("no host port input error...")
else:
    #print(f"{args.host_port}")
    pass
if(args.host_ipaddr==None):
    print("no host port input error...")
else:
    #print(f"{args.host_port}")
    pass

print(f"target host's ip : {args.host_ipaddr}")
print(f"target host's port : {args.host_port}")

python_code = '''

'''

filedir = os.path.dirname(os.path.abspath(__file__))
print(filedir)
with open('new_file.py', 'w') as f:
    # 코드 작성
    f.write(f"{python_code}")

