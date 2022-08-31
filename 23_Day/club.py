#class club

class Club():
    def __init__(self, clubName,maxMembers):
        self.clubName = clubName
        self.maxMembers = maxMembers    
        self.memberList = []

    def addMember(self, name):
        #make sure that there is enought room left.
        if len(self.memberList) < self.maxMembers:
            self.memberList.append(name)
            print("Ok",name,"has been added to the ",self.clubName,"club")
        else:
            print("Sorry there is no room left for the new members.")
    
    def report(self):
        print()
        print("Here are the names of ", len(self.memberList)," members of",self.clubName,"club:")
        for i in self.memberList   :
            print(i)
        print()
