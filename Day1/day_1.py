'''1)simple bank account data:
    create(an account)
    deposit
    withdraw
    check balance
2) what we need to create a simple account:
    customer name
    passsowrd
    balance'''

#single account without functions

accountName = 'Nitesh'
accountBalance = 10000
accountPassword = '9898'

while True:
    print("Press b to get the balance")
    print("Press d to make a deposite")
    print("Press w to make a withdrawl")
    print("press s to show the account")
    print("press q to quit\n")

    action = input("What do you want to do ?")
    action = action.lower()
    action = action[0] #for using frist letter only

    if action == 'b':
        print("Get Balance:")
        userPassword = input("Please enter the password:")
        if userPassword != accountPassword:
            print("The password is incorrect.")
        else:
            print("Your balance is:",accountBalance,'\n')
    elif action == 'd':
        print("Depost:")
        userDepositAmount = input("Please enter amount to deposite:")
        userDepositAmount  = int(userDepositAmount)
        userPassword = input("Please enter the password:")
        
        
        if userDepositAmount < 0:
            print("You cannot deposit a negative amount!")

        elif userPassword!= accountPassword:
            print("The password is incorrect.")
        else:
            accountBalance = accountBalance + userDepositAmount
            print("Your new balance is:",accountBalance)

    elif action =='s':
        print("Show:")
        print(" Name: ", accountName)
        print(" Balance: ", accountBalance)
        print(" Password: ", accountPassword)
    elif action == 'q':
        break

    elif action == 'w':
        print("withdrawl:")

        userWithdrawlAmount = input("Please enter the amount to withdraw")
        userWithdrawlAmount = int(userWithdrawlAmount)
        userPassword = input("Please enter the password:")

        if userWithdrawlAmount < 0:
            print("Cannot withdrawl a negative amount.")

        elif userPassword != accountPassword:
            print("The password is incorrect.")
        elif userWithdrawlAmount > accountBalance:
            print("You cannot withdrawl the money more than you have.")

        else:
            accountBalance = accountBalance - userWithdrawlAmount
            print("Your new balance is:",accountBalance)
    print("Done")