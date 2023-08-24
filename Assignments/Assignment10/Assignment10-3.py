import shutil
import os
from sys import *

def Directory_Demo(path1, path2):

    flag = os.path.isabs(path1)
    if flag == False:
        path1 = os.path.abspath(path1)

    exists = os.path.isdir(path1)

    if exists:
        shutil.copytree(path1, path2)
    else:
        print("Invalild path")
        return

def main():
    if(len(argv) < 3):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This script will travel the directory and display the name of all entries")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Application_name Directory_name")
        exit()

    try:
        Directory_Demo(argv[1], argv[2])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()