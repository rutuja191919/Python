# No of digits

def CalculateDigits(Value):
    Cnt = 0

    while Value != 0:
        Cnt = Cnt + 1
        Value = int(Value / 10)

    return Cnt

def main():
    print("Enter the number")
    no = input()
    Ret = CalculateDigits(int(no))

    print("The no of digits are : ",Ret)

if __name__ == "__main__":
    main()