#Positional Arguments, keyword arguments

def Add1(No1,No2):
    print("Value of No1 : ",No1)
    print("Value of No2 : ",No2)
    return No1 - No2

def Sub1(No1,No2):
    print("Value of No1 : ",No1)
    print("Value of No2 : ",No2)
    return No1 - No2

def main():
    #Positional arguments
    Ans = Add1(10,11)
    print("Addition is : ",Ans)

    #keyword arguments
    Ans = Sub1(No1 = 10, No2 = 11)      #Name of the parameter and argument should be sma ein keyword
    print("Substraction is : ",Ans)


if __name__ == "__main__":
    main()