# Digits Addition

def DigitsAddition(Value):
    Add = 0

    while Value != 0:
        Add = Add + (Value % 10)
        Value //= 10
        #Value = int(Value / 10)

    return Add

def main():
    print("Enter the number")
    no = input()
    Ret = DigitsAddition(int(no))

    print("The addition of digits are : ",Ret)

if __name__ == "__main__":
    main()