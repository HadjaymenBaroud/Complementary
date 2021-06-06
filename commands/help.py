from discord.ext import commands, tasks
import discord
class HelpCommands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.command()
  async def help(self,ctx,command=None):
    if command==None:
      embed = discord.Embed(title="Commands !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Ban", value='Send a message to the member when he gets Banned ! ')   
      embed.add_field(name="Kick", value='Send a message to the member when he gets Kicked ! ')
      embed.add_field(name="Mute", value='Send a message to the member when he gets Muted ! ')
      embed.add_field(name="Warn", value="Send a message to the member with the warn's reason ! ")
      embed.add_field(name="Hide", value='Hide a channel ! ')
      embed.add_field(name="Unhide", value='Unhide a channel !  ')
      embed.add_field(name="Top", value='Change The Top week roles ! ')
      embed.add_field(name="brod", value='send a message to all the members ! ')
      embed.add_field(name="pick", value='pick a value from a list of values !')
      embed.set_footer(
        text="Type >>help command for more infos ! ")

      
    elif str(command).lower()== 'ban' :
      embed = discord.Embed(title="Commands !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Ban", value='Send a message to the member when he gets Banned ! ')  
      embed.add_field(name="Syntax", value='>>ban [Member] [Reason]')
    elif command.lower()== 'kick' :
      embed = discord.Embed(title="Command !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Kick", value='Send a message to the member when he gets Kicked ! ') 
      embed.add_field(name="Syntax", value='>>kick [Member] [Reason]')
    elif str(command).lower()== 'mute' :
      embed = discord.Embed(title="Command !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Mute", value='Send a message to the member when he gets Muted !! ') 
      embed.add_field(name="Syntax", value='>>mute [Member] [Duration] [Reason]')      
    elif str(command).lower()== 'hide' :
      embed = discord.Embed(title="Command !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Hide", value='Hide a channel ! ')
    elif str(command).lower()== 'unhide' :
      embed = discord.Embed(title="Command !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Unide", value='Unhide a channel ! ')
    elif str(command).lower()== 'unhide' :
      embed = discord.Embed(title="Command !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Unide", value='Unhide a channel ! ')
    elif str(command).lower()== 'top' :
      embed = discord.Embed(title="Command !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Top", value='Change The Top week roles ! ')
      embed.add_field(name="Syntax", value='>>top [type] [members]')
      embed.add_field(name="Reminder !!!", value='t for TopText \n v for TopVoice')
    elif str(command).lower()== 'brod' :
      embed = discord.Embed(title="Command !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Brod", value='send a message to all the members ! ')
      embed.add_field(name="Syntax", value='>>brod [message] ')
    elif str(command).lower()== 'pick' :
      embed = discord.Embed(title="Command !  ",
                          colour=discord.Colour(0x00ce94))
      embed.add_field(name="Pick", value='pick a value from a list of values !')
      embed.add_field(name="Syntax", value='>>pick value1,value2,value3 ')
      embed.add_field(name="Reminded", value='The separator is a comma **,** ')
      
      

    await ctx.send(embed=embed) 


   
    



 
def setup(bot): 
  bot.add_cog(HelpCommands(bot)) 