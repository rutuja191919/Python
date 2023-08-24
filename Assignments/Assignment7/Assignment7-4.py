import threading

def small(str):
    count = 0
    print("Thread id ", threading.current_thread().ident, " Thread Name : ", threading.current_thread().name)
    for letter in str:
        if letter.islower() == True:
            count = count + 1
    print("No of small letters are : ",count)

def capital(str):
    count = 0
    print("Thread id ",threading.current_thread().ident," Thread Name : ",threading.current_thread().name)
    for letter in str:
        if letter >= 'A' and letter <= 'Z':
            count = count + 1
    print("No of capital letters are : ",count)

def digits(str):
    count = 0
    print("Thread id ",threading.current_thread().ident," Thread Name : ",threading.current_thread().name)
    for letter in str:
        if letter.isdigit():
            count = count + 1
    print("No of digits are : ",count)

def main():
    print("Enter the string")
    str = input()

    t1 = threading.Thread(name = 'small',target = small, args = (str,))
    t2 = threading.Thread(name = 'capital',target = capital, args = (str,))
    t3 = threading.Thread(name = 'digits',target = digits, args = (str,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
