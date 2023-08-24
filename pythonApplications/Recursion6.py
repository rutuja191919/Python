
def Add(Value):
    Sum = 0
    while(Value >= 0):
        Sum = Sum + Value
        Value = Value - 1
    return Sum

Ret = Add(4)

print("Result is : ",Ret)

