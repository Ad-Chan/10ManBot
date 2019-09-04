import discord

from discord.ext import commands
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from userClass import User
from userListClass import UserList
import shutil

BOT_PREFIX = "?"

getToken = open("../discordtoken.txt", "r")

TOKEN = getToken.readline().strip()

file1 = open("../users.txt","r") 

playerobjectList = UserList()

client = commands.Bot(command_prefix=BOT_PREFIX)


playerobjectList.readFromList()


def findUser(player):
    for server in client.servers:
        for member in server.members:
            if member.id == player.strip():
                print("FOUND MEMBER " + member.name)
                return member


@client.command(pass_context=True)
async def move(ctx, arg):
    file2 = open("buffer.txt","r+") 
    print("Running ?move")
    browser = webdriver.Firefox()
    browser.get(str(arg))
    #browser.refresh()
    #timeout = 5
    nav = browser.find_element_by_tag_name("body")
    print("writing to file")
    file2.write(nav.text)  
    file2.close()                  
    file2 = open("buffer.txt", "r+")
    largelist = []
    for line in file2:
        largelist.append(line)

    maps = ["de_overpass", "de_inferno", "de_dust2", "de_cache", "de_vertigo", "de_mirage", "de_train", "de_cbble", "de_nuke"]
    team1_m = []
    team2_m = []
    team1 = ""
    team2 = ""
    count = 0
    count2 = 0
    matchMap = ""
    for i in largelist:
        if (len(matchMap) > 0) & (count2 < 10):
            count2 = count2 + 1
            team2_m.append(i.strip())
        if (len(team1) > 0) & (len(team2) > 0) & (count < 10):
            count = count + 1
            team1_m.append(i.strip())
        if "TEAM" in i:
            if len(team1) <= 0:
                team1 = i.strip()
            else:
                if len(team2) <= 0:
                    team2 = i.strip()
        if "de_" in i:
            for j in maps:
                if i.strip() == j:  
                    matchMap = i.strip()
    channelread = open("channel.txt", "r")
    channel1 = channelread.readline()
    channel2 = channelread.readline()
    channelread.close()
    channelOne = ""
    channelTwo = ""
    for server in client.servers:
        for channel in server.channels:
            if channel.name.strip() == channel1.strip():
                channelOne = channel

    for server in client.servers:
        for channel in server.channels:
            if channel.name.strip() == channel2.strip():
                channelTwo = channel
    
    await client.say("Moving")

    for i in team1_m:    
        team1player = playerobjectList.getPlayerFaceit(i.strip())
        if isinstance(team1player, User): 
            team1member = findUser(team1player.getdiscordID())
            await client.move_member(team1member, channelOne)

    
    for i in team2_m:
        team2player = playerobjectList.getPlayerFaceit(i.strip())
        if isinstance(team2player, User):
            team2member = findUser(team2player.getdiscordID())
            await client.move_member(team2member, channelTwo)
    browser.close()
    file2.close()

@client.command()
async def read():
    if ctx.message.author.server_permissions.administrator:
        file2 = open("../users.txt","r+") 
        print("Running ?read")
        for server in client.servers:
            for member in server.members:
                print(str(member))
                file2.write(str(member)) 
                file2.write("\n")
        file2.close()
    else:
        await client.say("You need to be an administrator!")        

@client.command(pass_context=True)
async def findMe(ctx):
    userid = ctx.message.author.name
    userdis = ctx.message.author.discriminator
    username = str(userid) + "#" + str(userdis)
    if playerobjectList.findPlayer(username) == True:
        user = playerobjectList.getPlayer(username)
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
    if ctx.message.author.server_permissions.administrator:
        await client.say("Saving Data") 
        playerobjectList.updateList()
        try:
            shutil.move("../temp.csv", "../users.csv")  
        except:
            pass
        await client.say("Turning off bot")   
        exit()
    else:
        await client.say("You need to be an administrator!")

#@client.command(pass_context=True)
#async def help(ctx):
    

client.run(TOKEN)        
