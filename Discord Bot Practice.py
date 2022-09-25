import discord as ds

client= ds.Client()

#functions triggered by client event
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'hewwo c-can i \*sweats\* hewp you, {0.author.name}'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('!bot'):
        await message.channel.send("HEWWO")

@client.event
async def on_ready():
    print('wogged in as')
    print(client.user)
    print(client.user.id)
    print('weady at youw sewvice o7')
    print("~~~~~")

client.run('OTk3NTg1MTM2NTQ5OTA0NDc1.GlX9J4.CibdeL7FUZd32DjfA1kr9O7cxHXptKp-bXvlTo')