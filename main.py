import discord
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
WAIT_TIME = int(os.getenv("WAIT_TIME", 600))

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != CHANNEL_ID:
        return

    has_image = any(
        a.content_type and a.content_type.startswith("image")
        for a in message.attachments
    )

    if not has_image:
        return

    await asyncio.sleep(WAIT_TIME)

    msg = await message.channel.fetch_message(message.id)

    if not msg.reactions:
        await msg.add_reaction("❤️")

client.run(TOKEN)
