import discord
import os
import pyautogui

TOKEN = 'DISCORD_TOKEN'
intents = discord.Intents.all()
client = discord.Client(intents=intents)
channel_id = 'CHANNEL_ID'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    embed = message.embeds
    if str(message.channel.id) == channel_id:
        is_long = False
        is_short = False
        is_open = False
        is_close = False

        for embed in message.embeds:
            if "long" in embed.title.lower() and "open" in embed.title.lower():
                is_long = True
                is_open = True

            if "long" in embed.title.lower() and "close" in embed.title.lower():
                is_long = True
                is_close = True

            if "short" in embed.title.lower() and "open" in embed.title.lower():
                is_short = True
                is_open = True

            if "short" in embed.title.lower() and "close" in embed.title.lower():
                is_short = True
                is_close = True

        if is_long and is_close:
            close_button_position = pyautogui.locateOnScreen('close_bet.png', confidence=0.9)
            if close_button_position:
                close_button_center = pyautogui.center(close_button_position)
                pyautogui.click(close_button_center.x, close_button_center.y)
            channel = client.get_channel(channel_id)
            await message.channel.send("Long fermé !")

        elif is_long and is_open:
            place_bet_position = pyautogui.locateOnScreen('long_bet.png', confidence=0.9)
            if place_bet_position:
                place_bet_center = pyautogui.center(place_bet_position)
                pyautogui.click(place_bet_center.x, place_bet_center.y)

            channel = client.get_channel(channel_id)
            await message.channel.send("Long envoyé !")

        elif is_short and is_close:
            close_button_position = pyautogui.locateOnScreen('close_bet.png', confidence=0.9)
            if close_button_position:
                close_button_center = pyautogui.center(close_button_position)
                pyautogui.click(close_button_center.x, close_button_center.y)
            channel = client.get_channel(channel_id)
            await message.channel.send("Short fermé !")


        elif is_short and is_open:
            place_bet_position = pyautogui.locateOnScreen('C:/Users/bapti/Desktop/short_bet.png', confidence=0.9)
            if place_bet_position:
                place_bet_center = pyautogui.center(place_bet_position)
                pyautogui.click(place_bet_center.x, place_bet_center.y)

            channel = client.get_channel(channel_id)
            await message.channel.send("Short envoyé !")

client.run(TOKEN)
