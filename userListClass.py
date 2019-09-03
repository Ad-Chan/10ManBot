from userClass import User
import csv
import os

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

    def getPlayerFaceit(self, faceitID):
        for i in self.list:
            #print(i.getFaceit())
            if i.getFaceit() == faceitID:
                return i

    def addPlayer(self, player):
        self.list.append(player)

    def removePlayer(self, player):
        self.list.remove(player)


    def printList(self):
        for i in self.list:
            print(type(i.getName()))
            print(i.getName())   
            print(type(i.getFaceit()))
            print(i.getFaceit())     

    def addFaceitToList(self, player):
        with open("../users.csv", "r") as openfile:
            csv_r = csv.reader(openfile)            
            lines = list(csv_r)
        openfile.close()
        newrow = [player.getName(), player.getFaceit(), player.getdiscordID()]
        count = -1
        for row in lines:
            count = count + 1
            username = row[0].strip()      
            if username == player.getName():
                lines[count] = newrow
                print(lines)
                break 
        openwrite = open("../temp.csv", 'w+')
        csv_w = csv.writer(openwrite)
        for row in lines:          
            csv_w.writerow(row)
        openwrite.close()
                        

    def readFromList(self):
        openfile = open('../users.csv')
        csv_f = csv.reader(openfile)
        for row in csv_f:
            username = row[0].strip()
            newUser = User(username)
            try:
                newUser.setFaceit(row[1].strip())
                newUser.setdiscordID(row[2].strip())
                #print(row[1].strip())
                #print("set faceit user" + username + newUser.getFaceit() + newUser.getdiscordID())        
            except:
                pass
            self.addPlayer(newUser)
        openfile.close()

