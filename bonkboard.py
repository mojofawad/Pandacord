    # Bonkboard iterates through messages and returns a semisorted list of users and their bonks. Has a selection of bonk emotes (maybe should just check for the text bonk)
    # List needs to be sorted largest to smallest, and needs brackets removed
    # If not from closemutuals, return null
    # Also needs to have separate handling for args like alltime (csv), days, etc.

from discord import guild,channel
import time
from datetime import date, datetime
from dateutil import relativedelta
import os

async def bonk_history(timearg,panda):
    closemoots = panda.get_guild(881855141077213185) # needs to be updated to control for close mutuals
    messages = []
    # The classic bonkboard command, whoever has the most bonks in the last 100 messages
    if timearg == None:
        for channels in closemoots.channels:
            if str(channels.type) == 'text':
                try:
                    temp = await channels.history(limit=100).flatten()
                    messages.append(temp)
                except:
                    continue
            else:
                continue
        return messages
    # This really should be stored in a csv for referencing. Well, it should check for a csv, if there is none create it. Then update it, return top 10 bonkers
    elif timearg == 'all time':
        for channels in closemoots.channels:
            if str(channels.type) == 'text':
                temp = await channels.history().flatten()
                messages.append(temp)
            else:
                continue
        return messages
    # This is the time based bonker modelled after the yagpdb reminder command, i.e. 7d, 6h etc. Doesn't function atm
    else:
        past_date = time_parser(timearg)
        for channels in closemoots.channels:
            if str(channels.type) == 'text':
               temp = await channels.history(after=past_date)
               messages.append(temp)
            else:
                continue   
        return messages

            
def time_parser(timearg):
    if timearg.count(' ') >4:
        ParseError = True
        return  ParseError
    arg = []
    days = 0
    hours = 0
    months = 0
    weeknos = 0    
    arg = timearg.split(' ')
    for i in arg:
    
        if i.find('d') >=0:
            days = int(i.strip('d'))
        elif i.find('h') >=0:
            hours = int(i.strip('h'))
        elif i.find('m') >=0:
            months = int(i.strip('m'))
        elif i.find('w') >=0:
            weeknos = int(i.strip('w'))

    timedif = relativedelta.relativedelta(day=days,month=months,hour=hours,weeks=weeknos)
    today = datetime.now()
    history = today-timedif
    return history