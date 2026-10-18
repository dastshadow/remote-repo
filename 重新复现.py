import os
import shutil
import time
import sys
#前期工作
homework_parent_path=os.path.expanduser("~/Desktop/作业目录")
if not os.path.exists(homework_parent_path):
    os.mkdir(homework_parent_path)

#"""前提：双击或者后面想改名"""
config_path=os.path.join(homework_parent_path,"config.txt")
invalid_chars=r'<>:"/\|?*'
if len(sys.argv)<2:
    new_name=input("输入你要修改的名字")
    for char in invalid_chars:
        new_name=new_name.replace(char,"")
    with open(config_path,"w",encoding="UTF-8") as f:
        f.write(new_name)
    exit()

#"""后续：不双击，拖动文件，整理文件"""
if not os.path.exists(config_path):
    print("首次使用请先双击程序填写你要改的名字")
    input("按回车关闭")
    exit()
real_file_path=sys.argv[1]
try:
    #这个是提取出了文件的绝对路径，然后最后的.txt等等的后缀传给了ext
    file_basename=os.path.basename(real_file_path)
    file_name_no_suffix,ext=os.path.splitext(file_basename)
    #你改的文件名称从config里面提取出来
    with open(config_path,"r",encoding="UTF-8") as f:
        new_name =f.read()
    suffix_new_name=new_name+ext
    #获取当前操作的年月日时分秒
    time_str=time.strftime("%Y-%m-%d-%H_%M_%S")
    #子文件夹名
    homework_child_name=file_name_no_suffix+f" {time_str}"
    #子文件夹路径=父文件夹+子文件夹名称
    homework_child_path=os.path.join(homework_parent_path,homework_child_name)
    if not os.path.exists(homework_child_path):
        #创建子文件夹
        os.mkdir(homework_child_path)
    suffix_homework_child_path=os.path.join(homework_child_path,suffix_new_name)
    if not os.path.exists(suffix_homework_child_path):
        #将作业文件复制到子文件夹里面
        shutil.copyfile(real_file_path,suffix_homework_child_path)
except Exception as e:
    print(f"出错了，错误为{e}")
    input("按回车关闭")