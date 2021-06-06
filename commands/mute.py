from discord.ext import commands, tasks
import discord
class MuteCommands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.command()
  @commands.has_role('•━━ Staff ━━•')
  async def mute(self,ctx,
               member: discord.Member,
               dur='No Duration specefied',
               *,
               content='No Reason !'):

    channel = await member.create_dm()

    embed = discord.Embed(title="You have Been muted ",
                           colour=discord.Colour(0x00ce94))
    embed.set_author(
        name="Dz Otaku ",
        icon_url=
        'https://images-ext-1.discordapp.net/external/eiu0FkO6oEw9VnBetFKA5bYGX3YczOvWzQCgxqSbHfw/%3Fsize%3D1024/https/cdn.discordapp.com/icons/640924227372843039/e6a229fb9ac2143260d73d63ef365f0d.png?width=406&height=406'
    )
    embed.add_field(name="Duration :", value=dur)
    embed.add_field(name="Reason :", value=content)
    embed.add_field(name="Support :", value='<#799677983099060244>')
    embed.set_footer(
        text="Not satisfied with The mute ? \n Open  a Ticket",
        icon_url=
        'https://images-ext-1.discordapp.net/external/eiu0FkO6oEw9VnBetFKA5bYGX3YczOvWzQCgxqSbHfw/%3Fsize%3D1024/https/cdn.discordapp.com/icons/640924227372843039/e6a229fb9ac2143260d73d63ef365f0d.png?width=406&height=406'
    )
    await channel.send(embed=embed)
    await ctx.send(f'✅ Successfully muted **{member}** for **{dur}**')




def setup(bot): 
  bot.add_cog(MuteCommands(bot))