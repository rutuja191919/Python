def DisplayPattern(Number):
    if (Number > 0):
        DisplayPattern(Number-1)
        print(Number, end=" ")

def main():
    print("Enter the number")
    No = int(input())
    DisplayPattern(No)

if __name__ == "__main__":
    main()