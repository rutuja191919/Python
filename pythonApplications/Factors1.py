def factors(Value):
    print("Factors are : ")
    for i in range(1,int((Value/2)+1),1):
        if Value % i == 0:
            print(i)

def main():
    print("Enter the number")
    No = input()

    factors(int(No))

if __name__ == "__main__":
    main()