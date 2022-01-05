#모듈설치
import discord
import random
import string

client = discord.Client()


@client.event
async def on_ready():
    print("{client.name}")
    await client.change_presence(status=discord.Status.dnd) #다른용무중(겉멋....)


@client.event
async def on_message(message):
    if message.content.startswith('/니트로'):
        THNitro = ""
        for i in range(1, 21):
            THNitro = str(random.choice(string.ascii_letters))
            NitroEmbed = description='https://discord.gift/' + THNitro
        
#토큰넣기      
client.run('put token')


#문의사항 태형#0122 
 