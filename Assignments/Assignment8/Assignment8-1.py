def DisplayPattern(Number):
    if(Number > 0):
        print("*",end = " ")
        Number = Number - 1
        DisplayPattern(Number)

def main():
    print("Enter the number")
    No = int(input())
    DisplayPattern(No)

if __name__ == "__main__":
    main()