print("Application to demonstrate Industrial Programming")

def main():            #indent 0
    print("Enter first number : ")
    no1 = input()           #indent1
    #print(type(no1))  str

    print("Enter second number : ")
    no2 = input()
    #print(type(no1))  str

    Ans = int(no1) + int(no2)    #indent1
    print("Addition is : ",Ans)  #indent1

if __name__ == "__main__":   #special variable
    print("Inside starter")
    main()





