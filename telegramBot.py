from twitchio.ext import commands

bot = commands.Bot(
    irc_token = 'oauth:lj374iqbdcicw7e4u42w8y7jyor6fw',
    client_id = 'xz5i1gursaam6acar7bv1vj0wgcpdd',
    nick = 'syslasigb',
    prefix = '!',
    initial_channels = ['syslasigb']

)


@bot.event
async def event_ready():
    print('Estamos listos')


@bot.command(name='horario')
async def horario(ctx):
    await ctx.send(f'Buenas, {ctx.author.name} mi horario es X')

@bot.event
async def event_message(ctx):

    await bot.handle_commands(ctx)

    if 'crack' == ctx.content.lower():
        await ctx.channel.send(f'Tu si quieres un crack {ctx.author.name}')

bot.run()
