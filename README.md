# 10 Man Bot

This is my discord bot that reads a Faceit match page and moves discord users according to the 2 teams in the Faceit match.


10ManBot.py is the bot itself and handles all the commands necessary for functioning. There are two classes, userClass.py and userListClass.py. The user class is simply used to store each discord member's details, such as name and ID. The userList class is used to store all instances of User and the manipulation of them during runtime.



<h1>Prefix: '?'</h1>

<h2>Commands:</h2>

<b><i>?move URL</i></b>
- Takes in a URL (assumes it is a faceit match page url)
- Moves members accordingly to each team

<b><i>?read</i></b>
- Updates local file to reflect discord server members

<b><i>?findMe</i></b>
- Shows member what the Bot has about them on file (discord name, faceit name)

<b><i>?findPlayer DiscordUser</i></b>
- Shows an admin what the Bot has about a specific user on file (discord name, faceit name)

<b><i>?addFaceitID ID</i></b>
- Takes in ID (your faceit ID)
- Stores your faceit ID so that you can be moved in the future

<b><i>?addFaceitToUser DiscordID FaceitID</i></b>
- Admin only
- Adds faceitID to other users

<b><i>?removeFaceitID ID</i></b>
- Removes the ID specified

<b><i>?setChannels channel1 channel2</i></b>
- Takes in two channels, channel1 and channel2
- Team1 on match page will use channel1, team2 will use channel2
- Channel name cannot have spaces (May change in the future)

<b><i>?close</i></b>
- Turns off the bot (Admin only)
