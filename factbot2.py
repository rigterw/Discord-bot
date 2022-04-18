from multiprocessing.connection import wait
import discord, datetime, asyncio
from random import randrange as random


client = discord.Client()
nextfact = datetime.datetime(1,1,1)



@client.event
async def on_connect():
    nextfact = datetime.datetime.now()
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
    channel = client.get_channel(715680206609973319)
    print(channel)
    await channel.send("go")

def setTime():
    currentday = datetime.datetime.now()
    nextfact = datetime.datetime(currentday.year, currentday.month, currentday.day, random(0,23), random(0,59))
    waitTime = (nextfact-currentday).total_seconds()
    #print(waitTime)
    return waitTime






client.run('OTY0OTM3MTU1MzI1NjA4MDg4.Ylr5wQ.tnhyXaJCVP7G-UnOElaPm5yaId4')
print("run")

