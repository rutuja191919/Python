CheckEven = lambda Value : Value % 2 == 0

Square = lambda Value : Value * Value

Addition = lambda Value, Result : Value + Result

def Accept():
    Input = []
    print("Enter no of elements")
    no = int(input())
    print("Enter elements")
    for i in range(0,no,1):
        Input.append(int(input()))
    return Input

def filterX(Function_name, Arr):
    Result = []
    for no in Arr:
        if(Function_name(no)):
            Result.append(no)
    return Result

def mapX(Function_name, Arr):
    Result = []
    for no in Arr:
        Result.append(Function_name(no))
    return Result

def reduceX(Function_name, Arr):
    Add = 0
    for no in Arr:
        Add = Function_name(Add,no)
    return Add

def main():
    Data = Accept()
    print("Input List :",Data)
    Filter_Result = filterX(CheckEven,Data)
    print("List after filter : ", Filter_Result)

    Map_Result = mapX(Square,Filter_Result)
    #print("List after map : ", Map_Result)
    print("List after map : ",mapX(Square,filterX(CheckEven,Data)))

    Reduce_Result = reduceX(Addition, Map_Result)
    #print("Output of result : ", Reduce_Result)
    print("Output of result : ", reduceX(Addition, mapX(Square,filterX(CheckEven,Data))))

if __name__ == "__main__":
    main()