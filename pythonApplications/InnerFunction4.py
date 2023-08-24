def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def Calculator(Name_Of_Operation,Value1,Value2):
    return Name_Of_Operation(Value1, Value2)

iRet = Calculator(Add,10,20)   #positional arguments
print("Addition is : ",iRet)

iRet = Calculator(Value1 = 20,Value2 = 10,Name_Of_Operation = Sub)   #Keyword arguments
print("Substraction is : ",iRet)
