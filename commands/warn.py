from discord.ext import commands, tasks
import discord
class WarnCommand (commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.command()
  @commands.has_role('•━━ Staff ━━•')
  async def warn(self,ctx, member: discord.Member, *, reason=None):
     
     
    if member.id == ctx.author.id:
      await ctx.send("**You Can't Warn Yourself ! **")
    else: 
     if  member.top_role >= ctx.author.top_role   :
       await ctx.send(f" **You Can't Warn {member.mention} !**")
     else : 
      try:
         if reason == None:
             await ctx.send('⛔ **Pls Speciefy a Reason !**')
         else:
            channel = await member.create_dm()
            embed = discord.Embed(title="You have Been Warned ",
                                            colour=discord.Colour        (0x00ce94))
            embed.set_author(
                name="Dz Otaku ",
                icon_url=
                'https://images-ext-1.discordapp.net/external/eiu0FkO6oEw9VnBetFKA5bYGX3YczOvWzQCgxqSbHfw/%3Fsize%3D1024/https/cdn.discordapp.com/icons/640924227372843039/e6a229fb9ac2143260d73d63ef365f0d.png?width=406&height=406'
            )
            embed.add_field(name='Reason : ', value=reason)
            embed.set_footer(
                text="Dz Otaku",
                icon_url=
                'https://images-ext-1.discordapp.net/external/eiu0FkO6oEw9VnBetFKA5bYGX3YczOvWzQCgxqSbHfw/%3Fsize%3D1024/https/cdn.discordapp.com/icons/640924227372843039/e6a229fb9ac2143260d73d63ef365f0d.png?width=406&height=406'
            )

            await channel.send(embed=embed)
            await ctx.send(f'✅ **{member.mention}  Warned Successfully !**')
      except:
         await ctx.send('**raw ghal9 privih 😡**')


def setup(bot): 
  bot.add_cog(WarnCommand(bot))