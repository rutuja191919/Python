
class Addition:
    def __init__(self):
        self.Size = 0
        self.Arr = list()
        self.Accept()
        self.Display()

    def Accept(self):
        print("Enter the no of elements")
        self.Size = int(input())

        print("Enter the elements")
        for i in range(0, self.Size, 1):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements from list are : ")
        for Value in self.Arr:
            print(Value, end = " ")
        print()

    def Sum(self):
        Sum = 0
        for i in range(0,len(self.Arr),1):
            Sum = Sum + self.Arr[i]
        return Sum

    def Average(self):
        Sum = 0
        for i in range(0, len(self.Arr), 1):
            Sum = Sum + self.Arr[i]
        return Sum/self.Size

    def Maximum(self):
        Max = self.Arr[0]
        for Value in self.Arr:
            if Value > Max:
                Max = Value
        return Value

    def Minimum(self):
        Min = self.Arr[0]
        for Value in self.Arr:
            if Value < Min:
                Min = Value
        return Min

def main():
    obj = Addition()
    iRet = obj.Sum()
    print("Addition of numbers is : ",iRet)
    iRet = obj.Average()
    print("Average of numbers is : ", iRet)
    iRet = obj.Minimum()
    print("Minimum number is : ",iRet)
    iRet = obj.Maximum()
    print("Maximum number is : ", iRet)

    obj1 = Addition()
    iRet = obj1.Sum()
    print("Addition of numbers is : ",iRet)
    iRet = obj1.Average()
    print("Average of numbers is : ",iRet)
    iRet = obj1.Minimum()
    print("Minimum numbers is : ", iRet)
    iRet = obj1.Maximum()
    print("Maximum numbers is : ", iRet)

if __name__ == "__main__":
    main()