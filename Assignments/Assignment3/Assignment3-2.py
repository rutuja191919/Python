# Maximum no of n numbers
def Maximum(Arr):
    Max = Arr[0]
    for i in range(1,len(Arr)):
        if Arr[i] > Max:
            Max = Arr[i]
    return Max

def Accept():
    Input = []
    print("Enter the no of elements")
    no = int(input())
    print("Enter elements")
    for i in range(0, no):
        Input.append(int(input()))
    return Input

def main():
    Data = list(Accept())
    iRet = Maximum(Data)
    print("Maximum no from the list is : ",iRet)

if __name__ == "__main__":
    main()