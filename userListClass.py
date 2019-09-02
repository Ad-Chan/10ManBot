from userClass import User
import csv

class UserList:

    def __init__(self):
        self.list = []


    def findPlayer(self, username):
        for i in self.list:
            if i.getName() == username:
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

    def addFaceitToList(self, player):
        with open("users.csv", "r") as openfile:
            csv_r = csv.reader(openfile)            
            lines = list(csv_r)
        openfile.close()
        newrow = [player.getName(), player.getFaceit()]
        count = -1
        for row in lines:
            count = count + 1
            username = row[0].strip()      
            if username == player.getName():
                lines[count] = newrow
                print(lines)
                break 
        with open("write.csv", 'wb') as openwrite:
            csv_w = csv.writer(openwrite)
            csv_w.writerows(lines)
        openwrite.close()
                        

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
