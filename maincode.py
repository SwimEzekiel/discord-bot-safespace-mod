import discord
import bot_token
import message_detect_funcs

from discord.ext import commands
from discord import app_commands
from datetime import datetime

banned_words = ["kys", "kill yourself"]
cmd_prefix = "?"

with open("banned_words.csv", "r") as file:
    read_file = file.read()
    a_split = read_file.split(";")
    for i in a_split:
        banned_words.append(i)

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Safespace Mod is online now.")

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        with open("message_logs.txt", "a") as file:
            file.write(f"\nSafespace mod is now online-Logs are now starting at {current_time}\n")

        try:
            guild = discord.Object(id=1117069265602879648)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")

        except Exception as e:
            print(f"Error syncing commands: {e}")

    async def on_message(self, message):
        with open("message_logs.txt", "a") as file:
            file.write(f"{message.author} : {message.content}\n")

        if message.author == self.user:
            return
        
        if str.lower(message.content) in banned_words:
            if str(message.author) == "swimezekiel":
                print("Since you're my developer, I am coded to not allow to say anything bad to you.")
                return
            else:
                await message.channel.send(f"do not say that, @{message.author}. I will mute you.")
                await message.delete()

        elif message.content == "I'm giving birth":
                await message.channel.send(f"@ everyone PLEASE DO NOT give birth in the voice chats. i can't believe i have to say this (and it is quite embarrassing) but yesterday someone gave birth in channel, as much as we are honored that a child was birthed in this server, we also believe in privacy and children's protection on the internet! because of this we have disabled the voice chats for now.")
        

    async def on_message_delete(self, message):
        if message.author == self.user:
            return
        await message.channel.send(f'I have logs on all the messages sent here. I will expose your deleted text.')

    async def on_message_edit(self, message):
        if message.author == self.user:
            return
        await message.channel.send(f'I have logs on all the messages sent here. I will expose your unedited text.')

guild_id = discord.Object(id=1117069265602879648)

intents = discord.Intents.default()
intents.message_content = True 
client = Client(command_prefix=cmd_prefix, intents = intents)

@client.tree.command(name="say", description="Make safespace mod say something!", guild=guild_id)
async def say(interaction: discord.Interaction, message: str):
    if message in banned_words:
        await interaction.response.send_message(f"I'm not saying that tf")
    elif message == "SwimEzekiel is the best":
        await interaction.response.send_message(f"so true")
    else:
        await interaction.response.send_message(f"I am commanded to say this message. Anything that I'm about to say is out of my control. I've tried my best (not really) to blacklist the banned words. \n{message}")



client.run(f"{bot_token.token}")

