# Return the frequency of the no from list

def Frequency(Arr, iNo):
    iFreq = 0
    for no in Arr:
        if no == iNo:
            iFreq = iFreq + 1
    return iFreq

def Accept():
    Input = []
    print("Enter the no of elements")
    iNo = int(input())
    print("Enter elements")
    for i in range(0, iNo,1):
        Input.append(int(input()))
    return Input

def main():
    Data = list(Accept())
    print("Enter the number")
    iValue = int(input())
    iRet = Frequency(Data, iValue)
    print("Frequency of the no is : ",iRet)

if __name__ == "__main__":
    main()