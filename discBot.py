

from discord_easy_commands import EasyBot
import pyjokes
import discord




token = 'MTA1NTgzMTAzMDkzMTY1MjYwOA.G_NZIx.IuGvMyRear8LqeqNm2IfPkSJqKmkkoO2GvGy50'


joke = pyjokes.get_jokes(language='es', category='all')
intents = discord.Intents.all()
bot = EasyBot(intents = intents)


bot.setCommand('!youtube', 'www.youtube.com')
bot.setCommand('!instagram','syscursos')
bot.setCommand('!chiste', joke)

bot.run(token)
