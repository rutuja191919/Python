#input from command line arguments

from Numbers import *
from sys import *  #OS specific files

def main():
    print("Application name is : ",argv[0])
    DisplayFactors(int(argv[1]))

if __name__ == "__main__":
    main()


#python Factors4.py 12