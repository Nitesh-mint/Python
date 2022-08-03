'''Creating multiple global varaibles works but it is not a good practice.
so we are sotring all the account we created in a list.'''

from multiprocessing.spawn import old_main_modules
from main import *
#for storing all the accounts.
accountsList = []

#create two accounts
oAccount = Account("Susil","sus", 9000)
accountsList.append(oAccount)
print("Susil account number is 0.")
accountsList[0].show()

print()

oAccount  = Account("sunil","sun", 8989)
accountsList.append(oAccount)
print("Sunil account number is 1")

accountsList[1].show()
print()

#calling some methos on the different accounts
print("calling methods of the two accounts.....")
accountsList[0].deposit(100,'sus')
accountsList[1].withdraw(300,'sun')
accountsList[1].deposit(400,'sun')
accountsList[0].show()
accountsList[1].show() 