
def Demo():
    print("Inside Demo")

def Hello(FPTR):
    print("Inside Hello")
    FPTR()

Hello(Demo)     #Name of the function should pass
