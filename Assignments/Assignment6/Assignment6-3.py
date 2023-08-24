class Numbers:
    def __init__(self):
        self.Value = 0

    def Accept(self):
        print("Enter the number : ")
        self.Value = int(input())

    def ChkPrime(self):
        for i in range(2,int((self.Value/2)+2),1):
            if self.Value % i == 0 or self.Value == i:
                break
        if i == int((self.Value/2)+1):
            return True
        else:
            return False

    def ChkPerfect(self, SumFactors):
        if SumFactors == self.Value:
            return True
        else:
            return False

    def SumFactors(self):
        sum = 0
        for i in range(1,int((self.Value/2)+1)):
            if self.Value % i == 0:
                sum = sum + i
        return sum

    def Factors(self):
        print("Factors are : ")
        for i in range(1,int((self.Value/2)+1)):
            if self.Value % i == 0:
                print(i , end = "\t")
        print()

def main():
    Obj1 = Numbers()
    Obj1.Accept()
    Obj1.Factors()
    print("Sum of factors is : ",Obj1.SumFactors())
    print("Is number prime : ",Obj1.ChkPrime())
    print("Is number perfect : ",Obj1.ChkPerfect(Obj1.SumFactors()))

    Obj2 = Numbers()
    Obj2.Accept()
    Obj2.Factors()
    print("Sum of factors is : ",Obj2.SumFactors())
    print("Is number prime : ",Obj2.ChkPrime())
    print("Is number perfect : ",Obj2.ChkPerfect(Obj1.SumFactors()))

if __name__ == "__main__":
    main()