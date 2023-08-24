class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first number")
        self.Value1 = int(input())

        print("Enter second number")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2

def main():

    obj1 = Arithmetic()
    obj2 = Arithmetic()

    obj1.Accept()
    print("Addition : ",obj1.Addition())
    print("Substraction : ", obj1.Substraction())
    print("Multiplication : ", obj1.Multiplication())
    print("Division : ", obj1.Division())
    print()

    obj2.Accept()
    print("Addition : ", obj2.Addition())
    print("Substraction : ", obj2.Substraction())
    print("Multiplication : ", obj2.Multiplication())
    print("Division : ", obj2.Division())

if __name__ == "__main__":
    main()