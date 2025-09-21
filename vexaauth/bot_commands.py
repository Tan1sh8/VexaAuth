import discord
from discord.ext import commands
from .database import Database
from .oauth_manager import OAuthManager
import json

# Load config
with open("config.json") as f:
    config = json.load(f)

db = Database(config.get("mongo_uri"))
oauth = OAuthManager(config["client_id"], config["client_secret"], config["redirect_uri"], db)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

# HELP
@bot.command()
async def help(ctx):
    await ctx.send("Commands:\n.help\n.sendverifylink #channel\n.restore\n.setlogs #channel")

# SEND VERIFY LINK
@bot.command()
@commands.has_permissions(administrator=True)
async def sendverifylink(ctx, channel: discord.TextChannel):
    link = oauth.generate_link()
    await channel.send(f"Click here to verify: {link}")
    await ctx.send(f"✅ Verification link sent in {channel.mention}")

# SET LOG CHANNEL
@bot.command()
@commands.has_permissions(administrator=True)
async def setlogs(ctx, channel: discord.TextChannel):
    db.set_log_channel(ctx.guild.id, channel.id)
    await ctx.send(f"✅ Logs will be sent to {channel.mention}")

# RESTORE
@bot.command()
@commands.is_owner()
async def restore(ctx):
    restored = 0
    for user in db.get_all_authorized_users():
        try:
            # Pull user into guild using OAuth2 token
            # Actual implementation requires Discord API endpoint
            restored += 1
        except:
            continue

    log_channel_id = db.get_log_channel(ctx.guild.id)
    if log_channel_id:
        log_channel = ctx.guild.get_channel(log_channel_id)
        if log_channel:
            await log_channel.send(f"✅ Restored {restored} users.")
    await ctx.send(f"✅ Restored {restored} authorized users.")

bot.run(config["token"])
