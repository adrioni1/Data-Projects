import io
import random
import discord
from discord import Game
from discord.ext.commands import Bot
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import Voice_Channel
import Web_Scrape
from Voice_Channel import *
from discord import FFmpegPCMAudio
import asyncio



intents = discord.Intents.all()
intents.members = True

BOT_PREFIX = ("?", "!")
import secure
TOKEN = secure.token

client = Bot(command_prefix = BOT_PREFIX, intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="beer pong w shinji"))
    print('wogged in as')
    print(client.user)
    print(client.user.id)
    print('weady at youw sewvice o7')
    print("~~~~~")


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    channel = client.get_channel(channel.id)
    emb = discord.Embed(title = "NEW MEMBER", description= f"Thanks {member.mention} for joining! ヽ༼ ・ ل͜ ・ ༽ﾉ")
    await channel.send(embed=emb)

@client.command()
async def hello(message):
    if message.author == client.user:
        return
    msg = 'GET IN THE ROBOT '+ str.upper('{0.author.name}'.format(message))
    await message.channel.send(msg)

#async def list_servers():
#    await client.wait_until_ready()
#    while not client.is_closed():
#        print("Currently eating at:")
#        for server in client.guilds:
#            print(server.name)
#        await asyncio.sleep(6)
#
#client.loop.create_task(list_servers())
#############################

@client.command(name='8ball',
                description = "Shakes an eight ball",
                brief = "Helps you decide your fate",
                aliases = ['eight_ball', 'eightball', "8-ball"])
async def eight_ball(ctx):
    possible_responses = [
        "That is a resounding no",
        "Doubtful :(",
        "Ask again ;)",
        "Maybe if you try hard enough :)",
        "Definitely"
    ]
    await ctx.send(random.choice(possible_responses)+", " + ctx.message.author.mention)

@client.command(aliases = ['bitties','bitys'],
                description = 'Tells you current bitcoin price',
                brief= ' buy btc dip')
async def bitcoin(ctx):
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send("Bitcoin price is $"+value+'\nThat\'s '+ str(round(float(value.replace(',',''))/1.68,2))+ ' hot n spicy mcchickens')

#VOICE CHANNEL#
@client.command(aliases = ['joinvc'],
                pass_context = True)
async def join(ctx):
    await Voice_Channel.join(ctx)

@client.command(aliases = ['mario','bro','Mario'],
                pass_context= True)
async def bruh(ctx):
    await Voice_Channel.bruh(ctx)

@client.command(aliases = ['bean','army'],
                pass_context = True)
async def edward(ctx):
    await Voice_Channel.edward(ctx)

@client.command(pass_context = True)
async def play(ctx, arg):
    await Voice_Channel.play(ctx, arg)

@client.command(pass_context = True)
async def ben(ctx):
    await Voice_Channel.ben(ctx)

@client.command(aliases = ['leavevc','kickvc', 'dora','boots'],
                pass_context =True)
async def leave(ctx):
    await Voice_Channel.leave(ctx)
###############

#WEB SCRAPE#
@client.command(pass_context=True,
                aliases = ['vulgar_pie','bad_mouth','needs_soap','retrieve_messages'])
async def vulgar(ctx):
    await Web_Scrape.vulgar(ctx)








###############

client.run(TOKEN)
