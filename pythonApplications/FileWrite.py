import os

def Write_File(FileName):
    if os.path.exists(FileName):
        print("Enter the data that you want to write in file")
        Data = input()

        fd = open(FileName, "a")
        fd.write(Data)

    else:
        print("File is not exists")
        return

def main():
    print("Enter the name of the file to write")
    name = input()
    Write_File(name)

if __name__ == "__main__":
    main()
