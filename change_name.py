import os
import time
import shutil
import sys
from importlib.util import source_hash

desktop=os.path.expanduser("~/Desktop")#获取用户桌面地址
main_folder=os.path.join(desktop,"作业总目录")#在桌面生成操作的总文件
if not os.path.exists(main_folder):#条件判断，如果没有该文件夹则创建
    os.mkdir(main_folder)
    print("主文件创建成功")
else:
    print("主文件已存在")

time_str=time.strftime("%Y%m%d_%H%M%S")#获取当前操作时间年月日时分秒
sub_folder=os.path.join(main_folder,time_str)#在主文件夹里面创建子文件夹
if not os.path.exists(sub_folder):#条件判断，如果没有该文件夹则创建
    os.mkdir(sub_folder)
    print("子文件创建成功")
else:
    print("文件已存在，请勿重复操作")

#original_name=input("输入你想要重命名的原文件名称，要完整带后缀(xxx.pdf)这样")
# source_files=rf"{main_folder}/{original_name}”#这个是俗手
#source_files=os.path.join(main_folder,original_name) #这是初版操作
if len(sys.argv)<2:
    print("错误：你只是双击打开了，你要做的是把文件拖到这里来")
    input("点击回车关闭")
    exit()

source_files=sys.argv[1]

if not os.path.isfile(source_files):
    print("错误：请传入文件，不要传入与文件无关的东西")
    input("点击回车关闭")
    exit()
else:
    new_name = input("输入你想要重命名文件名称，要完整带后缀(xxx.pdf)这样 ")  # new_name可更改
    target_files = os.path.join(sub_folder, new_name)
    shutil.copyfile(source_files, target_files)
    print("文件复制重命名完成")
# if not os.path.exists(source_files):
#     print("错误：该文件不存在或文件名称输入不正确")
# else:
#     new_name=input("输入你想要重命名文件名称，要完整带后缀(xxx.pdf)这样 ")#new_name可更改
#     target_files=os.path.join(sub_folder,new_name)
#     shutil.copyfile(source_files,target_files)
#     print("文件复制重命名完成")







# if __name__=="__main__":
#     os.rename("test.txt",new_name)
