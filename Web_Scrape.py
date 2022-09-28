import discord
import pandas as pd
import numpy as np
import io
import asyncio
import matplotlib.pyplot as plt

async def vulgar (ctx):
    # for easy database-ing for user output
    id_content = {}
    id_name_score = {}
    id_name_badwords = {}

    # adding each user who typed to id_content and what they typed + initializing id_name_score for each new id
    async for message in ctx.channel.history(limit=500):
        if (message.author.bot == False):
            if message.author.id in id_content:
                id_content[message.author.id].append(message.content.lower())
            else:
                id_content.setdefault(message.author.id, [message.content])
                id_name_score[message.author.id] = [message.author.name, 0]
                id_name_badwords[message.author.id] = [message.author.name, ""]

    print(id_name_score)  # keeping different dictionaries with same key is very helpful!

    # LIST PROCEEDING THIS COMMENT HAS SLURS BECAUSE THOSE ARE BAD WORDS, all lower case
    with open('bad-words.txt') as f:
        bad_words = f.read().splitlines()
    del bad_words[0]  # empty string in list at beggining

    for key in id_content:  # for person in dictionary
        for content in id_content[key]:  # for message in values of dictionary
            for word in content.split():
                if word in bad_words:  # need to count every word in content
                    id_name_score[key][1] = id_name_score[key][1] + 1
                    id_name_badwords[key][1] = id_name_badwords[key][1] + ' ' + word

    await ctx.send('Need to buy soap for: \n' +
                   str([id_name_score[id] for id in id_name_score]) +
                   '\n Words to clean with soap:\n' +
                   str([id_name_badwords[id] for id in id_name_badwords]) +
                   '\n')

    # end goal: have each distinct name with a long line of things sent, proabably dictionary format so no duplicate names {name:said}
    # send table#
    vulgar_df = pd.DataFrame(id_name_score)
    print(vulgar_df.T)
    await ctx.send(vulgar_df.T)

    # piechart#
    vulgar_df_pie = vulgar_df.T
    scores = vulgar_df_pie.iloc[:, 1].tolist()

    total_scores = sum(scores)
    percent_scores = scores
    for i in range(len(scores)):
        percent_scores[i] = (scores[i] / total_scores) * 100
    print(percent_scores)
    vulgar_df_pie.iloc[:, 1] = percent_scores

    vulgar_df_pie.rename({0: "Names", 1: "Percent"})
    vulgar_df_pie = vulgar_df_pie.sort_values(vulgar_df_pie.columns[1])
    print(vulgar_df_pie)

    # Initialize IO
    data_stream_pie = io.BytesIO()

    # make graph
    plt.pie(vulgar_df_pie.iloc[:, 1], labels=vulgar_df_pie.iloc[:, 0], explode=vulgar_df_pie.iloc[:, 1] / 100)

    # save content into data stream
    plt.savefig(data_stream_pie, format='png', bbox_inches="tight", dpi=80)
    plt.close()
    data_stream_pie.seek(0)
    chart = discord.File(data_stream_pie, filename="vulgar_df_pie.png")

    # send pie chart and clear data stream
    await ctx.send(file=chart)
    data_stream_pie.seek(0)
    data_stream_pie.truncate()

    #Box Plot for server#

    #Initialize IO
    data_stream_box = io.BytesIO()

    #make box plot
    vulgar_df_box= vulgar_df.T
    plt.boxplot(vulgar_df_box.iloc[:,1])

    #save content into data stream
    plt.savefig(data_stream_box, format='png', bbox_inches="tight",dpi=80)
    plt.close()
    data_stream_box.seek(0)
    chart= discord.File(data_stream_box, filename='vulgar_df_box.png')

    #send box plot and clear data stream
    await ctx.send(file=chart)
    data_stream_box.seek(0)
    data_stream_box.truncate()
    await ctx.send("Listen up Shinji, this is a box plot.\n"
                   "The middle bar is the median, the box stretches to the 1st and 3rd quantiles, and the lines at the bottom and top are the maximum and minimum any one of us cursed-- ya got that? ")