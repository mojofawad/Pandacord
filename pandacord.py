import discord
import os
from dotenv import load_dotenv
import random
from discord import HTTPException


load_dotenv()
token = os.getenv('Discord_token')
close_mutuals = os.getenv('close_moots')
daddycord = os.getenv('daddycord')


leadvar = '>'
EMOJI_NAMES = ["pin", "📌"]

panda = discord.Client()

@panda.event
async def on_ready():
    for guild in panda.guilds:
        if guild.name == daddycord: # or guild.name == close_mutuals:
            break

    print(
        f'{panda.user} has entered the swimming pool!:\n'
        f'{guild.name}(id: {guild.id})\n'
        )

# Panda Gifer
@panda.event
async def on_message(message):
    if message.author == panda.user:
        return
    
    pangif = [
        'https://c.tenor.com/2XHTM3NHQfYAAAAC/panda-jjk.gif',
        'Panda is not a Panda',
        'https://c.tenor.com/gmvdv-e1EhcAAAAC/weliton-amogos.gif'
        'https://c.tenor.com/ZiNqSxHmdIYAAAAC/jjk-jujutsu-kaisen.gif',
        'https://c.tenor.com/YDionZwapW4AAAAC/jjk-lazy.gif',
        'https://media3.giphy.com/media/N6funLtVsHW0g/giphy.gif?cid=ecf05e47oy0ihuz5qzbrdflupwb28sk98dfnwc2j8hrc5nou&rid=giphy.gif&ct=g',
        'https://media3.giphy.com/media/EPcvhM28ER9XW/giphy.gif?cid=ecf05e47oy0ihuz5qzbrdflupwb28sk98dfnwc2j8hrc5nou&rid=giphy.gif&ct=g',
        'https://media.tenor.co/videos/6c5f4ceb9199e579fe690b4df0050747/mp4'
    ]
    
    message.content = message.content.lower()
    message.content = message.content.replace('.', "")
    message.content = message.content.replace("'", "")
    # >panda
    if message.content.startswith(leadvar+'panda'):
        response = random.choice(pangif)
        await message.channel.send(response)

    # >ignose    
    if message.content.startswith(leadvar+'ignose'):
        await message.channel.send('a white powder')
    elif message.content == 'raise-exception':
        raise discord.DiscordException
 
    # >geo
    if message.content.startswith(leadvar+'geo'):
        if message.author.id == '244858804863238144':
            await message.channel.send('Are you really trying to bonk yourself Geo? Go to Horny Jail')
        else:
            # await message.channel.send('<:bonk:896886830622965820>')
            k = random.randrange(1,3)
            if k == 1:
                await message.channel.send('https://cdn.discordapp.com/emojis/896886830622965820.png?size=96')
                print(k)
            else:
                await message.channel.send('Geo is important and worthy of love <:people_hugging:928020730384359525>')
                print(k)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


    # >imran
    if message.content.startswith(leadvar+'imran'):
        await message.channel.send('https://cdn.discordapp.com/attachments/881855141656006699/928035535077916702/20220104_072745.jpg')

    # >mel
    melo = [
    'https://media.discordapp.net/attachments/881855141656006699/928029399989768193/Screenshot_20220104-043443.jpg',
    'https://cdn.discordapp.com/attachments/881855141656006699/929716909279174677/Screenshot_20220109-074250.jpg',
    'https://cdn.discordapp.com/attachments/881855141656006699/929739942664482836/unknown.png',
    'https://cdn.discordapp.com/attachments/881855141656006699/929740142099431424/unknown.png',
    'https://cdn.discordapp.com/attachments/881855141656006699/930052640870641704/unknown.png'
    ]

    if message.content.startswith(leadvar+'hermajesty'):
        k = random.randrange(0,len(melo))
        await message.channel.send(melo[k])
    if message.content.startswith(leadvar+'theirmajesty'):
        k = random.randrange(0,len(melo))
        await message.channel.send(melo[k])
    
    # >reese
    reese = [
    'https://cdn.discordapp.com/attachments/881855141656006699/928037187054874624/Therapy_costs_money_shitposting_is_free.png',
    'resident catgirl',
    '<:pained:930055983160524840>',
    'https://www.youtube.com/watch?v=XVekJTmtwqM'
    ]
    if message.content.startswith(leadvar+'reese'):
        j = random.randrange(0,len(reese))
        await message.channel.send(reese[j])
    
    # >nico
    nico = [
        '<@&919998459795361822>',
        'I am a child',
        'read unorthodox marxism',
        'parecon solves this'
    ]
    if message.content.startswith(leadvar+'nico'):
        j = random.randrange(0,len(nico))
        await message.channel.send(nico[j])

    # >kimik
    if message.content.startswith(leadvar+'kimik'):
        z = random.randrange(1,3)
        if z == 1:
            await message.channel.send('https://i.redd.it/3bsmt7wh3m611.jpg')
        else:
            await message.channel.send('fuck you too')
  
    # >corb
    if message.content.startswith(leadvar+'corb'):
        await message.channel.send('https://i.kym-cdn.com/photos/images/newsfeed/002/255/820/79a.jpg')        
    
    # >waifu
    if message.content.startswith(leadvar+'waifu'):
        if random.randrange(1,2) == 1:
            await message.channel.send('https://c.tenor.com/xMUclj_Bn9AAAAAC/jujutsu-kaisen-anime.gif')
        # else:
            # await message.channel.send('https://media4.giphy.com/media/862A6X2sooSsw/giphy.gif?cid=ecf05e47u1pxr0t8k0xcp6ldqnfctilojn8hwtt5clamodls&rid=giphy.gif&ct=g')
            
    # >lucky
    if message.content.startswith(leadvar+'lucky'):
        await message.channel.send('A certified cool guy')
    
    # >ginge
    if message.content.startswith(leadvar+'ginge'):
        if random.randrange(1,3) == 1:
            await message.channel.send('https://c.tenor.com/Nu5y6fiL9cEAAAAd/reigen-arataka-drinking.gif')
        else:
            await message.channel.send('https://www.youtube.com/watch?v=es9-P1SOeHU')    
    
    # >zoomy
    zoomy = [
    'Fuckin\' Brits',
    'GDP is lies and hornswoggle',
    'Neoclassical economics is horoscopes and witchcraft',
    'Oi you wanker, ah u havin\' a gaggle? Ay\'ll baight ur fookin\' legs off',
    ]
    if message.content.startswith(leadvar+'zoomy'):
        j = random.randrange(0,len(zoomy))
        await message.channel.send(zoomy[j])

    # >cass
    if message.content.startswith(leadvar+'cass'):
        await message.channel.send('https://www.ikea.com/de/de/p/blahaj-stoffspielzeug-hai-30373588/')
    # Functional Responses
    # imvegan

    if message.content.find('im vegan') >= 0:
        vegan = [
            'But where do you get your protein?',
            'Oh me too! I only eat meat on Thursdays!',
            'Oh I could never be vegan, where would I get my B12?',
            'So that means you eat fish right?'
        ]
        t = random.randrange(0,len(vegan))
        await message.channel.send(vegan[t])
    

    # >dakota will likely need some sort of gif return
    # if message.content.startswith(leadvar+'dakota'):
        # await message.channel.send()
    #if message.content.startswith(leadvar+'bonkcount'):



@panda.event       
async def on_raw_reaction_add(reaction):
    # print(reaction)
    message_id = reaction.message_id
    # print(type(message_id))
    channel_id = reaction.channel_id
    channel = panda.get_channel(channel_id)
    message = await channel.fetch_message(message_id)
    
    if message.pinned:
                return
    try:
        reaction = next(x for x in message.reactions if (isinstance(x.emoji, str) and str(x.emoji) in EMOJI_NAMES) or (not isinstance(x.emoji, str)and x.emoji.name in EMOJI_NAMES))
        if reaction.count >= 5:
            try:
                await message.pin()
            except HTTPException:  # This most likely means we reached max pins
                pins = await channel.pins()
                oldest_pin = pins.pop()
                await oldest_pin.unpin()
                await message.pin()
    except Exception:
        pass

panda.run(token)