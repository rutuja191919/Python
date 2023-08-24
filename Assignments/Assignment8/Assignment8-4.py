def DigitsAddition(Number):
    if Number == 0:
        return 0
    return int(Number % 10) + DigitsAddition(int(Number/10))

def main():
    print("Enter the number")
    No = int(input())

    Ans = DigitsAddition(No)
    print("Addition : ",Ans)

if __name__ == "__main__":
    main()