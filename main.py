import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from apikeys import *

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")

@client.command(pass_context = True)
async def ted(ctx):
    await ctx.send("I fucked Ted")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel, join one and try again")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I'm not in a voice channel, you can change that by typing !join")

@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Nothing is playing currently")

@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Nothing is paused at the moment")

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    voice.stop()

@client.command(pass_context = True)
async def play(ctx, arg):
    if (arg == 'ted'):
        source = FFmpegPCMAudio("ted.mp3")
    elif (arg == 'dad'):
        source = FFmpegPCMAudio("dad.mp3")
    elif (arg == 'hank'):
        source = FFmpegPCMAudio("hank.mp3")
    elif (arg == ""):
        await ctx.send("Invalid name try ted, dad, or hank")
    voice = ctx.guild.voice_client
    player = voice.play(source)





client.run(BOTTOKEN)