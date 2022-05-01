from discord.ext import commands
from math import sqrt

class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def calc(self, ctx, *args):
        resposta = eval(''.join(args))
        await ctx.send('Resposta: ' + str(resposta))
    
    @commands.command()
    async def raiz(self, ctx, arg):
        resposta = sqrt(int(arg))
        await ctx.send('Resposta: ' + str(resposta))


def setup(bot):
    bot.add_cog(Math(bot))
    print('Loaded math.py')