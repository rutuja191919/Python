# pattern

def DisplayPattern(Value):
    for i in range(0,Value):
        for j in range(0,Value):
            print("*",end = " ")
        print(" ")

def main():
    print("Enter the number")
    no = input()
    DisplayPattern(int(no))

if __name__ == "__main__":
    main()