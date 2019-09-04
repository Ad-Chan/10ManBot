import discord

from discord.ext import commands
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from userClass import User
from userListClass import UserList
import shutil



browser = webdriver.Firefox()
browser.get("https://www.faceit.com/en/csgo/room/1-5ed64fb4-2c72-4e99-8c5b-c57bd41b409f")
browser.refresh()
timeout = 5
nav = browser.find_element_by_tag_name("body")
file2 = open("buffer2.txt","r+") 
print("writing to file")
file2.write(nav.text)  
file2.close()  
file2 = open("buffer2.txt", "r+")
largelist = []
for line in file2:
    print
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
            #print(i)
            team1 = i.strip()
        else:
            if len(team2) <= 0:
                #print(i)
                team2 = i.strip()
    if "de_" in i:
        for j in maps:
            if i.strip() == j:  
                matchMap = i.strip()

for i in team1_m:
    print(i)

for i in team2_m:
    print(i)

print(matchMap)
print(team1)
print(team2)

file2.close()
