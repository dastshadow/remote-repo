import tkinter as tk
import os
from tkinter import filedialog
import shutil
root = tk.Tk()
root.withdraw()
#下面这段打开Windows文件选择框
real_file_path=filedialog.askopenfilename()
print("你选择的文件路径是",real_file_path)
#这个是提取出了文件的绝对路径，然后最后的.txt等等的后缀传给了ext
file_path_no_suffix,ext=os.path.splitext(real_file_path)
print(file_path_no_suffix)
print(ext)
#同一个文件不允许相同的文件名，每次手工填避免忘记
new_name=input("输入你要修改的名字")
#这是完整文件名
real_new_name=new_name+ext
#这是提取了该文件的文件夹地址
folder_path=os.path.dirname(real_file_path)
print(folder_path)
#这是把文件夹的地址和新文件名拼接起来
real_new_name_path=os.path.join(folder_path,real_new_name)
#这是将传入的文件复制了一份，然后改了个名称
change_name=shutil.copyfile(real_file_path,real_new_name_path)
print(change_name)
if __name__ == '__main__':
    pass