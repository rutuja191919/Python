# Pattern

def Display(Value):
    for i in range(0,Value):
        print("*")

def main():
    print("Enter the number")
    no = input()
    Display(int(no))

if __name__ == "__main__":
    main()