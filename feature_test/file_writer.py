import os

filedir = os.path.dirname(os.path.abspath(__file__))

print(filedir)
with open('new_file.py', 'w') as f:
    # 코드 작성
    f.write('print("Hello, World!")')