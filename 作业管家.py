import os
import time
import shutil
import sys
from importlib.util import source_hash

desktop=os.path.expanduser("~/Desktop")#获取用户桌面地址
main_folder=os.path.join(desktop,"作业总目录")#在桌面生成操作的总文件
config_flie_name="rename_config.txt"
config_path=os.path.join(main_folder,config_flie_name)
if not os.path.exists(main_folder):#条件判断，如果没有该文件夹则创建
    os.mkdir(main_folder)
    print("主文件创建成功")
else:
    print("主文件已存在")
invalid_chars=r'<>:"/\|?*'
if len(sys.argv) < 2:
    # print("错误：你只是双击打开了，你要做的是把文件拖到这里来")
    print("-----设置重命名的名称-----")
    preset_name = input("请输入重命名名称，无需后缀")
    for char in invalid_chars:
        preset_name = preset_name.replace(char, "")

    with open(config_path, "w", encoding="utf-8") as f:
        f.write(preset_name)
    print(f"预设重命名-{preset_name}-已保存")
    input("点击回车关闭")
    exit()

#子文件夹创建
time_str=time.strftime("%Y_%m_%d-%H_%M_%S")#获取当前操作时间年月日时分秒
#提取原文件名
source_files=sys.argv[1]
original_basename=os.path.basename(source_files)
original_no_ext,original_ext=os.path.splitext(original_basename)
#特殊符号处理
for char in invalid_chars:
    original_no_ext=original_no_ext.replace(char,"")

new_time_str=f"{time_str}_{original_no_ext}"
sub_folder=os.path.join(main_folder,new_time_str)#在主文件夹里面创建子文件夹
if not os.path.exists(sub_folder):#条件判断，如果没有该文件夹则创建
    os.mkdir(sub_folder)
    print("子文件创建成功")
else:
    print("文件已存在，请勿重复操作")

#双击打开输入重命名名称，开始

if not os.path.exists(config_path):
    print("还没有设置名称，先双击填写名字")
    input("点击回车关闭")
    exit()
with open(config_path, "r", encoding="utf-8") as f:
    prefix_name = f.read().strip()
if not os.path.isfile(source_files):
    print("错误：请传入文件，不要传入与文件无关的东西")
    input("点击回车关闭")
    exit()
else:
    _,ext=os.path.splitext(source_files)
    for char in invalid_chars:
        prefix_name=prefix_name.replace(char,"")

    new_name=f"{prefix_name}{ext}"
    target_files = os.path.join(sub_folder, new_name)

try:
    shutil.copyfile(source_files, target_files)
    print("文件复制重命名完成")
except Exception as error:
    print(f"文件复制重命名失败，错误信息为：{error}")
