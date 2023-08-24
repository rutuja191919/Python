import os
from sys import *

def Directory_Demo(path, File_Ext1, File_Ext2):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolders, filenames in os.walk(path):
            for fnames in filenames:
                if File_Ext1 in fnames:
                    filename = os.path.join(foldername,fnames)
                    os.rename(filename,filename.replace(File_Ext1, File_Ext2))
    else:
        print("Invalid path")
        return

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