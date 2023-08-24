import time
import threading

def DisplayEven(No):
    for i in range(1,No+1,1):
        if i % 2 == 0:
            print("Even Number : ",i)

def DisplayOdd(No):
    for i in range(1,No+1,1):
        if i % 2 != 0:
            print("Odd Number : ",i)

def main():
    print("Demonstration of parallel programming using multiple processes")
    Number = 20000

    t1 = threading.Thread(target = DisplayEven, args = (Number,))   #handle for the process
    t2 = threading.Thread(target = DisplayOdd, args = (Number,))    #handle for the process

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()  #Execution time of the process(main)
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)