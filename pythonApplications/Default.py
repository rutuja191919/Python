# Types of arguments

def Area(Radius, PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def main():
   RValue = 10.5
   PIValue = 3.14

   # Positional arguments
   Ans = Area(RValue, PIValue)  #Area(10.5,3.14)
   print("Area of Circle is : ",Ans)

   # Keyword argument with any sequence and same keyword in function call and function def
   Ans = Area(PI = PIValue, Radius = RValue)   #Area(10.5,3.14)
   print("Area of Circle is : ", Ans)

   # Default argument
   Ans = Area(10.5)
   print("Area of Circle is : ", Ans)

   # Keyword with Default argument
   Ans = Area(Radius = 10.5)
   print("Area of Circle is : ", Ans)

   # Keyword with Default argument which takes updated value
   Ans = Area(PI = 7.10, Radius=10.5)
   print("Area of Circle is : ", Ans)


if __name__ == "__main__":
    main()