class Arithmetic:
    def __init__(self, A, B):  #special method with keyword as self and special variable __init__
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Addition(self):
        return self.No1 + self.No2

    def Substraction(self):
        return self.No1 - self.No2

def main():
    print("Inside main method")

    print("Enter first number")
    num1 = int(input())

    print("Enter second number")
    num2 = int(input())

    obj = Arithmetic(num1, num2)
    iRet = obj.Addition()
    print("Addition is : ",iRet)
    iRet = obj.Substraction()
    print("Substraction is : ",iRet)

    obj1 = Arithmetic(30, 20)
    iRet = obj1.Addition()
    print("Addition is : ", iRet)
    iRet = obj1.Substraction()
    print("Substraction is : ", iRet)

if __name__ == "__main__":
    print("Inside starter")
    main()