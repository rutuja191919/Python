#instance variable : Name, Amount, Address, Account_No
#instance method : CreateAccount, DisplayAccountInfo

class BankAccount:
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

def main():
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