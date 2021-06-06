from discord.ext import commands, tasks
import discord
import random
class PickCommands(commands.Cog) : 
  def __init__(self,bot):
    self.bot=  bot 
   
  @commands.command()
  async def pick(self,ctx,*,hkm): 
    p = hkm.split(",")
    await ctx.send(f"**I Picked : {random.choice(p)}**")


def setup(bot): 
  bot.add_cog(PickCommands(bot))
