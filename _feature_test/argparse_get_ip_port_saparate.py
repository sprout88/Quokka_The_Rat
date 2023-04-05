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

print(f"{args.host_port} / {args.host_ipaddr}")