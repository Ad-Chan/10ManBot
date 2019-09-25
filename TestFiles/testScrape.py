import discord

from discord.ext import commands
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from userClass import User
from userListClass import UserList
from selenium.webdriver.firefox.options import Options
import shutil


options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get("https://www.faceit.com/en/csgo/room/1-9ff89488-3cf6-47b0-9120-86015bb4e81b")
#browser.refresh()
#timeout = 5
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
bannedWords = ["SHARE", "WATCH DEMO", "GO TO HUB", "Download client", "CREATE ACCOUNT", "LOGIN", "CS:GO 5V5", "OVERVIEW", "SCOREBOARD", "VIDEOS", "READY", "TIME TO CONNECT", "FACEIT use cookies to ensure you get the best experience online!", "I UNDERSTAND"]
team1_m = []
team2_m = []
team1 = ""
team2 = ""
count = 0
count2 = 0
matchMap = ""
for i in largelist:
    if i.strip() not in bannedWords:
        if (len(matchMap) > 0) & (count2 < 5):
            count2 = count2 + 1
            team2_m.append(i.strip())
        if (len(team1) > 0) & (len(team2) > 0) & (count < 5):
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

print("Team1:\n")
for i in team1_m:
    print(i)
print("Team2:\n")
for i in team2_m:
    print(i)

print(matchMap)
print(team1)
print(team2)

file2.close()
