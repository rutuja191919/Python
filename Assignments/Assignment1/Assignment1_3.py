# Addition of two numbers

def Addition(Value1, Value2):
    return Value1 + Value2

def main():
    print("Enter the numbers")
    no1 = input()
    no2 = input()

    Ret = Addition(int(no1), int(no2))

    print("Addition of numbers is : ",Ret)

if __name__ == "__main__":
    main()