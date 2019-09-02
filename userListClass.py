from userClass import User

class UserList:

    def __init__(self):
        self.list = []


    def findPlayer(self, username):
        for i in self.list:
            #if (i.getName() == "Stosh#6394"):
                #print("true")
            if i.getName() == username:
                #print("true")
                return True
        return False

    def getPlayer(self, username):
        for i in self.list:
            if i.getName() == username:
                return i

    def addPlayer(self, player):
        if self.findPlayer(player.getName()) == False:
            self.list.append(player)

    def removePlayer(self, player):
        self.list.remove(player)


    def printList(self):
        for i in self.list:
            print(type(i.getName()))
            print(i.getName())        


    def readFromList(self, userfile):
        openfile = open(userfile, "r")
        for line in openfile:
            username = line.strip()
            newUser = User(username)
            self.addPlayer(newUser)
        openfile.close()
