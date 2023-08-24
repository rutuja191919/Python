import os

def ReadFile(FileName):
    if(os.path.exists(FileName)):
        fd = open(FileName, 'r')
        Data = fd.read()
        print("Data from the file : ",Data)
        fd.close()

    else:
        print("The file is not exists")
        return

def main():
    print("Enter the name of the file to create")
    name = input()
    ReadFile(name)

if __name__ == "__main__":
    main()
