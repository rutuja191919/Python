print("Application to demonstrate Industrial Programming")

def Addition(Value1, Value2):    #acts as generic function
    Ans = Value1 + Value2    #indent1
    return Ans

def main():
    print("Enter first number : ")
    no1 = int(input())
    print("Enter second number : ")
    no2 = int(input())

    Ret = Addition(no1,no2)
    print("Addition is : ",Ret)  #indent1

if __name__ == "__main__":   #special variable
    print("Inside starter")
    main()





