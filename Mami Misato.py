import random
import discord
from discord import Game
from discord.ext.commands import Bot
import requests
import json
import pandas as pd

import Voice_Channel
from Voice_Channel import *
from discord import FFmpegPCMAudio
import asyncio

intents = discord.Intents.default()
intents.members = True

BOT_PREFIX = ("?", "!")
TOKEN = 'OTk3NTg1MTM2NTQ5OTA0NDc1.GlX9J4.CibdeL7FUZd32DjfA1kr9O7cxHXptKp-bXvlTo'

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
                aliases = ['bad_mouth','needs_soap','vulgar'])
async def retrieve_messages(ctx):
    messages = await ctx.channel.history(limit=500).flatten()

    id_content = {}
    id_name_score={}

    for message in messages:
        if (message.author.bot == False):
            if message.author.id in id_content:
                id_content[message.author.id].append(message.content.lower())
            else:
                id_content.setdefault(message.author.id,[message.content])
                id_name_score[message.author.id] = [message.author.name,0]

    print(id_content.keys())
    print(id_name_score) #keeping different dictionaries with same key is very helpful!

    #LIST PROCEEDING THIS COMMENT HAS SLURS BECAUSE THOSE ARE BAD WORDS, all lower case
    with open('bad-words.txt') as f:
        bad_words = f.read().splitlines()
    del bad_words[0] #empty string in list at beggining
    print(bad_words)

    print(id_content)
    print(id_name_score)
    for key in id_content:                        #for person in dictionary
        for content in id_content[key]:          #for message in values of dictionary
            for word in content.split():
                if word in bad_words:            #need to count every word in content
                    id_name_score[key][1] = id_name_score[key][1]+1
    await ctx.send('Need to buy soap for: \n' +
                   str(id_name_score))

            #go through said_only and match names, if no matching names then add new dictionary
            #once matched or name made, add content to dictionary name
    #end goal: have each distinct name with a long line of things sent, proabably dictionary format so no duplicate names {name:said}



#make list of each message, append content to each one
    #d_col = {'name':[]}
    #df = pd.DataFrame()
    #print(len(messages))
    #print(messages)
    #i have list of messages, now i need to suck out author name(by name or by id#) and message content
    #for i in messages
###############

client.run(TOKEN)
