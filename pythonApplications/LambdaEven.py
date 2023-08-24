
# Compact version
def CheckEvenX(No):
    return (No % 2 == 0)

Ret = CheckEvenX(10)

if Ret == True:
    print("Even")
else:
    print("Odd")

# Lambda function
Even = lambda No : No % 2 == 0

Ret = Even(12)

if Ret == True:
    print("Even")
else:
    print("Odd")



