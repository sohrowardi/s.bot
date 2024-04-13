import discord
from config import DISCORD_BOT_TOKEN, DISCORD_SERVER_ID, NOTIFICATION_CHANNEL_ID
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello', help='Responds with a greeting.')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

@bot.command(name='echo', help='Repeats your message.')
async def echo(ctx, *, message):
    await ctx.send(message)

bot.run(DISCORD_BOT_TOKEN)
