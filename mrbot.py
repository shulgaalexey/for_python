import os
import psutil
import shutil
import sys

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printcol(s, c):
    print(c + s + colors.ENDC)


def file_duplication(f):
    if os.path.isfile(f):
        shutil.copy(f, f + '.dupl')
        if os.path.exists: # checking if duplication was successful
            print("duplicated: " + f)
            return True
        else:
            printcol("ERROR while duplicating file: " + f, colors.FAIL)
            return False
    else:
        printcol("ignoring directory: " + f, colors.WARNING)
        return False


def delete_duplicates():
    file_list = os.listdir(".")
    cnt = 0
    for f in file_list:
        if os.path.isfile(f) and f.endswith('.dupl'):
            print("to be removed: " + f)
            os.remove(f)
            if not os.path.exists(f):
                cnt += 1
    return cnt


def system_info():
    printcol("SYSTEM INFO", colors.BLUE)
    printcol("platform: " + sys.platform, colors.BLUE)
    printcol("os name: " +  os.name, colors.BLUE)
    printcol("current dir: " + os.getcwd(), colors.BLUE)
    printcol("current user: " + os.getlogin(), colors.BLUE)
    printcol("file system coding: " + sys.getfilesystemencoding(), colors.BLUE)
    printcol("CPU count: " + str(psutil.cpu_count(logical=False)), colors.BLUE)


def main():
    printcol("\nHello\n", colors.HEADER)

    is_continue = "y"
    while True:
        if is_continue == "y":

            printcol("I can do following: ", colors.GREEN)
            printcol(" [1] - Print file list", colors.GREEN)
            printcol(" [2] - Print system info", colors.GREEN)
            printcol(" [3] - Print process list", colors.GREEN)
            printcol(" [4] - Duplicate files in cur dir", colors.GREEN)
            printcol(" [5] - Duplicate specified file", colors.GREEN)
            printcol(" [6] - Remove duplicates", colors.GREEN)

            do = int(raw_input(colors.GREEN + "select, please: " + colors.ENDC))

            if do == 1: # Print file list
                print(os.listdir("."))

            elif do == 2: # Print system info
               system_info()

            elif do == 3: # Print process list
                print(psutil.pids())

            elif do == 4: #Duplicate file list
                print("duplicating....")
                file_list = os.listdir(".")
                for f in file_list:
                    file_duplication(f)

            elif do == 5: # Duplicate specified file
                print("duplicating....")
                f = raw_input(colors.GREEN + "enter file name: " + colors.ENDC)
                file_duplication(f)

            elif do == 6: # Remove duplicates
                print("removing duplicates....")
                cnt = delete_duplicates()
                printcol("total: " + str(cnt), colors.WARNING)

            else:
                print("unknown operation")
        elif is_continue == "n":
            printcol("\nNoooooooooo\n", colors.HEADER)
            break
        else:
            printcol("\nHwat??\n", colors.FAIL)

        is_continue = raw_input(colors.GREEN + "continue (y/n)? " + colors.ENDC)

if __name__ == "__main__":
    main()
