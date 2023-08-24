class BankAccount:
    ROI  = 10.5

    def __init__(self,Name,Account):
        self.Name = Name
        self.Account = Account

    def Display(self):
        print("Name : ",self.Name, " Account : ",self.Account)

    def Deposit(self, Value):
        self.Account = self.Account+Value

    def Withdraw(self, Value):
        self.Account = self.Account + Value

    def CalculateInterest(self):
        interest = (self.Account * BankAccount.ROI)/100
        return interest

def main():
    Obj1 = BankAccount("Rutuja Chaudhari",10000)
    Obj1.Deposit(5000)
    Obj1.Withdraw(1000)
    Obj1.Display()
    print("Interest is : ",Obj1.CalculateInterest())

    Obj2 = BankAccount("Aarti More", 20000)
    Obj2.Deposit(10000)
    Obj2.Withdraw(5000)
    Obj2.Display()
    print("Interest is : ", Obj2.CalculateInterest())

if __name__ == "__main__":
    main()