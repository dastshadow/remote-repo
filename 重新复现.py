import tkinter as tk
import os
from tkinter import filedialog
import shutil
import time
root = tk.Tk()
root.withdraw()
#下面这段打开Windows文件选择框
real_file_path=filedialog.askopenfilename()
print("你选择的文件路径是",real_file_path)
#这个是提取出了文件的绝对路径，然后最后的.txt等等的后缀传给了ext
file_basename=os.path.basename(real_file_path)
file_name_no_suffix,ext=os.path.splitext(file_basename)
print(file_name_no_suffix)
print(ext)
#同一个文件不允许相同的文件名，每次手工填避免忘记
new_name=input("输入你要修改的名字")
print(new_name)
#这是完整文件名(带后缀),不是地址
suffix_new_name=new_name+ext
print(suffix_new_name)
#创建一个方便管理作业的总文件夹
homework_parent_path=os.path.expanduser("~/Desktop/作业目录")
print(homework_parent_path)
#如果这个总文件夹不存在，则创建
if not os.path.exists(homework_parent_path):
    os.mkdir(homework_parent_path)
else:
    pass
#获取当前操作的年月日
time_str=time.strftime("%Y-%m-%d")
print(time_str)
#子文件夹名
homework_child_name=file_name_no_suffix+f" {time_str}"
print(homework_child_name)
homework_child_path=os.path.join(homework_parent_path,homework_child_name)
print(homework_child_path)
if not os.path.exists(homework_child_path):
    os.mkdir(homework_child_path)
else:
    pass
suffix_homework_child_path=os.path.join(homework_child_path,suffix_new_name)
print(suffix_homework_child_path)
if not os.path.exists(suffix_homework_child_path):
    shutil.copyfile(real_file_path,suffix_homework_child_path)
else:
    pass