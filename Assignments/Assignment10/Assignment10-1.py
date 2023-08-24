import os
import datetime
from sys import *

def Directory_Demo(path, Dir_Ext):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        ct = datetime.datetime.now().strftime("%Y%m%d-%H%M%S");
        str_ct = str(ct)
        file_name = str_ct+".txt"
        fd = open(file_name,'w')

        for foldername, subfolders, filenames in os.walk(path):
            for fnames in filenames:
                if Dir_Ext in fnames:
                    fd.write("File inside folder "+foldername+ " is " +fnames+"\n")

    else:
        print("Invalid path")
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