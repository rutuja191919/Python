#return function reference(name) from the another function
#By this method you can call the inner function when outer returns that function name
#Functions are first class object in the python

def Outer():
    print("Inside Outer")

    def Inner():
        print("Inside Inner")

    print(id(Inner))
    return Inner

ret = Outer()       #You can use placeholder for the function name to pass as well as when return that function reference
print(type(ret))
print(id(ret))
ret()   #release abstraction