import os

def Write_File(FileName):
    if os.path.exists(FileName):
        fd = open(FileName, "r")
        Data = fd.read()
        print("Data from the file is : ")
        print(Data)
        fd.close()

    else:
        print("File is not exists")
        return

def main():
    print("Enter the name of the file to write")
    name = input()
    Write_File(name)

if __name__ == "__main__":
    main()
