def Frequency(FileName, Str):
    fd = open(FileName, 'r')
    Data = fd.read()
    return Data.count(Str)

def main():
    print("Enter the file name")
    FileName = input()
    print("Enter the string")
    str = input()
    iRet = Frequency(FileName,str)
    print("The frequency of the string in file is : ",iRet)

if __name__ == "__main__":
    main()