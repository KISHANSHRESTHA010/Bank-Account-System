class BalanceException(Exception):
    pass

class BankAccount:

    def __init__(self,initialAmount,accName):
        self.balance= initialAmount
        self.name= accName

        print(f"Bank Account: '{self.name}' created.\nBank balance: ${self.balance:.2f}\n")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance: .2f} ")

    def deposite(self, amount):
        self.balance = self.balance+amount
        print("\nDeposite complete!")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, Account '{self.name} only has a balance of  ${self.balance: .2f}"
            )

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete. ")
            self.getBalance()

        except BalanceException as error:
            print(f"\n Withdraw Interruped : {error}")

    def transfer(self,amount,account):
        try:
            print("******************\n\nBeginning Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\nTransfer Complete✅\n\n**************")
        except BalanceException as error:
            print(f"\nTransfer interruped❌: {error}")

class InterestRewardsAcc(BankAccount):

    def deposite(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("\nDeposite Complete")
        self.getBalance()

class savingAccount(InterestRewardsAcc):

    def __init__(self,initialAmount,accName):
        super().__init__(initialAmount,accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance = self.balance - (amount+self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"WIthdraw interrupted: {error}")