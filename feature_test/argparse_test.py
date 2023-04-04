import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="specify your name")
parser.add_argument("--age", type=int, help="specify your age")

args = parser.parse_args()

print(f"Hello, {args.name}! You are {args.age} years old.")