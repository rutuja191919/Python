# Call Arithmetic Module

from Arithmetic import *

def main():
    print("Enter first number")
    no1 = input()

    print("Enter second number")
    no2 = input()

    Ret = Add(int(no1),int(no2))
    print("Addition is : ",Ret)

    Ret = Sub(int(no1),int(no2))
    print("Substraction is : ",Ret)

    Ret = Mult(int(no1),int(no2))
    print("Multiplication is : ",Ret)

    Ret = Div(int(no1),int(no2))
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()