from main import * 

accountsDict = {}
nextAccountNumber = 0

#creating two accounts
oAccount = Account("nitesh","nit",8000)
NiteshAccountNumber = nextAccountNumber
accountsDict[NiteshAccountNumber] = oAccount
print("Account number of Nitesh is:",NiteshAccountNumber)
nextAccountNumber = nextAccountNumber + 1
accountsDict[NiteshAccountNumber].show()


oAccount = Account("Ritika","Rit",9000)
RitikaAccountNumber = nextAccountNumber
accountsDict[RitikaAccountNumber] = oAccount
print("Account number for Ritika is:",RitikaAccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountsDict[RitikaAccountNumber].show()