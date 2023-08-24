# Check that number is positive, negative or zero

def ChkNumber(Value):
    if Value == 0:
        print("Zero")
    else:
        if Value > 1:
            print("Positive Number")
        else:
            if Value < 1:
                print("Negative Number")

def main():
    print("Enter the number")
    no = input()

    ChkNumber(int(no))

if __name__ == "__main__":
    main()