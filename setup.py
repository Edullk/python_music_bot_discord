import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix = "/", case_insensitive = True, intents=intents)

client.remove_command('help')

print("PRONTO PARA USAR")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('OTAxNjE4NTc0NTg0NTgyMTU0.YXSfuw.ak7HfXnfli27B-Vs6STg0oouGGY')