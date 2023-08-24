import os

def Checkfile(FileName):
    if(os.path.exists(FileName)):
        return True
    else:
        return False

def main():
    print("Enter the name of the file")
    name = input()
    bRet = Checkfile(name)
    if bRet == True:
        print("The file is exists")
    else:
        print("The file is not exists")

if __name__ == "__main__":
    main()