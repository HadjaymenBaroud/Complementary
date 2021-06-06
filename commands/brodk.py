from discord.ext import commands, tasks
import discord
 

class BrodCommands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def brod(self,ctx, *, message):
        
          members =  ctx.guild.members
          successfulcounter = 0
          badcounter = 0
          for member in members:
             
            try:
               
              await member.send(f'**{message}**')
              await ctx.send('sent to {}'.format(member.mention))
              successfulcounter += 1   
            except Exception as e:
                print(e)
                badcounter +=1
          await ctx.send(f'**sent to {successfulcounter} Members ** ')
          await ctx.send(f'** not sent to {badcounter} Members ** ')
        


def setup(bot): 
  bot.add_cog(BrodCommands(bot))