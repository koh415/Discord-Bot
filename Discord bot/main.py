# Discord Bot for sidcord
#libraries 
import discord
from discord.ext.commands import Bot
from discord import Intents
from discord.ext import commands
import io
import asyncio
import aiohttp
import os
import requests
import json
import random
from replit import db

# bot variable 
bot = Bot(command_prefix='$')

# List for sad words
sad_words = ["sad", "depressed","unhappy","angry","miserable", "depressing","morbid","dejected","meloncholy","shitted on"]

# List for encouraements
start_encouragements = [
  "Cheer Up!",
  "Hang in there!",
  "You can't win them all.",
  "You'll get them next time champ!",
  "You're an amazing person.",
  "Come on! You can do it!.",
  "It'll buff right out",
  "Never give up.",
  "Stay strong.",
  "Keep fighting!",
  "Keep Pushing G!"
]

# DiscordAPI 
my_secret = os.environ['TOKEN']

# Function for quotes 
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#Online print statement
@bot.event
async def on_ready():
  print('We have login in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
  if message.author == bot.user:
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
    await message.channel.send('Here\'s a quick list of our admins: \n<@234932426370056193> \n<@319276480683048973> \n<@139506615010328576> \n<@258425124271685632> \n<@101062013593088000> \n<@96127875668770816>')

  if message.content.startswith('$mods'):
    await message.channel.send('Here\'s a quick list of our mods: \n<@114875787173298183> \n<@372785252340334593> \n<@244077241330302977> \n<@187762730155900928> \n<@193085582195294209>')

  if message.content.startswith('$rules'):
    await message.channel.send('1. No Racism \n2. No Gore / NSFL \n3. Do not spam \n4. Do not send others viruses or malware \n5. Do not organize, participate in, or encourage harassment of others  \n6. Use the appropriate channels for whatever purpose it may be \n7. Please be careful with what you talk about in the streaming lobby! \n8.  No doxxing/releasing other\'s private personal information, no matter the reason. \n9.  Do not advertise any Discord servers or referral links or all the other crap noone cares about including in DMs. If you ever receive unsolicited DMs from a user in this server, please message a mod/admin and they will deal with it. \n10.  Follow Discord\'s AND Steam\'s TOS at all times. \nRules also can be viewed in the <#700137885722214461> channel!')

  if message.content.startswith('$lol'):
    await message.channel.send('Ha Ha Ha Ha u funny as hell!')

#a work in progress
@commands.command()
async def dog(self, ctx):
  async with aiohttp.ClientSession() as cs:
    async with cs.get("https://random.dog/woof.json") as r:
      data = await r.json()

      embed = discord.Embed(title="Woof")
      embed.set_image(url=data['url'])
      embed.set_footer(text="http://random.dog/")

      await ctx.send(embed=embed)


# $smoke command, user joins smoke sesh room and bot annouces it to server i.e. "[User] has joined the smoke sesh!"

bot.run(os.getenv('TOKEN'))