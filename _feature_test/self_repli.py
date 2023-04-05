import shutil
import os

FILE_NAME = "self_repli"

current_file_path = os.path.realpath(__file__)

copy_file_path = current_file_path+".copy"

shutil.copyfile(current_file_path,copy_file_path)

print("hello repli!!")