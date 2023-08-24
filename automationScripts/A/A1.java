import os
from sys import *

#def Directory_Watcher(Dir_Name):

def main():
    print("Directory Watcher Application")

    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This script will travel the directory and display the name of all entries")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Application_name Directory_name")
        exit()

    #Directory_Watcher(argv[1])

if __name__ == "__main__":
    main()