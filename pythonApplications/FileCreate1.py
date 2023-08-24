import os

def CreateFile(FileName):
    if(os.path.exists(FileName)):
        print("File is already exists")
        return
    else:
        fd = open(FileName, "w")        #if already exists then that data gets overwrite by this function

def main():
    print("Enter the name of the file to create")
    name = input()
    CreateFile(name)

if __name__ == "__main__":
    main()
