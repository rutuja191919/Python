# Accept two numbers and perform addition and substraction of it

# Kay karayache ahe?  --> Behaviour
#   Addition & Substraction

# Te karayala kay lagnar ahe?  -->Characteristics
#   2 numbers

# Object Oriented Programming
# Class = Characteristics + Behaviour
# Class = Data + Functions

class Arithmetic:
    def __init__(self,A,B):     # init is constructor and self is like this pointer, constructor is compulsory(__init__)
        self.No1 = A            # No1 and No2 are characteristics and they are directly used in the constructor thats why constructor is compulsory
        self.No2 = B

    def Add(self):              # self keyword is necessary for every method which is part of class
        return self.No1 + self.No2

    def Sub(self):              # self keyword is necessary for every method which is part of class
        return self.No1 - self.No2

def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    obj = Arithmetic(Value1, Value2)

    Ans = obj.Add()     #0X100.Add()  -->Add(0X100)  ...address of object and stored in self
    print("Addition is : ",Ans)

    Ans = obj.Sub()
    print("Substraction is : ",Ans)

if __name__ == "__main__":
    main()
