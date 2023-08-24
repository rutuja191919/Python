# Minimum no of n numbers
def Minimum(Arr):
    Min = Arr[0]
    for i in range(1,len(Arr)):
        if Arr[i] < Min:
            Min = Arr[i]
    return Min

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
    iRet = Minimum(Data)
    print("Minimum no from the list is : ",iRet)

if __name__ == "__main__":
    main()