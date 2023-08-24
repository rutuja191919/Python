
def Display(Value):
    if(Value > 1):
        Value = Value - 1
        Display(Value)  #Recursive Call head
        print(Value)

print("Enter the number : ")
Value = int(input())

Display(Value)

