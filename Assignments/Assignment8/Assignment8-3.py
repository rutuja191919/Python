def DisplayPattern(Number):
    if (Number > 0):
        print(Number, end=" ")
        DisplayPattern(Number-1)

def main():
    print("Enter the number")
    No = int(input())
    DisplayPattern(No)

if __name__ == "__main__":
    main()