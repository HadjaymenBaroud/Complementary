from discord.ext import commands, tasks
import discord
class VoiceCommand(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.command()
  async def join(self,ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
  @commands.command()
  async def leave(ctx):
    await ctx.voice_client.disconnect()



def setup(bot): 
  bot.add_cog(VoiceCommand(bot))