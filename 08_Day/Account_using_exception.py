#error indicated by raise statement
class AbortTransaction(Exception):
    pass

class Account():
    def __init__(self,name,balance,password):
        self.name = name
        self.balance = balance
        self.password = password

    def validateAmount(self,amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction("Amount must be an Integer")

        if amount < 0:
            raise AbortTransaction("Amount must be Positive.")
        
        return amount
    
    def checkPassword(self,password):
        if password != self.password:
            raise AbortTransaction("Your password is incorrect.")
        
    def deposit(self,amountToDeposit):
        self.amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.amountToDeposit + self.balance
        return self.balance

    def getBalance(self):
        return self.balance

    def withdrawl(self, amountToWithdraw):
        self.amountToWithdraw = self.validateAmount(amountToWithdraw)
        self.balance = self.balance - self.amountToWithdraw
        return self.balance
    
    #for debugging
    def show(self):
        print()
        print("        name: ",self.name)
        print("        balance:",self.balance)
        print("        password",self.password)


oNitesh = Account("nitesh",900,"n")
print(oNitesh.show())