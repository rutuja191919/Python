import threading
import time

def Display():
    print("Display 1 to 50 digits")
    for i in range(1,51):
        print(i, end = " ")
    print()
    print()

def DisplayReverse():
    print("Display 50 to 1 digits")
    for i in range(50,0,-1):
        print(i, end = " ")
    print()

def main():
    Thread1 = threading.Thread(target = Display)
    Thread2 = threading.Thread(target=DisplayReverse)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time of the process : ",end_time - start_time)