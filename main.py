import discord
import os
import asyncio
import random
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix=(["n ","N ","nb ","Nb "]), help_command=None)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game("Nb nhelp"))
print("Bot is ready!") 

@client.command()
async def nhelp(ctx):
  embed = discord.Embed(
 title="NB helper is a bot for Naruto Botto cooldowns!",
 description="We have command for Mission help that is ``Nb mhelp``.\n \nThe bot will respond like when you do n mission so it will ping you after 1 minute and for every Naruto botto command except long commands like daily and weekly!",
  color=0x000000
  )
  embed.set_image(url="")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894943504751534150/954268125870829588/jougan.png")
  embed.set_footer(text="Requested By {}".format(ctx.message.author.name),icon_url="https://cdn.discordapp.com/attachments/894943504751534150/957146536037457920/jougan.png")
  await ctx.send(embed=embed)

@client.command()
async def mhelp(ctx):
  embed = discord.Embed(
 title="Helping for your mission!",
 description="**Tailed beasts:-**\n1-shukaku\n2-matatabi\n3-isobu\n4-son goku \n5-kokuo \n6-saiken \n7-chomei \n8-gyuki \n9-kurama\n \n**Seven ninja Swordsmen of the mist:-**\nJinin = kabutowari\nJinpachi = shibuki\nFuguki, kisame = samehada\nZabuza, suigetsu = kubikiribocho\nChojuro = hiramekarei\nAmeyuri, raiga = kiba\nKushimaru = nuibari ",
  color=0x000000
  )
  embed.set_image(url="")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/894943504751534150/954268125870829588/jougan.png")
  embed.set_footer(text="Bot will ping you 1 minute after mission done! Requested By {}".format(ctx.message.author.name),icon_url="https://cdn.discordapp.com/attachments/894943504751534150/957146536037457920/jougan.png")
  await ctx.send(embed=embed)

@client.command(aliases=['m'])
async def mission(ctx):
  await asyncio.sleep(60)
  await ctx.send(f"<:ready:954051849533661224> **Mission** is Ready {ctx.message.author.mention}!")

@client.command(aliases=['r'])
async def report(ctx):
  await asyncio.sleep(600)
  await ctx.send(f"<:ready:954051849533661224> **Report** is Ready {ctx.message.author.mention}!")

@client.command(aliases=['to'])
async def tower(ctx):
  await asyncio.sleep(21600)
  await ctx.send(f"<:ready:954051849533661224> **Tower** is Ready {ctx.message.author.mention}!")

@client.command(aliases=['ch'])
async def challenge(ctx):
  await ctx.send(f"{ctx.message.author.mention} Type **nb chg** when challenge is done.")

@client.command()
async def chg(ctx):
  await ctx.send(f"{ctx.message.author.mention} Your **Challenge** Cooldown has started!")
  await asyncio.sleep(1800)
  await ctx.send(f"<:ready:954051849533661224> **Challenge** is Ready {ctx.message.author.mention}!")

@client.command(aliases=['tr'])
async def train(ctx):
  await ctx.send(f"{ctx.message.author.mention} Type **nb trn** when train is done.")

@client.command()
async def trn(ctx):
  await ctx.send(f"{ctx.message.author.mention} Your **Train** Cooldown has started!")
  await asyncio.sleep(3600)
  await ctx.send(f"<:ready:954051849533661224> **Train** is Ready {ctx.message.author.mention}!")

@client.command(aliases=['v'])
async def vote(ctx):
  await ctx.send(f"{ctx.message.author.mention} Type **nb nv** when vote is done.")

@client.command()
async def nv(ctx):
  await ctx.send(f"{ctx.message.author.mention} Your **Vote** Cooldown has started!")
  await asyncio.sleep(43200)
  await ctx.send(f"<:ready:954051849533661224> **Vote** is Ready {ctx.message.author.mention}!")

@client.command()
async def ninjapromo(ctx):
    firstID = 843008997391990804
    secondID = 900012098040504321
    if ctx.message.author.id == firstID or ctx.message.author.id == secondID:
     embed = discord.Embed(
   title="Rank Promotion for Shinobi World",
   description="**Shinobi World is a Naruto botto based naruto server**\nHere are the Ninja rank promotion:-\nAnbu Black Ops:- 250k power or more\nRogue Ninja:- 200k to 249k\nJonin:- 150k to 200k power\nChunin:- 100k to 199k power\nGenin:- 50k to 100k power\nAcademy Student:- Below 50k power",
   color=0x000000
   )
    embed.set_image(url="https://cdn.discordapp.com/attachments/918366358692061224/954055100765200454/latest.png")
    embed.set_thumbnail(url="")
    await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv('token'))