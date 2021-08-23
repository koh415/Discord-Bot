# Discord Bot for sidcord
import discord
import os
import requests
import json
import random
from replit import db


# List for sad words
sad_words = ["sad", "depressed","unhappy","angry","miserable", "depressing","morbid","dejected","meloncholy","shitted on"]

# List for encouraements
start_encouragements = [
  "Cheer Up!",
  "Hang in there!",
  "You can't win them all.",
  "You'll get them next time champ!",
  "You're an amazing person.",
  "You were an asshole but you'll get better!",
  "It'll buff right out",
]


# DiscordAPI 
my_secret = os.environ['TOKEN']

# Function for quotes 
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


# Variable for bot
client = discord.Client()


@client.event
async def on_ready():
  print('We have login in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(start_encouragements))

  if message.content.startswith('$owner'):
    await message.channel.send('V1brant aka Koh aka Sid')  

  if message.content.startswith('$admin'):
    await message.channel.send('Here\'s a quick list of our admins: \nZazo \nNokio \nSlurppie \nSwayzee \nGeddz \nTriton')

  if message.content.startswith('$mods'):
    await message.channel.send('Here\'s a quick list of our mods: \nBayani \nDonut \nk1o \nMikeyS \ntight')

  if message.content.startswith('$rules'):
    await message.channel.send('1. No Racism \n2. No Gore / NSFL \n3. Do not spam \n4. Do not send others viruses or malware \n5. Do not organize, participate in, or encourage harassment of others  \n6. Use the appropriate channels for whatever purpose it may be \n7. Please be careful with what you talk about in the streaming lobby! \n8.  No doxxing/releasing other\'s private personal information, no matter the reason. \n9.  Do not advertise any Discord servers or referral links or all the other crap noone cares about including in DMs. If you ever receive unsolicited DMs from a user in this server, please message a mod/admin and they will deal with it. \n10.  Follow Discord\'s AND Steam\'s TOS at all times. \nRules also can be viewed in the #rules channel!')

client.run(os.getenv('TOKEN'))