def CreateFile(FileName):
    fd = open(FileName, "w")

def main():
    print("Enter the name of the file to create")
    name = input()
    CreateFile(name)

if __name__ == "__main__":
    main()
