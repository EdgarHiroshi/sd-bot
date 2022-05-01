import os
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix='!')

"""     
carrega eventos básicos em manage;
carrega comandos na pasta extensions.
"""

bot.load_extension('manage')
for file in os.listdir('extensions'):
    if file[-3:] == '.py':
        bot.load_extension(f'extensions.{file[:-3]}')

"""
a variável TOKEN está contida no arquivo .env
"""

TOKEN = config("TOKEN")
bot.run(TOKEN)