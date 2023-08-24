# Check Number is divisible by 5 or not

def ChkDivisibleByFive(Value):
    if Value % 5 == 0:
        return True
    else:
        return False

def main():
    print("Enter the number")
    no = input()
    Ret = ChkDivisibleByFive(int(no))

    if Ret == True:
        print("No is divisible by 5")
    else:
        print("No is not divisible by 5")

if __name__ == "__main__":
    main()