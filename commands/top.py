import discord 
from discord.ext import commands,tasks  
from discord.utils import get
class TopCommand(commands.Cog):
  def __init__(self,bot):
    self.bot = bot 
  @commands.command() 
  @commands.has_role('VIP Respo')  
  async def top(self,ctx ,typee,*member :discord.Member):
    VoiceKeys = ['voice','v','vc']
    TextKeys = ['text','t','txt']
    if typee.lower() in VoiceKeys :
        VipVoice = get(ctx.guild.roles, name='VIP ☆彡(Voice)')
    
        for i in VipVoice.members :
          await i.remove_roles(VipVoice)
        for m in member :
          await m.add_roles(VipVoice)
          await ctx.send('**✅ VIP ☆彡(Voice) Added Successfully ! **  {}'.format(m.mention))
    if typee.lower() in TextKeys :
      VipText = get(ctx.guild.roles, id=780543595202609172)
   
      for i in VipText.members :
     
          await i.remove_roles(VipText)
      
      for m in member :
     
        await m.add_roles(VipText)
        await ctx.send('✅ **VIP ☆彡(Text) Added Successfully {}**'.format(m.mention))


def setup(bot): 
  bot.add_cog(TopCommand(bot))