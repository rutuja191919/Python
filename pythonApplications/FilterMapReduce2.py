def CheckEven(No):
    return (No % 2 == 0)

def Multiply(No):
    return No * 2

def Addition(Sum, Value):
    return Sum + Value

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

    Data_Filter = list(FilterX(CheckEven, Data_Input))
    Data_Map = list(MapX(Multiply, Data_Filter))
    Data_Reduce = ReduceX(Addition, Data_Map)

    print("Data after filteration : ",list(Data_Filter))
    print("Data after mapping : ", list(Data_Map))
    print("Data after reduction : ", Data_Reduce)

if __name__ == "__main__":
    main()
