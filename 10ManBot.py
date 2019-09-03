# link to add bot https://discordapp.com/oauth2/authorize?&client_id=557511023276457994&scope=bot&permissions=8
import discord

from discord.ext import commands
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from userClass import User
from userListClass import UserList
import shutil

BOT_PREFIX = "?"

getToken = open("../../discordtoken.txt", "r")

TOKEN = getToken.readline().strip()

file1 = open("users.txt","r") 

playerobjectList = UserList()

client = commands.Bot(command_prefix=BOT_PREFIX)


playerobjectList.readFromList()


def findUser(player):
    for server in client.servers:
        for member in server.members:
            if member.id == player.strip():
                print("FOUND MEMBER")
                return member


@client.command(pass_context=True)
async def move(ctx, arg):
    file2 = open("buffer.txt","r+") 
    print("============================================================================")
    print("Running ?move")
    print("============================================================================")
    browser = webdriver.Firefox()
    browser.get(str(arg))
    #browser.refresh()
    #timeout = 5
    nav = browser.find_element_by_tag_name("body")
    #print(nav.text)
    print("writing to file")
    file2.write(nav.text)  
    file2.close()                  
    file2 = open("buffer.txt", "r+")
    largelist = []
    for line in file2:
        largelist.append(line)
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
    await client.say(newmessage) 
    channelread = open("channel.txt", "r")
    
    channel1 = channelread.readline()
    channel2 = channelread.readline()
    channelread.close()
    channelOne = ""
    channelTwo = ""
    for server in client.servers:
        for channel in server.channels:
            #print(channel.name + " " + channel1)
            if channel.name.strip() == channel1.strip():
                #print("true")
                channelOne = channel

    for server in client.servers:
        for channel in server.channels:
            print(channel.name)
            if channel.name == channel2:
                channelTwo = channel
    
    for i in team1_m:    
        team1player = playerobjectList.getPlayerFaceit(i.strip())
        if isinstance(team1player, User): 
            print(channelOne)
            print(team1player.getdiscordID())
            team1member = findUser(team1player.getdiscordID())
            #team1member = await client.get_user_info(team1player.getdiscordID())
            print(team1member)
            await client.move_member(team1member, channelOne)
            #await team1member.move_to(channelOne)

    
    for i in team2_m:
        team2player = playerobjectList.getPlayerFaceit(i.strip())
        if isinstance(team2player, User):
            team2member = findUser(team2player.getdiscordID())
            #team1member = await client.get_user_info(team2player.getdiscordID())
            await client.move_member(team2member, channelTwo)
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
        message = "Discord username on file: " + user.getName() + "\n" + "FaceitID on file: " + user.getFaceit()  
        await client.say(message)

@client.command(pass_context=True)
async def setFaceitID(ctx, faceitID):
    userid = ctx.message.author.name
    userdis = ctx.message.author.discriminator
    username = str(userid) + "#" + str(userdis)
    if playerobjectList.findPlayer(username) == True:
        user = playerobjectList.getPlayer(username)
        user.setFaceit(faceitID)
        user.setdiscordID(ctx.message.author.id)
        playerobjectList.addFaceitToList(user)
        message2 = "Your faceitID is now set to " + user.getFaceit()
        await client.say(message2)

@client.command(pass_context=True)
async def setChannels(ctx, team1, team2):
    channel1 = team1
    channel2 = team2
    channelfile = open("channel.txt", "w+")
    channelfile.writelines(team1)
    channelfile.writelines("\n")
    channelfile.writelines(team2)
    channelfile.flush()
    channelfile.close()
    adoptChannel()


@client.command(pass_context=True)
async def close(ctx):
    await client.say("Saving Data")
    try:
        shutil.move("temp.csv", "users.csv")  
    except:
        pass
    await client.say("Turning off bot")   
    exit()

client.run(TOKEN)        
