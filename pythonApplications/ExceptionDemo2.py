
def main():
    try:        #this is the syntax error
        print("Enter first number")
        No1 = int(input())

        print("Enter second number")
        No2 = int(input())
        Ans = No1 / No2
        print("Division is : ", Ans)

    except ZeroDivisionError:
        print("Zero division error occured")

    except ValueError:
        print("Value error occured")

    except Exception:
        print("Exception occured")

    finally:
        print("Inside finally block")

if __name__ == "__main__":
    main()