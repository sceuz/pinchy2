import discord
from discord.ext import commands
import music


cogs = [music]
client = commands.Bot(command_prefix='!?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)
client.run('ODkyODM3OTE0NDIwMDY0MzI5.YVSuGg.PS6wWot2sTbsdTt3pOCbp1GSBxM')
