#Help command example.

@client.group(invoke_without_command=True)
async def help(ctx,):
   embed = discord.Embed(title = "Help", description = f"Do {prefix}help <command> for more information on the command.",color = ctx.author.color)

  embed.add_field(name = "Moderation", value = "`kick` , `ban` , `mute`")
  embed.add_field(name = "Misc and fun", value = "`snipe` , `dm` , `ping` , `poll` , `rules` , `help` , `COMMAND NAME`)

  await ctx.send(embed=embed)
                  

#HELP COMMAND EDIT
                  
@help.command()
async def help(ctx):

  embed = discord.Embed(title = "**Name**", description = "Description of command.", color = ctx.author.color)

  embed.add_field(name = "Permission level", value = "Who uses")

  embed.add_field(name = "**Usage**", value = f"{prefix}Name")

  await ctx.send(embed=embed)
