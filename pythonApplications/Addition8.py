print("Application to demonstrate Industrial Programming")

import MarvellousModule

def main():
    print("Value of __name__ from main is : ",__name__)
    print("Enter first number : ")
    no1 = int(input())
    print("Enter second number : ")
    no2 = int(input())

    Ret = MarvellousModule.Addition(no1, no2)
    print("Addition is : ",Ret)  #indent1

if __name__ == "__main__":   #special variable
    print("Inside starter")
    main()





