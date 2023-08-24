import threading
def evenfactors(No):
    add = 0
    for i in range(1, int(No/2)+1):
        if No % i  == 0 and i % 2 == 0:
            add = add + i
    print("Addition of the even factors : ",add)

def oddfactors(No):
    add = 0
    for i in range(1, int(No/2)+1):
        if No % i == 0 and i % 2 != 0:
            add = add + i
    print("Addition of the odd factors : ",add)

def main():
    print("Enter the number :")
    Number = int(input())

    t1 = threading.Thread(target = evenfactors, args = (Number,))
    t2 = threading.Thread(target = oddfactors, args = (Number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()