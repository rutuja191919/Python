
from sys import *

def Addition(No1, No2):
    return No1 + No2

def main():
    if (len(argv) != 3):
        print("Invalid number of arguments")
        exit()

    Ret = Addition(int(argv[1]), int(argv[2]))
    print("The addition is : ",Ret);

if __name__ =="__main__":
    main()


#python Command1.py 12 Hello 21