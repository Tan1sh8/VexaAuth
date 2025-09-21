VexaAuth 🔐

VexaAuth is a Discord bot that allows users to verify globally via OAuth2 and be automatically pulled into servers when the owner runs .restore.
All user data is stored securely in MongoDB Cloud (Atlas).


---

Features

Global verification via OAuth2

Automatically pull authorized users into servers (.restore)

Server logs support (.setlogs)

MongoDB Cloud storage for users and server config

Commands: .help, .sendverifylink, .restore, .setlogs



---

Requirements

Python 3.9 or higher

A Discord bot token

Discord application client ID and secret

MongoDB Atlas account (free tier works)



---

Setup Instructions

1️⃣ Fork or Download Repo

Clone or fork the repository:

git clone https://github.com/YourUsername/VexaAuth.git
cd VexaAuth


---

2️⃣ Create MongoDB Atlas Database

1. Go to MongoDB Atlas.
2. Create a free cluster.
3. Create a database named vexaauth.
4. Create a database user with username and password.
5. Copy the connection string (URI), e.g.:



mongodb+srv://<username>:<password>@cluster0.mongodb.net/vexa?retryWrites=true&w=majority

Replace <username> and <password> with your credentials.


---

3️⃣ Configure config.json

Fill in your bot and database details:

{
    "token": "YOUR_BOT_TOKEN",
    "owner_id": 1234567890,
    "client_id": "DISCORD_CLIENT_ID",
    "client_secret": "DISCORD_CLIENT_SECRET",
    "redirect_uri": "YOUR_REDIRECT_URI",
    "mongo_uri": "mongodb+srv://<username>:<password>@cluster0.mongodb.net/vexa?retryWrites=true&w=majority"
}

token → your bot token

owner_id → your Discord user ID

client_id / client_secret → from your Discord application

redirect_uri → a valid redirect URI configured in your Discord app (used for OAuth2)

mongo_uri → MongoDB Atlas URI



---

4️⃣ Install Dependencies

pip install -r requirements.txt

Dependencies include:

discord.py>=2.4.0

pymongo>=4.9.0



---

5️⃣ Run the Bot

python -m vexaauth.bot_commands

The bot will now connect to Discord and MongoDB Atlas.


---

# Commands

Command	Description

.help	Shows all available commands
.sendverifylink #channel	Posts an OAuth2 verification link in the specified channel
.restore	Pulls all globally authorized users into the current server
.setlogs #channel	Sets a channel to send restoration logs



---

# User Flow

1. Admin runs .sendverifylink in a channel.


2. Users click the OAuth2 link and authorize the bot.


3. Their Discord ID and OAuth2 token are stored in MongoDB Atlas.


4. When the owner runs .restore, all authorized users are automatically added to the server.






# Notes

Ensure your bot has the Manage Guild and Add Members permissions.

Users authorize once globally; no need to reverify for other servers.

You can optionally add a .setlogs channel to monitor restores.
