import csv
from http.client import responses
import os




full_name = ''
guilddict = {}

# imports the local csv file, returning it for the custom variable function to search
# This might need a try block to handle empty rows if they show up in the csv. Would go before command = row[0]
def custom_func_get(guild):
    #script_dir = os.path.dirname(__file__)
    guild = guild.name + '.csv'
    guild = os.path.normpath(guild)
    full_name = os.path.join('Data',guild)
    #full_name = 'D:\Python\Git\Pandacord\Data\close mutuals.csv'
    with open(full_name,newline='') as guilddata:
        data = csv.reader(guilddata)
        for row in data:
            command = row[0]
            row.pop(0)
            responses = row
            guilddict.update({command: responses})

    guilddata.close()
    return guilddict



# Updates the local csv file w/ the new commands. Copies data from the old csv, adds the new data, then returns the updated object, which is then written to csv.
def custom_func_update(guild,arg2,arg3):
    #script_dir = os.path.dirname(__file__)
    guild = guild.name + '.csv'
    guild = os.path.normpath(guild)
    full_name = os.path.join('Data',guild)
    #full_name = 'D:\Python\Git\Pandacord\Data\close mutuals.csv'
    confirmation = False
    update = False
    if os.path.exists(full_name):
        with open(full_name,newline='',mode='r') as guilddata:
            data = csv.reader(guilddata)
            guildobj = []
            for row in data:
                command = row[0]
                if arg2 == command:
                    response = arg3
                    row.append(response)
                    guildobj.append(row)
                    update = True
                    
                else:
                    guildobj.append(row)
                    continue
                      
            if update == False:
                newrow = [arg2,arg3]
                print(newrow)
                guildobj.append(newrow)
            guilddata.close()
        with open(full_name,mode='w',newline='') as new_csv:
            writer = csv.writer(new_csv)
            for row in guildobj:
                writer.writerow(row)
            confirmation = True
            new_csv.close()

    else:    
        with open(full_name,newline='',mode='x') as guilddata:
            writer = csv.writer(guilddata)
            row = [arg2,arg3]
            writer.writerow(row)
            confirmation = True
            guilddata.close()
    return confirmation 