# inbuild functions with inline lambda

from functools import reduce

def Accept_List():
    Data = []  # empty list
    print("Enter the no of elements")
    iSize = int(input())
    print("Please enter the data")
    for iCnt in range(0, iSize, 1):
        Value = int(input())
        Data.append(Value)
    return Data

def main():
    Data_Input = list(Accept_List())

    print("Data after reduction : ", reduce(lambda Sum,Value : Sum + Value,map(lambda No : No * 2, filter(lambda No : No % 2 == 0, Data_Input))))

if __name__ == "__main__":
    main()
