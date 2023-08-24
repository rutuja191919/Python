#instance variable : Name, Amount, Address, Account_No
#instance method : CreateAccount, DisplayAccountInfo
#class variable : BankName, ROI_On_FD
#class method : DisplayBankingInformation
#static method : DisplayKYCInfo

class BankAccount:
    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0.0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name")
        self.Name = input()

        print("Enter the amount")
        self.Amount = float(input())

        print("Enter your address")
        self.Address = input()

        print("Enter your account no")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):       #self keyword : Instance method
        print("--------------Your account information is as below---------")
        print("Name of the Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in account : ",self.Amount)
        print()

    @classmethod        #use decorator compulsory
    def DisplayBankInformation(cls):    #cls keyword : class method
        print("Welcome to the banking console")
        print("Bank Name : ",cls.Bank_Name)
        print("Rate of Interest on Fixed Deposit : ",cls.ROI_On_FD)

    @staticmethod       #static method with no parameters
    def DisplayKYCInfo():
        print("Please consider below KYC information : ")
        print("According to the rules of Government of India you have to submit below documents")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of Adhaar Card")
        print("3 : Photo of PAN Card")

    def Deposit(self,Value):
        self.Amount = self.Amount + Value

    def Withdraw(self,Value):
        self.Amount = self.Amount - Value

def main():
    print("----------------------------------------------------------------")
    print("---------- Banking Application ----------")
    print("----------------------------------------------------------------")
    print("---------- Calling Static method to display KYC info ---------- ")
    BankAccount.DisplayKYCInfo()

    print("----------------------------------------------------------------")
    print("---------- Accessing the class variables from main ----------")
    print("----------------------------------------------------------------")
    print("Name of bank : ", BankAccount.Bank_Name)
    print("Rate of Intrest on Fixed deposit : ", BankAccount.ROI_On_FD)

    print("----------------------------------------------------------------")
    print("---------- Calling the class method to display Bank informatrion ----------")
    print("----------------------------------------------------------------")
    BankAccount.DisplayBankInformation()

    print("----------------------------------------------------------------")
    print("---------- Creating the objects of class ----------")
    print("----------------------------------------------------------------")
    User1 = BankAccount()
    User2 = BankAccount()

    print("----------------------------------------------------------------")
    print("Createing the first account")
    print("----------------------------------------------------------------")

    print("----------------------------------------------------------------")
    print("---------- Enter details for first account holder ----------")
    print("----------------------------------------------------------------")
    User1.CreateAccount()

    print("----------------------------------------------------------------")
    print("Createing the second account")
    print("----------------------------------------------------------------")

    print("----------------------------------------------------------------")
    print("---------- Enter details for second account holder ----------")
    User2.CreateAccount()
    print("----------------------------------------------------------------")

    print("---------- Calling instance method to display information of first account ----------")
    User1.DisplayAccountInfo()

    print("---------- Calling instance method to display information of second account ----------")
    User2.DisplayAccountInfo()

    print("---------- Depositing 500 in User1 ----------")
    User1.Deposit(500)
    print("---------- Depositing 1200 in User2 ----------")
    User2.Deposit(1200)

    print("Amount of {} after deposit is {}: ".format(User1.Name, User1.Amount))
    print("Amount of {} after deposit is {}: ".format(User2.Name, User2.Amount))

    print("---------- Withdraw 200 in User1 ----------")
    User1.Withdraw(200)

    print("---------- Withdraw 3000 in User2 ----------")
    User2.Withdraw(3000)

    print("Amount of {} after withdraw is {}: ".format(User1.Name, User1.Amount))
    print("Amount of {} after withdraw is {}: ".format(User2.Name, User2.Amount))

    print("----------------------------------------------------------------")
    print("---------- End of banking appplication ----------")
    print("----------------------------------------------------------------")

if __name__ == "__main__":
    main()