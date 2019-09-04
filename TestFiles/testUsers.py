from userClass import User
from userListClass import UserList



PL = UserList()

PL.readFromList()
PL.printList()
print(PL.findPlayer("Stosh#6394"))

user = PL.getPlayerFaceit("Stosh")
print(user.getFaceit())

print(user.getName())
