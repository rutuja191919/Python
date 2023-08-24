class Demo:
    Value = 0
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print(self.no1)

    def Gun(self):
        print(self.no2)

def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    obj = Demo(Value1, Value2)
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj.Fun()
    obj.Gun()
    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()

if __name__ == "__main__":
    main()