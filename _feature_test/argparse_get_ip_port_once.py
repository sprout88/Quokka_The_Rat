import os
import argparse

### argparser
parser = argparse.ArgumentParser()

parser.add_argument("ip",help="ex) 127.0.0.1")
parser.add_argument("port",help="ex) 8080")
args = parser.parse_args()

print(args)
print(args.ip)
print(args.port)
