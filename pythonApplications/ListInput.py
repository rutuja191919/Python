# take the nos from user and insert that numbers in the list

def main():
    Arr  = list();   #list creation is there : list object is created

    print("Enter how many elements you want to store?")
    size = int(input())

    print("Please enter the values")

    for i in range(0,size):
        no = int(input())
        Arr.append(no)  # Arr.insert(i,no)

    print(Arr)

if __name__ == "__main__":
    print("Inside Starter")
    main()
