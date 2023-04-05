import os

filedir = os.path.dirname(os.path.abspath(__file__))

print(filedir)
with open(f'{filedir}/test.txt', 'r',encoding="utf-8") as f:
    file_contents = f.read()

print(file_contents)