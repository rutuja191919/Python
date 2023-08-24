import os
from sys import *

def ReadFile(FileName1, FileName2):
    if(os.path.exists(FileName1) and os.path.exists(FileName2)):
        fd1 = open(FileName1,'r')
        fd2 = open(FileName2,'r')
        Data1 = fd1.read()
        Data2 = fd2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        fd1.close()
        fd2.close()

    else:
        print("File is not exists")
        return

def main():
    if(len(argv) != 3):
        print("Invalid number of arguments")

    ReadFile(argv[1], argv[2])

if __name__ == "__main__":
    main()