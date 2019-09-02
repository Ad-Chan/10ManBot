from userClass import User
import csv

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


    def readFromList(self):
        openfile = open('users.csv')
        csv_f = csv.reader(openfile)
        for row in csv_f:
            username = row[0].strip()
            newUser = User(username)
            try:
                newUser.setFaceit = row[1].strip()            
            except:
                print(username + " has no faceit id on file") 
            self.addPlayer(newUser)
        openfile.close()
