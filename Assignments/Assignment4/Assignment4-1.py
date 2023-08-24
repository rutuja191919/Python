Power = lambda no : 2 ** no

def main():
    iRet = 0
    print("Enter the number")
    no = int(input())

    iRet = Power(no)

    print("Power is : ",iRet)

if __name__ == "__main__":
    main()