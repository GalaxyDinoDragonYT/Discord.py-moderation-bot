# Discord.py-moderation-bot
Made by me for everyone.

# Guide

Clone this github post or the repl found here: https://replit.com/@GalaxyDinoDino/Discordpy-moderation-bot-template

Go to discord developer portal here: https://discord.com/developers
Sign in with discord and go to applications: https://discord.com/developers/applications
Make a new application and add a bot to it.
Copy the token. 
Paste the token where it says TOKEN = '' 

Change the prefix and role names for moderators, admins and clear chat perms.

Put your rules in the Rules list, use \n for a new line.

Change the filtered words, these are delted when they are sent.

Logs channel is broken as of 2/04/2021 but will be fixed soon.

Change Status to what you want the bot's status to be. 

Change server to your server name.

for filtered words just remove the # at the start of each line: 56, 57, 58, 59, 60, 61, 62

Change where it says MUTED ROLE on line 180 to the id of the muted role in your server.

Emojis can be changed by going to https://emojipedia.org and copying an emoji. 

Help command can be changed if you add a command by adding a field or editing the current fields, here is some example code: 

`@client.group(invoke_without_command=True)
async def help(ctx,):
  embed = discord.Embed(title = "Help", description = f"Do {prefix}help <command> for more information on the command.",color = ctx.author.color)

  embed.add_field(name = "Moderation", value = "`kick` , `ban` , `mute`")
  embed.add_field(name = "Misc and fun", value = "`snipe` , `dm` , `ping` , `poll` , `rules` , `help` , `YOUR COMMAND NAME`") 

  await ctx.send(embed=embed)`
  
  If you edit the help command you need to add the following code:
  
  `@help.command()
async def COMMAND NAME(ctx):

  embed = discord.Embed(title = "**COMMAND NAME**", description = "Command description.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "WHO CAN USE IT?")

  embed.add_field(name = "**Usage**", value = f"{prefix}COMMAND NAME")

  await ctx.send(embed=embed)`
  
  If you need more help join our support server: https://discord.gg/Ada7RsHSRj
