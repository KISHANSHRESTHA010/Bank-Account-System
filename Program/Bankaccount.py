from accCreate import *

Kishan = BankAccount(1000,"Kishan")

John = BankAccount(2000,"John")

Kishan.getBalance()
John.getBalance()

Kishan.deposite(5000)

Kishan.withdraw(2000)

Kishan.transfer(2000,John)

Jim=InterestRewardsAcc(1000,"Jim")
Jim.getBalance()
Jim.deposite(100)
Jim.transfer(100,John)

blaze = savingAccount(1000,"Blaze")
blaze.getBalance()
blaze.deposite(100)
blaze.transfer(1000,Kishan)

Kishan.getBalance()