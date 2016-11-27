import os
import psutil
import shutil
import sys

print("hello")

while True:
    is_continue = raw_input("continue (y/n)? ")
    if is_continue == "y":

        print("I can print: ")
        print(" [1] - file list")
        print(" [2] - system info")
        print(" [3] - process list")
        print(" [4] - duplicate files in cur dir")

        do = int(raw_input("select, please: "))
        if do == 1:
            print(os.listdir("."))
        elif do == 2:
            print("SYSTEM INFO")
            print("platform", sys.platform)
            print("os name", os.name)
            print("current dir", os.getcwd())
            print("current user", os.getlogin())
            print("file system coding", sys.getfilesystemencoding())
            print("CPU count: ", psutil.cpu_count(logical=False))
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            file_list = os.listdir(".")
            print("files in dir:", file_list)
            print("duplicating....")
            i = 0
            while i < len(file_list):
                shutil.copy(file_list[i], file_list[i] + '.dupl')
                #os.remove(file_name) to revert
                i += 1
            file_list = os.listdir(".")
            print("files in dir:", file_list)
        else:
            print("unknown operation")
    elif is_continue == "n":
        print("nooooo")
        break
    else:
        print("hwat??")
