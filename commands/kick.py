from discord.ext import commands, tasks
import discord
class KickCommands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.command()
  @commands.has_role('•━━ Staff ━━•')
  async def kick(self,ctx, member: discord.Member, *, content='No Reason !'):
   try:
    channel = await member.create_dm()

    embed = discord.Embed(title="You have Been kicked ",
                          colour=discord.Colour(0x00ce94))
    embed.set_author(
        name="Dz Otaku ",
        icon_url=
        'https://images-ext-1.discordapp.net/external/eiu0FkO6oEw9VnBetFKA5bYGX3YczOvWzQCgxqSbHfw/%3Fsize%3D1024/https/cdn.discordapp.com/icons/640924227372843039/e6a229fb9ac2143260d73d63ef365f0d.png?width=406&height=406'
    )
    embed.add_field(name="Reason :", value=content)
    embed.set_footer(
        text="Not satisfied with The kick ? \n Contact an admin",
        icon_url=
        'https://images-ext-1.discordapp.net/external/eiu0FkO6oEw9VnBetFKA5bYGX3YczOvWzQCgxqSbHfw/%3Fsize%3D1024/https/cdn.discordapp.com/icons/640924227372843039/e6a229fb9ac2143260d73d63ef365f0d.png?width=406&height=406'
    )
    await channel.send(embed=embed)
   except Exception as e : 
    print(e)



def setup(bot): 
  bot.add_cog(KickCommands(bot))