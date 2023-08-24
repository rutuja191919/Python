import os

def DeleteFile(FileName):
    if os.path.exists(FileName):
        size = os.path.getsize(FileName)
        if(size == 0):
            os.remove(FileName)
            print("File deleted successfully")
        else:
            print("Are you sure to delete the file? Y/N")
            option = input()
            if(option == 'Y' or option == 'y'):
                os.remove(FileName)
                print("File deleted successfully")
            else:
                print("File deletion process stopped")

    else:
        print("File is not exists")
        return

def main():
    print("Enter the file name to delete")
    name = input()
    DeleteFile(name)

if __name__ == "__main__":
    main()
