from re import L
from Bank import * 

oAccount = Bank()

niteshAccountNumber = oAccount.createAccount("Nitesh",900,"ioio")
print(niteshAccountNumber)

JohnAccountNumber = oAccount.createAccount("John",80,"i")
print(JohnAccountNumber)

while True:
    print()
    print("Press b to get the balance")
    print("Pess d to make a depost")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all acconts")
    print("Press c to close account")
    print("Press q to quit")
    print()

    action = input("What do you want to do: ")
    action = action[0].lower()
    
    if action == 'b':
        oAccount.balance()
    
    elif action == 'd':
        oAccount.deposit()

    elif action == 'o':
        oAccount.openAccount()

    elif action == 'w':
        oAccount.withdrawal()

    elif action == 's':
        oAccount.show()
    
    elif action == 'c':
        oAccount.closeAccount()

    elif action == 'q':
        break

    else:
        print("sorry not a valid option.")