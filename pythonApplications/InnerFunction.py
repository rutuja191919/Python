#two functions are independent

def Demo():
    print("Inside Demo")

def Hello():
    print("Inside Hello")
    Demo()

Hello()
Demo()