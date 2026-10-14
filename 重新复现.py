import tkinter as tk
import os
from tkinter import filedialog
import shutil
root = tk.Tk()
root.withdraw()
#下面这段打开Windows文件选择框
real_file_path=filedialog.askopenfilename()
print("你选择的文件路径是",real_file_path)
file_path_no_suffix,ext=os.path.splitext(real_file_path)
print(file_path_no_suffix)
new_name=f"我去牛逼啊{ext}"
folder_path=os.path.dirname(real_file_path)
print(folder_path)
change_name=shutil.copyfile(real_file_path,f"C:/Users/wuweiqiu/Documents/测试文件/{new_name}")
print(change_name)
if __name__ == '__main__':
    pass