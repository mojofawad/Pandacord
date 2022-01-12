import discord
import os
from dotenv import load_dotenv
import random
from discord import HTTPException
from tqdm import tqdm
import json

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
        'https://media.tenor.co/videos/6c5f4ceb9199e579fe690b4df0050747/mp4',
        'https://tenor.com/view/busy-panda-run-busy-panda-busy-person-gif-23478514'
    ]
    
    message.content = message.content.lower()
    message.content = message.content.replace('.', "")
    message.content = message.content.replace("'", "")
    # >panda
    if message.content.startswith(leadvar+'panda'):
        response = random.choice(pangif)
        await message.channel.send(response)

    # >ignose
    ignose = [
        'papa ignose',
        'One must imagine Sisyphus happy',
        'The boulder is heavy',
        'ACAB',
        'Abolish the state'
    ]
    if message.content.startswith(leadvar+'ignose'):
        l = random.randrange(0,len(ignose))
        await message.channel.send(ignose[l])
    elif message.content == 'raise-exception':
        raise discord.DiscordException
 
    # >geo
    if message.content.startswith(leadvar+'geo'):
        geo = [
            'https://cdn.discordapp.com/emojis/896886830622965820.png?size=96',
            'Geo is important and worthy of love <:people_hugging:928020730384359525>',
            'We all believe in you Geo',
            'Certified Not a Simp'
        ]
        if message.author.id == '244858804863238144':
            await message.channel.send('Are you really trying to bonk yourself Geo? Go to Horny Jail')
        else:
            # await message.channel.send('<:bonk:896886830622965820>')
            k = random.randrange(0,len(geo))
            await message.channel.send(geo[k])
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
    kimik = [
        'https://i.redd.it/3bsmt7wh3m611.jpg',
        'fuck you too',
        'Tu rationalise tes echecs par le contexte, c\'est un biais classique'
    ]
    if message.content.startswith(leadvar+'kimik'):
        z = random.randrange(0,len(kimik))
        await message.channel.send(kimik[z])

  
    # >corb
    if message.content.startswith(leadvar+'corb'):
        await message.channel.send('https://i.kym-cdn.com/photos/images/newsfeed/002/255/820/79a.jpg')        
    
    # >waifu
    waifu = [
        'https://c.tenor.com/xMUclj_Bn9AAAAAC/jujutsu-kaisen-anime.gif',
        '"Knowing how to be solitary is central to the art of loving. When we can be alone, we can be with others without using them as a means of escape."',
        'Fuck Covid',
        'Fuck Joe Biden',
        'The democrats are corrupt and impotent.',
        'The rising tide of fascism will doom us all, and the only political party able to stand in its way prefers to squabble amongst itself and hand Trump or DeSantis the 2024 presidency.',
        'Climate Change has stolen the future from us all, and we are only able to watch its immense propensity with limp torpor.',
        'https://cdn.discordapp.com/attachments/753748113294098542/930728310932127774/gude-tiring-wow.png https://cdn.discordapp.com/attachments/753748113294098542/930728311355756554/gudetama-in-shell.png'
    ]
    if message.content.startswith(leadvar+'waifu'):
        j = random.randrange(1,len(waifu))
        await message.channel.send(waifu[j])
            
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
    'https://youtu.be/3bYRCTS7eBU'
    ]
    if message.content.startswith(leadvar+'zoomy'):
        j = random.randrange(0,len(zoomy))
        await message.channel.send(zoomy[j])

    # >pecun
    pecun = [
        'I love veblen almost obsessively',
        'https://discord.com/channels/881855141077213185/881856105070866442/929801848464998421',
        'There is a required consumption which escalates with the pecuniary standard.',
    ]
    if message.content.startswith(leadvar+'pecun'):
        j = random.randrange(0,len(pecun))
        await message.channel.send(pecun[j])

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
    
    # Bonkboard iterates through messages and 
    if message.content.startswith(leadvar+'bonkboard'):
        bonk = ['<:bonk:896886830622965820>','<:BONK:718289967155118130>','<:bonk:930818372831174656>']
        bonkboard = {}
        closemoots = panda.get_guild(881855141077213185)
        messagechannel = message.channel
        for channels in closemoots.channels:
            try:
                messages = await channels.history(limit=100).flatten()
                for message in messages:
                    for react in message.reactions:
                        if str(react) in bonk:
                            try: 
                                temp = bonkboard[message.author.name] + react.count
                                bonkboard.update({message.author.name: temp})
                            except:
                                bonkboard[message.author.name] = react.count
                        else:
                            continue
            except AttributeError:
                continue
            except:
                continue
        prettybonkboard =json.dumps(bonkboard, indent=4)
        await messagechannel.send(prettybonkboard)




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