from MarvellousNum import ChkPrime

def ListPrime():
    Input = []
    print("Enter the no of elements")
    iNo = int(input())
    print("Enter elements")
    for i in range(0, iNo,1):
        iValue = int(input())
        if(ChkPrime(iValue)):
            Input.append(iValue)
    return Input

def Addition(Arr):
    iSum = 0
    for no in Arr:
        iSum = iSum + no
    return iSum

def main():
    Data = list(ListPrime())
    iRet = Addition(Data)

    print("Addition of prime no is : ", iRet)

if __name__ == "__main__":
    main()