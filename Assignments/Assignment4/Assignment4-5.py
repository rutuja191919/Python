CheckPrime = lambda Value,i : Value == i or Value % i == 0

Multiply = lambda Value : Value * 2

def Maximum(no, Result):
    if no > Result:
        Result = no
    return Result

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
        for i in range(2, int(no / 2)+2, 1):
            if(Function_name(no,i)):
                break
        if i == int(no/2)+1:
            Result.append(no)
    return Result

def mapX(Function_name, Arr):
    Result = []
    for no in Arr:
        Result.append(Function_name(no))
    return Result

def reduceX(Function_name, Arr):
    Max = Arr[0]
    for i in range(1,len(Arr)):
        Max = Function_name(Arr[i],Max)
    return Max

def main():
    Data = Accept()
    print("Input List :",Data)
    Filter_Result = filterX(CheckPrime,Data)
    print("List after filter : ", Filter_Result)
    Map_Result = mapX(Multiply, Filter_Result)
    print("List after map : ",Map_Result)
    Reduce_Result = reduceX(Maximum, Map_Result)
    print("Output of reduce : ", Reduce_Result)

if __name__ == "__main__":
    main()