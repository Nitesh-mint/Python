#creating a bank account class:
''' *account name
    *passowrd for the account
    *user can deposit money
    *user can withdraw money'''



class Account():
    def __init__(self,name,password,balance):
        self.name = name
        self.password = password
        self.balance = int(balance)

    def deposit(self,dAmount,password):
            if password != self.password: #mathi ko pass sanga you pass milcha?
                print("Sorry the password is incorrect")
                return None
            if dAmount < 0:
                print("Cannot deposite negative amount")
                return None
            self.balance = self.balance + dAmount
    
    def withdraw(self,wAmount,password):
        if password != self.password:
            print("Sorry the password is incorrect")
            return None
        if wAmount < 0 :
            print("Cannot withdraw negativ balance.")
            return None
        if wAmount > self.balance:
            print("Cannot withdraw amount more than on your account")
            return None
        self.balance = self.balance - wAmount

    def getbalance(self,password):
        if password != self.password:
            print("Sorry the password is incorrect.")
            return None
        return self.balance
    #added for debugging
    def show(self):
        print("     Account: ",self.name)
        print("     Password: ",self.password)
        print("     Balance: ",self.balance)
        print()
        