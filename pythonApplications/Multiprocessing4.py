import time
import multiprocessing

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
    Number = 200

    p1 = multiprocessing.Process(target = DisplayEven, args = (Number,))   #handle for the process
    p2 = multiprocessing.Process(target = DisplayOdd, args = (Number,))    #handle for the process

    p1.start()
    p2.start()

    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()  #Execution time of the process
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)