def Fact(Number):
    if Number == 0:
        return 1
    return Number * Fact(Number - 1)

def main():
    print("Enter the number")
    No = int(input())

    Ans = Fact(No)
    print("Factorial : ",Ans)

if __name__ == "__main__":
    main()