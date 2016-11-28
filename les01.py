import os
import psutil
import shutil
import sys


def smart_file_duplication(f):
    if os.path.isfile(f):
        shutil.copy(f, f + '.dupl')
        if os.path.exists: # checking if duplication was successful
            print("duplicated: " + f)
            return True
        else:
            print("ERROR while duplicating file: " + f)
            return False
    else:
        print("ignoring directory: " + f)
        return False

print("hello", bcolors.HEADER)

is_continue = "y"
while True:
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
            print("duplicating....")
            file_list = os.listdir(".")
            for f in file_list:
                smart_file_duplication(f)

        elif do == 5: # Duplicate specified file
            print("duplicating....")
            f = raw_input("enter file name: ")
            smart_file_duplication(f)

        elif do == 6: # Remove duplicates
            print("removing duplicates....")
            file_list = os.listdir(".")
            for f in file_list:
                if os.path.isfile(f) and f.endswith('.dupl'):
                    print("to be removed: ", f)
                    os.remove(f)

        else:
            print("unknown operation")
    elif is_continue == "n":
        print("nooooo")
        break
    else:
        print("hwat??")

    is_continue = raw_input("continue (y/n)? ")
