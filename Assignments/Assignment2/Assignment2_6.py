# Pattern

def DisplayPattern(Value):
    for i in range(Value,0,-1):
        for j in range(i,0,-1):
            print("*",end = " ")
        print(" ")

def main():
    print("Enter the number")
    no = input()
    DisplayPattern(int(no))

if __name__ == "__main__":
    main()