# Addition of n numbers
def Addition(Arr):
    iSum = 0
    for no in Arr:
        iSum = iSum + no
    return iSum

def Accept():
    Input = []
    print("Enter the no of elements")
    no = int(input())
    print("Enter elements")
    for i in range(0, no,1):
        Input.append(int(input()))
    return Input

def main():
    Data = list(Accept())
    iRet = Addition(Data)
    print("Addition of the elements in the list is : ",iRet)

if __name__ == "__main__":
    main()