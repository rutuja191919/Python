
def Fact(Value):
    if(Value<=0):
        return 1
    else:
        return (Value * Fact(Value - 1))

Ret = Fact(5)

print("Result is : ",Ret)

