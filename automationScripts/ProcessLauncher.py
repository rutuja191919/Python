import subprocess
from sys import *
import os

def ProcessLauncher(path):
    subprocess.call(path)

def main():
    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("Help : This script will travel the directory and display the name of all entries")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Application_name Directory_name")
        exit()

    try:
        ProcessLauncher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid Input",E)

if __name__ == "__main__":
    main()