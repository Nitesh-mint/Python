#version 4 with an interactive menu
from main import *

accountsDict ={}
nextAccountNumber = 0

while True:
    print()
    print("Press b to get the balance")
    print("Pess d to make a depost")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all acconts")
    print("Press q to quit")
    print()

    action= input("What do you want to do? ")
    action = action.lower()
    action = action[0] #grab the first letter in case if user types full.
    print()

    if action == 'b':
        print("*** Get Balance ***")
        userAccountNumber = int(input("Please enter your account number: "))
        userAccountPassword = input("Please enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print("Your balance is:",theBalance)
    elif action == 'd':
        print("*** Deposit ***")
        userAccountNumber = int(input("Please enter your account number: "))
        userAccountPassword = input("Please enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        theDepost = int(input("Enter the amount to depost."))
        theBalance = oAccount.deposit(userAccountNumber,userAccountPassword)
        if theBalance is not None:
             print("Ypur new balance is: ",theBalance)
    elif action == 'o':
        print("*** Open Account ***")
        userName = input("Please enter your name: ")
        userStartingAmmount = int(input("What is the starting balance for this account?"))
        userAccountPassword = input("Please enter a new password for the account: ")
        oAccount = Account(userName,userAccountPassword,userStartingAmmount)
        accountsDict[nextAccountNumber] = oAccount
        print("Your new account number is: ",nextAccountNumber)
        nextAccountNumber += 1
        print()

    elif action == 'w':
        print("*** Withdrawl ***")
        userAccountNumber = int(input("Please enter your account number: "))
        userAccountPassword = input("Please enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        userWithdrawAmmount = int(input("Please enter the amount to witdraw:"))
        theBalance = oAccount.withdraw(userWithdrawAmmount,userAccountPassword)
        if theBalance is not None:
            print("Your new balance is :", theBalance)
        else:
            print("Sorry that was not a vaild action. Please try again.")
    elif action == 's':
        print("*** Showing Your Bank Details ****")
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print("     Account Number:",userAccountNumber)
            oAccount.show()
    elif action == 'q':
        break
