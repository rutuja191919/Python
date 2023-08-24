#Demo is defined inside Hello now we cannot call Demo independently
#This is abstraction in python

def Hello():
    print("Inside Hello")

    def Demo(): #private function
        print("Inside Demo")

    Demo()

Hello()