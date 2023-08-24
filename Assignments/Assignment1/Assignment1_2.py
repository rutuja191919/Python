# Check whether number is even or odd

def ChkSum(Value):
    if Value % 2 == 0:
        return True
    else:
        return False

def main():
    print("Enter the number")
    no = input()
    Ret = ChkSum(int(no))

    if Ret == True:
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()