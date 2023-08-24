#Options of import modules

#import Numbers
#from Numbers import DisplayFactors
#from Numbers import *
import Numbers as NUM

def main():
    print("Enter the number")
    No = input()

    #Numbers.DisplayFactors(int(No))
    #DisplayFactors(int(No))    #used with the from imports
    NUM.DisplayFactors(int(No))

if __name__ == "__main__":
    main()