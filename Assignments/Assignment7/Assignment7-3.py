import threading
import time

def evenlist(No):
    add = 0
    for i in No:
        if i % 2 == 0:
            add = add+i
    print("Addition of even nos : ",add)

def oddlist(No):
    add = 0
    for i in No:
        if i % 2 != 0:
            add = add + i
    print("Addition of odd nos : ",add)

def main():
    Numbers = []

    print("Enter the no of elements in the list")
    size = int(input())

    print("Enter the elements in the list")
    for i in range(1, size+1, 1):
        ele = int(input())
        Numbers.append(ele)

    t1 = threading.Thread(target = evenlist, args = (Numbers,))
    t2 = threading.Thread(target = oddlist, args = (Numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time of the process : ",end_time - start_time)