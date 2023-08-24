def DisplayFactors(Value):
    i = 1
    print("Factors are : ")
    #for i in range(1,int(Value/2)+1,1)
    while(i <= int(Value/2)):
        if Value % i == 0:
            print(i)
        i = i + 1

def main():
    print("Enter the number")
    No = input()

    DisplayFactors(int(No))

if __name__ == "__main__":
    main()