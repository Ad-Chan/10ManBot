from userClass import User
from userListClass import UserList



PL = UserList()

PL.readFromList("users.txt")
PL.printList()
print(PL.findPlayer("Stosh#6394"))
