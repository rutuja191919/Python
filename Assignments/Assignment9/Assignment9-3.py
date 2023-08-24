import os
from sys import *

def ReadFile(FileName):
    if(os.path.exists(FileName)):
        fd1 = open("Demo.txt",'w')
        fd2 = open(FileName,'r')
        Data = fd2.read()
        fd1.write(Data)
        print("Successfully written into file")
        fd1.close()
        fd2.close()

    else:
        print("File is not exists")
        return

def main():
    if(len(argv) != 2):
        print("Invalid number of arguments")

    ReadFile(argv[1])

if __name__ == "__main__":
    main()