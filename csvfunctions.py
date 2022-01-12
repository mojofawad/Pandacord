import csv
import discord

def custom_func_get(guild):
    base_string = 'D:\Python\Git\Pandacord\Data\\'
    #guild = guild.name 
    full_name = base_string + guild + '.csv'
    guilddict = {}
    with open(full_name,newline='') as guilddata:
        data = csv.reader(guilddata)
        for row in data:
            command = row[0]
            row.pop(0)
            responses = row
            #print(command,responses)
            guilddict.update({command: responses})

    return guilddict

def custom_func_update(guild):
    base_string = 'D:\Python\Git\Pandacord\Data\\'    



guild = "close mutuals"
guilddict = custom_func_get(guild)
