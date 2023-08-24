def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def main():
    print("Enter first number")
    No1 = int(input())

    print("Enter second number")
    No2 = int(input())

    Ret = Add(No1, No2)
    print("Addition is : ",Ret)

    Ret = Sub(No1, No2)
    print("Substraction is : ",Ret)

if __name__ == "__main__":
    main()