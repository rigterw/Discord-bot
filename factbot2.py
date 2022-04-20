from multiprocessing.connection import wait
from aiohttp import request
from googletrans import Translator
import discord, datetime, asyncio, json, requests
from random import randrange as random


client = discord.Client()
nextfact = datetime.datetime(1,1,1)
translator = Translator()



@client.event
async def on_connect():

    i = 0
    while i < 10:
        await checkFactTime()
        i+=1



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'hoi':
        channel = message.channel
        await channel.send('hoi')
    


async def checkFactTime():
            await sendFact()
            print("true")
            await asyncio.sleep(setTime())

async def sendFact():
    fact = getFact()
    feitje = translator.translate(fact, "nl")
    print(type(feitje))
    channel = client.get_channel(715680206609973319)
    print(channel)
    await channel.send("Fact of the day: \n"+feitje.text)
    print(fact)

def getFact():
    fact = requests.get("https://api.api-ninjas.com/v1/facts?limit=1", headers={'X-Api-Key': "CB0eucx3lFZayue7aSDJGw==tvtLUMKZp4ygZAPN"})
    if fact.status_code == requests.codes.ok:
        json_data = json.loads(fact.text)
        
        return json_data[0]['fact']
    else:
        return "wessel kan geen goede bots maken"

def setTime():
    currentday = datetime.datetime.now()
    tomorrow = currentday.day + 1
    nextfact = datetime.datetime(currentday.year, currentday.month, tomorrow, random(0,23), random(0,59))
    waitTime = (nextfact-currentday).total_seconds()
    return waitTime






client.run(TOKEN)
print("run")

