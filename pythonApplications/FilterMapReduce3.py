# Using lambda with user defined function

CheckEven = lambda No : No % 2 == 0

Doubles = lambda No : No * 2

Addition = lambda Sum,Value : Sum + Value

def Accept_List():
    Data = []  # empty list
    print("Enter the no of elements")
    iSize = int(input())
    print("Please enter the data")
    for iCnt in range(0, iSize, 1):
        Value = int(input())
        Data.append(Value)
    return Data

def FilterX(Helper_Function, Data):
    FilterData = []
    for no in Data:
        if(Helper_Function(no)):
            FilterData.append(no)
    return FilterData

def MapX(Helper_Function, Data):
    MapData = []
    for no in Data:
        MapData.append(Helper_Function(no))
    return MapData

def ReduceX(Helper_Function, Data):
    Sum = 0
    for no in Data:
        Sum = Helper_Function(Sum, no)
    return Sum

def main():
    Data_Input = list(Accept_List())

    Data_Filter = FilterX(CheckEven, Data_Input)
    Data_Map = MapX(Doubles, Data_Filter)
    Data_Reduce = ReduceX(Addition, Data_Map)

    print("Data after filteration : ",Data_Filter)
    print("Data after mapping : ", Data_Map)
    print("Data after reduction : ", Data_Reduce)

if __name__ == "__main__":
    main()
