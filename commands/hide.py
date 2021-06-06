from discord.ext import commands, tasks
import discord
from discord.utils import get

class Hide(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  

  @commands.command()
  @commands.has_role('•━━ Staff ━━•')
  async def hide(self,ctx):
    channel = ctx.channel
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    overwrite.read_messages = False
    await ctx.message.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'** {channel.mention} has been hidden Successfully !**')
    
 




def setup(bot): 
  bot.add_cog(Hide(bot))
