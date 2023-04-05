import os

# filedir = os.path.dirname(os.path.abspath(__file__))

# print(filedir)

# savedir = os.path.join(filedir,"asdf")
# with open(savedir, 'wb') as f:
#     # 코드 작성
#     f.write(b'print("Hello, World!")')

##pemission denied
script_path = os.path.dirname(os.path.abspath(__file__))
saved_file_path = os.path.join(os.getcwd(),"debugtestfile")
file_content=b'asdfjlasdf'

print(saved_file_path)
with open(saved_file_path,'wb') as f:
    f.write(file_content)
