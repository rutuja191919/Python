# factorial

def Factorial(Value):
    Fact = 1
    for i in range(1,Value+1):
        Fact = Fact * i
    return Fact

def main():
    print("Enter the number")
    no = input()
    Ret = Factorial(int(no))

    print("Factorial of the number is : ",Ret)

if __name__ == "__main__":
    main()