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

    BankAccount.DisplayKYCInfo()

    print("Name of the bank : ",BankAccount.Bank_Name)
    print("Rate of Interest on Fixed deposit : ",BankAccount.ROI_On_FD)

    BankAccount.DisplayBankInformation()

    User1 = BankAccount()
    User2 = BankAccount()

    print("Creating the first account")
    User1.CreateAccount()

    print("Creating the second account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposit(1000)
    User2.Deposit(2000)

    print("Amount of {} after deposit : {}".format(User1.Name,User1.Amount))
    print("Amount of {} after deposit : {}".format(User2.Name,User2.Amount))

    User1.Withdraw(500)
    User2.Withdraw(1000)

    print("Amount of {} after withdrwal : {}".format(User1.Name,User1.Amount))
    print("Amount of {} after withdrwal : {}".format(User2.Name,User2.Amount))

if __name__ == "__main__":
    main()