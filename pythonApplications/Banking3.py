#instance variable : Name, Amount, Address, Account_No
#instance method : CreateAccount, DisplayAccountInfo
#class variable : BankName, ROI_On_FD
#class method : DisplayBankingInformation

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

    def DisplayAccountInfo(self):
        print("--------------Your account information is as below---------")
        print("Name of the Account Holder : ",self.Name)
        print("Account Number : ",self.AccountNo)
        print("Address of Account Holder : ",self.Address)
        print("Current Amount in account : ",self.Amount)
        print()

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to the banking console")
        print("Bank Name : ",cls.Bank_Name)
        print("Rate of Interest on Fixed Deposit : ",cls.ROI_On_FD)

def main():

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

if __name__ == "__main__":
    main()