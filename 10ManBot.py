# link to add bot https://discordapp.com/oauth2/authorize?&client_id=557511023276457994&scope=bot&permissions=8
from discord.ext.commands import Bot
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from userClass import User
from userListClass import UserList

BOT_PREFIX = "?"
TOKEN = 'NTU3NTExMDIzMjc2NDU3OTk0.D3JWTw.UwcR8wNMAwQSGgse46uo7349G3Y'

file1 = open("users.txt","r") 

playerobjectList = UserList()

client = Bot(command_prefix=BOT_PREFIX)


playerobjectList.readFromList("users.txt")


@client.command()
async def move(arg):
    file2 = open("buffer.txt","r+") 
    print("============================================================================")
    print("Running ?move")
    print("============================================================================")
    browser = webdriver.Firefox()
    browser.get(arg)
    browser.refresh()
    timeout = 5
    nav = browser.find_element_by_tag_name("body")
    #print(nav.text)
    print("writing to file")
    file2.write(nav.text)  
    file2.close()                  
    file2 = open("buffer.txt", "r+")
    largelist = []
    for line in file2:
        largelist.append(line)
    #count = 0
    #for i in largelist:
    #    print(count, i)
    #    count = count + 1
    team1 = largelist[7]
    team2 = largelist[11]
    team1_m = []
    team2_m = []
    team1_m.append(largelist[12])
    team1_m.append(largelist[14])
    team1_m.append(largelist[16])
    team1_m.append(largelist[18])
    team1_m.append(largelist[20])
    team2_m.append(largelist[27])
    team2_m.append(largelist[29])  
    team2_m.append(largelist[31])    
    team2_m.append(largelist[33])    
    team2_m.append(largelist[35])
    server = largelist[22]
    cs_map = largelist[23]
    block = "============================================================================\n"
    message = "Server: " + server + "Map: " + cs_map + "\n"
    newmessage = block + message + team1 + "\n" 
    for i in team1_m:
        newmessage += i
    newmessage += "\n"
    newmessage += "VS\n"
    newmessage += "\n"
    newmessage += team2
    newmessage += "\n"
    for i in team2_m:
        newmessage +=i
    newmessage += "\n"
    newmessage += block
    await client.send_message(client.get_channel('618118339415375874'), newmessage)    
    print("============================================================================")
    print("Server: ", server, "Map: ", cs_map)
    print("============================================================================")
    print(team1)
    for i in team1_m:
        print(i)
    print("VS\n")
    print(team2)
    for i in team2_m:
        print(i)
    print("============================================================================")
    file2.close()

@client.command()
async def read():
    file2 = open("users.txt","r+") 
    print("============================================================================")
    print("Running ?read")
    print("============================================================================")
    for server in client.servers:
        for member in server.members:
            print(str(member))
            file2.write(str(member)) 
            file2.write("\n")
    file2.close()

@client.command(pass_context=True)
async def findMe(ctx):
    userid = ctx.message.author.name
    userdis = ctx.message.author.discriminator
    username = str(userid) + "#" + str(userdis)
    if playerobjectList.findPlayer(username) == True:
        user = playerobjectList.getPlayer(username)
        #print(user.getName())
        await client.say(user.getName())


client.run(TOKEN)        
