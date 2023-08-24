# Variable no of arguments

def Add(*Values):    #immutable ahe mhanun tuple ahe karan function la list la update karu shaken
    print(type(Values))     #tuple
    print("Number of arguments are : ",len(Values))
    Sum = 0

    for no in Values:    #foreach loop
        Sum = Sum + no

    return Sum

def AddX(*Values):
    Sum = 0

    for i in range(0,len(Values),1):
        Sum = Sum + Values[i]

    return Sum

def main():
    Ans = 0
    Ans = Add(2,3,4,5)
    print("Addition is : ",Ans)

    Ans = Add(10,20)
    print("Addition is : ", Ans)

    Ans = AddX(10, 20)
    print("Addition is : ", Ans)

if __name__ == "__main__":
    main()