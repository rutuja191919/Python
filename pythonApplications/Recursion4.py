
def Display(Value):
    if(Value > 0):
        print(Value)
        Value = Value-1
        Display(Value)  #Recursive Call tail

print("Enter the number : ")
Value = int(input())

Display(Value)

