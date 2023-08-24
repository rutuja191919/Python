# Factors addition

def FactAdd(Value):
    Add = 0
    for i in range(1,int(Value/2)+1):
        if Value % i == 0:
            Add = Add + i

    return Add

def main():
    print("Enter the number")
    no = input()
    Ret = FactAdd(int(no))

    print("Addition of the factors is : ",Ret)

if __name__ == "__main__":
    main()