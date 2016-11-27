import os
import psutil
import shutil
import sys

print("hello")

while True:
    is_continue = raw_input("continue (y/n)? ")
    if is_continue == "y":

        print("I can do following: ")
        print(" [1] - Print file list")
        print(" [2] - Print system info")
        print(" [3] - Print process list")
        print(" [4] - Duplicate files in cur dir")
        print(" [5] - Duplicate specified file")
        print(" [6] - Remove duplicates")

        do = int(raw_input("select, please: "))
        if do == 1: # Print file list
            print(os.listdir("."))
        elif do == 2: # Print system info
            print("SYSTEM INFO")
            print("platform", sys.platform)
            print("os name", os.name)
            print("current dir", os.getcwd())
            print("current user", os.getlogin())
            print("file system coding", sys.getfilesystemencoding())
            print("CPU count: ", psutil.cpu_count(logical=False))
        elif do == 3: # Print process list
            print(psutil.pids())
        elif do == 4: #Duplicate file list
            file_list = os.listdir(".")
            print("files in dir:", file_list)
            print("duplicating....")
            i = 0
            while i < len(file_list):
                if file_list[i][0] == '.':
                    i += 1
                    continue
                print("copying...: ", file_list[i])
                shutil.copy(file_list[i], file_list[i] + '.dupl')
                i += 1
            file_list = os.listdir(".")
            print("files in dir:", file_list)
        elif do == 5: # Duplicate specified file
            file_list = os.listdir(".")
            print("files in dir:", file_list)
            file_to_dup = raw_input("enter file name: ")
            print("duplicating....")
            i = 0
            while i < len(file_list):
                if file_list[i] == file_to_dup:
                    shutil.copy(file_list[i], file_list[i] + '.dupl')
                i += 1
            file_list = os.listdir(".")
            print("files in dir:", file_list)
        elif do == 6: # Remove duplicates
            file_list = os.listdir(".")
            print("files in dir:", file_list)
            print("removing duplicates....")
            i = 0
            while i < len(file_list):
                file_name = file_list[i]
                extension = os.path.splitext(file_name)[1]
                if extension == '.dupl':
                    print("to be removed: ", file_name)
                    os.remove(file_name)
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
