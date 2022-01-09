# bonkbot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

leadvar = '>'
EMOJI_NAMES = [":pushpin:", "📌"]


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_raw_reaction_add(reaction):
    print(reaction)
    message_id = reaction.message_id
    channel_id = reaction.channel_id
    channel = client.get_channel(channel_id)
    message = await channel.fetch_message(message_id)

    if message.pinned:
        return
    else:
        for react in message.reactions:
            if (react in EMOJI_NAMES) or (react.emoji in EMOJI_NAMES):
                print('react in list')  # this line is for testing purposes
                await message.pin()
            print(react)

client.run(TOKEN)
