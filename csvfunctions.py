import csv
import discord
import random

# imports the local csv file
def custom_func_get(guild):
    base_string = 'D:\Python\Git\Pandacord\Data\\'
    guild = guild.name 
    full_name = base_string + guild + '.csv'
    print(full_name)
    guilddict = {}
    with open(full_name,newline='') as guilddata:
        data = csv.reader(guilddata)
        for row in data:
            command = row[0]
            row.pop(0)
            responses = row
            guilddict.update({command: responses})

    guilddata.close()
    return guilddict



# Updates the local csv file w/ the new commands
def custom_func_update(guild):
    base_string = 'D:\Python\Git\Pandacord\Data\\'    
