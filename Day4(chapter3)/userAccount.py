from main import Account #calling account class . teti ta ho class

uName = input("Please enter a name for your account: ")
uPassword = input("Password for the accoun: ")
uBalance = int(input("What is the starting balance of the account: "))

oNewAccount = Account(uName,uPassword,uBalance)
print()
print("succesfull! You accont is created with following attributes: ")
print()
print(oNewAccount.show())