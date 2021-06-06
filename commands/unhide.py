from discord.ext import commands, tasks
import discord

class UnHide(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  @commands.has_role('•━━ Staff ━━•')
  
  async def unhide(self,ctx):
   channel = ctx.channel
   overwrites = discord.PermissionOverwrite()
   overwrites.send_messages = True
   overwrites.read_messages = True
   await ctx.message.channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
   await ctx.send(f'** {channel.mention} has been Unhidden Successfully !**')




def setup(bot): 
  bot.add_cog(UnHide(bot))