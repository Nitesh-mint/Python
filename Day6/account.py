from main import *

class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self,theName,theStartingBalance,thePassword):
        oAccount = Account(theName,thePassword,theStartingBalance)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        #increment to prepare for the next account to be created
        self.nextAccountNumber += 1
        return newAccountNumber
    #to ask user and call createAccount object .
    def openAccount(self):
        print("*** Opening Account ***")
        userName = input("What is the name for the new user account: ")
        userStartingAmount = int(input("What is the starting balance for this account:" ))
        userPassword = input("What is the passowrd you want to use for this account:")
        userAccountNumber = self.createAccount(userName,userStartingAmount,userPassword)
        print("Your new account number is: ",userAccountNumber)
        print()
    
    def closeAccount(self):
        print("*** Closing Accont ***")
        userAccountNumber = int(input("Please enter your account number: "))
        userPassword = input("Enter the password: ")
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if  theBalance is not None:
            print("You had", theBalance, "in your acount, which is being returned to you.")
            del self.accountsDict[userAccountNumber]
            print("Your account is now closed.")
    
    def balance(self):
        print("*** Geting Balance ***")
        userAccountNumber = int(input("Please enter your account number: "))
        userPassword = input("Please enter your password: ")
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getbalance(userPassword)
        if theBalance is not None:
            print("Your balance is ", theBalance)
    
    def deposit(self):
        print("*** Deposit ***")
        userAccountNumber = int(input("Please enter your account number: "))
        userPassword = input("Please enter your password: ")
        depositAmmount = int(input("Enter the ammount to deposit: "))
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(depositAmmount,userPassword)
        if theBalance is not None:
            print("Your new balance is: ",theBalance)
    
    def show(self):
        print("*** Showing the Account Info ***")
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print("     Account: ", userAccountNumber)
            oAccount.show()

    def withdrawal(self):
        print("*** Withdrwal ***")
        userAccountNumber = int(input("Please enter your account number: "))
        userPassword = input("Please enter the password: ")
        amount = int(input("Enter the amount to withdraw."))
        oAccount = self.accountsDict[userAccountNumber]
        thebalance = oAccount.withdraw(amount,userPassword)
        if thebalance is not None:
            print("Deducting ", amount)
            print("Your new balance is: ", thebalance)

