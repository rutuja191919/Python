# Prime no

def ChkPrime(Value):
    if Value == 2:
        return True
    i = 2
    for i in range(2,int(Value/2)+2):
        if Value % i == 0:
            break
    if i == int(Value/2)+1:
        return True
    else:
        return False

def main():
    print("Enter the number")
    no = input()
    Ret = ChkPrime(int(no))

    if Ret == True:
        print("Prime no")
    else:
        print("Not a prime no")

if __name__ == "__main__":
    main()