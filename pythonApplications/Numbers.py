#Factors3 is the file which import this file

def DisplayFactors(Value):
    i = 1
    print("Factors are : ")
    #for i in range(1,int(Value/2)+1,1)
    while(i <= int(Value/2)):
        if Value % i == 0:
            print(i)
        i = i + 1
