
def Add(Value):
    if(Value <= 0):
        return 0
    else:
        return (Value + Add(Value - 1))

Ret = Add(4)

print("Result is : ",Ret)

