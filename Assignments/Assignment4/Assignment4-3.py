#def Compare(Value):
        #if Value >= 70 and Value <= 90:
            #return True

#def Increment(Value):
    #Value = Value + 10
    #return Value

Compare = lambda Value : Value >= 70 and Value <= 90

Increment = lambda Value : Value + 10

Product = lambda Value, Result : Value * Result

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
    Mult = 1
    for no in Arr:
        Mult = Function_name(Mult,no)
    return Mult

def main():
    Data = Accept()
    print("Input List :",Data)
    Filter_Result = filterX(Compare,Data)
    print("List after filter : ", Filter_Result)

    Map_Result = mapX(Increment,Filter_Result)
    #print("List after map : ", Map_Result)
    print("List after map : ",mapX(Increment,filterX(Compare,Data)))

    Reduce_Result = reduceX(Product, Map_Result)
    #print("Output of result : ", Reduce_Result)
    print("Output of result : ", reduceX(Product, mapX(Increment,filterX(Compare,Data))))

if __name__ == "__main__":
    main()