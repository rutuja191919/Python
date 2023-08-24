
class Value:
    def __init__(self,Value):
        self.No = Value

    def SumFactors(self):
        Sum = 0
        for i in range(1,int((self.No/2)+1),1):
            if self.No % i == 0:
                Sum = Sum + i
        return Sum

    def CheckPerfect(self):
        Sum = self.SumFactors()
        if Sum == self.No:
            return True
        else:
            return False

    def CheckPrime(self):    #best approach for prime
        for i in range(2,int(self.No/2)+2,1):
            if(self.No % i == 0) and (self.No != i):
                break
        if i == int(self.No/2)+1:
            return True
        else:
            return False

def main():
    print("Please enter number")
    Val = int(input())
    Obj = Value(Val)

    iRet = Obj.CheckPerfect()
    if(iRet == True):
        print("{} is a perfect number".format(Val))
    else:
        print("{} is a not a perfect number".format(Val))

    iRet = Obj.CheckPrime()
    if(iRet == True):
        print("Number {} is prime".format(Val))
    else:
        print("Number {} is not prime".format(Val))

if __name__ == "__main__":
    main()