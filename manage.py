from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound

class Manage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')

    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f'{ctx.author}: "{ctx.message.content}" ({ctx.channel})')

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(f'Responded to {ctx.author}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print("Invalid command or command usage.")
        await ctx.send("Erro ao processar comando:")
        if isinstance(error, CommandNotFound):
            await ctx.send("Comando inexistente.(digite !ajuda)")
        else:
            await ctx.send("Argumento(s) inválido(s).")
    
    @commands.command()
    async def ajuda(self, ctx):
        await ctx.send("Comandos: ajuda, calc, raiz.")

def setup(bot):
    bot.add_cog(Manage(bot))
    print('Loaded manage.py')