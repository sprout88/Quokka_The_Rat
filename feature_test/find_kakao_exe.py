import shutil
import os

current_file_path = os.path.realpath(__file__)
copy_file_path = ""

def kakao_exe_finder():
    start_dir = "C:\\"
    kakao_path = None
    for dirpath, dirnames, filenames in os.walk(start_dir):
        if "kakao.exe" in filenames:
            kakao_path = os.path.join(dirpath,"kakao.exe")
        break
    if kakao_path is not None:
        return kakao_path
    else:
        return 1

#shutil.copyfile(current_file_path,copy_file_path)

print("hello dup!!!!")
print(kakao_exe_finder())


os.system("pause")