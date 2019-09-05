class User:

    def __init__(self, name):
        self.name = name
        self.faceitID = " "
        self.discordID = " "

    
    def getName(self):
        return self.name


    def setName(self, name):
        self.name = str(name)


    def getFaceit(self):
        return self.faceitID


    def setFaceit(self, faceitID):
        self.faceitID = faceitID
    

    def getdiscordID(self):
        return self.discordID



    def setdiscordID(self, discordID):
        self.discordID = discordID
