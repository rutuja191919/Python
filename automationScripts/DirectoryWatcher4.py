import os
from sys import *

def Directory_Watcher(path,ext):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolders, filenames in os.walk(path):
            for fnames in filenames:
                if fnames.lower().endswith(ext):        #case insensitive extension
                    print(fnames)
    else:
        print("Invalid path")

def main():
    print("Directory Watcher Application")

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This script will travel the directory and display the name of all entries")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Application_name Directory_name")
        exit()

    if (len(argv) != 3):
        print("Insufficient arguments")
        exit()

    Directory_Watcher(argv[1], argv[2])

if __name__ == "__main__":
    main()