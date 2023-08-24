import os

def main():
    print("PID of the current process is : ",os.getpid())
    print("PID of the parent process is : ",os.getppid())

if __name__ == "__main__":
    main()