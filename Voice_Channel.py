import random

from discord import FFmpegPCMAudio
import discord
import os
#Use this to update file_names
def get_filepaths(directory):
    file_names =[]
    for root, directories, files in os.walk(directory):
        for filename in files:
            filename = os.path.join(root, filename)
            file_names.append(filename)
    return file_names
#get_filepaths(r'C:\Users\adria\Desktop\Discord Audio Files')
file_names = ['C:\\Users\\adria\\Desktop\\Discord Audio Files\\android-sound-meme-By-Tuna.mp3', 'C:\\Users\\adria\\Desktop\\Discord Audio Files\\ara-ara-By-Tuna.mp3', 'C:\\Users\\adria\\Desktop\\Discord Audio Files\\bruh-By-Tuna.mp3', 'C:\\Users\\adria\\Desktop\\Discord Audio Files\\ereh-By-Tuna.mp3', 'C:\\Users\\adria\\Desktop\\Discord Audio Files\\fortunate-son-By-Tuna.mp3', 'C:\\Users\\adria\\Desktop\\Discord Audio Files\\stand-up,-father---eren-yeager-By-Tuna.mp3', 'C:\\Users\\adria\\Desktop\\Discord Audio Files\\tatakae-By-Tuna.mp3', 'C:\\Users\\adria\\Desktop\\Discord Audio Files\\yamete-kudasai!-By-Tuna.mp3']






#THIS SAYS IF CONNECTED, none means not connected
def is_connected(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    return (voice_client and voice_client.is_connected())

async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(r'C:\Users\adria\Desktop\Discord Audio Files\bruh-By-Tuna.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You're not even in a voice channel! (;｀O´)o")
#I WANT TO SEPERATE join FUNCT AND THE PART THAT PLAYS AUDIO, so
#so have a join function, then a different function that plays audio
#and can tell if the bot is in a voice channel or not

async def bruh(ctx):
    if (is_connected(ctx) == True):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(r'C:\Users\adria\Desktop\Discord Audio Files\bruh.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You're not even in a voice channel! (;｀O´)o")

async def edward(ctx):
    if (is_connected(ctx) == True):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(r'C:\Users\adria\Desktop\Discord Audio Files\fortunate_son.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You're not even in a voice channel! (;｀O´)o")

async def play(ctx, arg):
    if (is_connected(ctx) == True):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('C:\\Users\\adria\\Desktop\\Discord Audio Files\\' + arg + '.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You're not even in a voice channel! (;｀O´)o")

async def ben(ctx):
    if (is_connected(ctx) == True):
        voices = ['yes','no','ben']
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('C:\\Users\\adria\\Desktop\\Discord Audio Files\\' + random.choice(voices) + '.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You're not even in a voice channel! (;｀O´)o")

async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Ba-bye")
    else:
        await ctx.send("Can't kick me if I'm not in the party ( ˘ ͜ʖ ˘)")
