# Inbuild functions with inline lambda

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

    Data_Filter = list(filter(lambda No : No % 2 == 0, Data_Input))
    Data_Map = list(map(lambda No : No * 2, Data_Filter))
    Data_Reduce = reduce(lambda Sum,Value : Sum + Value, Data_Map)

    print("Data after filteration : ",Data_Filter)
    print("Data after mapping : ", Data_Map)
    print("Data after reduction : ", Data_Reduce)

if __name__ == "__main__":
    main()
