import shutil
import os
from sys import *

def Directory_Demo(path1, path2, ext):

    flag1 = os.path.isabs(path1)
    flag2 = os.path.isabs(path2)

    if flag1 == False or flag2 == False:
        path1 = os.path.abspath(path1)

    exists = os.path.isdir(path1)

    if not os.path.isdir(path2):
        os.mkdir(path2)
    else:
        print("Invalid path")
        return

    if exists:
        for foldername, subfolders, filenames in os.walk(path1):
            for fnames in filenames:
                if fnames.endswith(ext):
                    shutil.copy(os.path.join(foldername, fnames), path2)
    else:
        print("Invalid path")

def main():
    if(len(argv) < 4):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This script will travel the directory and display the name of all entries")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Application_name Directory_name")
        exit()

    try:
        Directory_Demo(argv[1], argv[2], argv[3])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()