Power = lambda no1, no2 : no1 * no2

def main():
    iRet = 0
    print("Enter the first number")
    no1 = int(input())

    print("Enter the second number")
    no2 = int(input())

    iRet = Power(no1, no2)

    print("Multiplication is : ",iRet)

if __name__ == "__main__":
    main()