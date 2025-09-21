# VexaAuth 🔐

A Discord bot library that allows users to **verify once globally via OAuth2** and be automatically pulled into servers when the owner runs `.restore`.  

## Features
- Global verification via OAuth2
- Automatically pull authorized users into servers
- Server logs support
- MongoDB storage for users and config
- Commands: `.help`, `.sendverifylink`, `.restore`, `.setlogs`

## Setup
1. Clone this repo
2. Fill in `config.json` with your bot token, client ID/secret, and MongoDB URI
3. Install requirements:
```bash
pip install -r requirements.txt
python -m vexaauth.bot_commands```
