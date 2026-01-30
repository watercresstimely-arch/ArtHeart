import discord
import asyncio
import os

# ========== CONFIG ==========

TOKEN = os.getenv("DISCORD_TOKEN")

TARGET_CHANNEL_ID = 1466902507157717092 
WAIT_SECONDS = 60  # 3 hours sjsjsnsis
REACTION_EMOJI = "<:noodlelove:1459884784586195076>"
# ============================


intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")


@client.event
async def on_message(message):

    # Ignore bots
    if message.author.bot:
        return

    # Only target channel
    if message.channel.id != TARGET_CHANNEL_ID:
        return

    # Must contain attachment
    if not message.attachments:
        return

    # Check for image file types
    is_image = any(
        attachment.filename.lower().endswith(
            ("png", "jpg", "jpeg", "gif", "webp")
        )
        for attachment in message.attachments
    )

    if not is_image:
        return

    print(f"Image detected: {message.id}")

    # Wait 3 hours
    await asyncio.sleep(WAIT_SECONDS)

    try:
        msg = await message.channel.fetch_message(message.id)

        # Count all reactions
        total_reactions = sum(reaction.count for reaction in msg.reactions)

        if total_reactions == 0:
            await msg.add_reaction(REACTION_EMOJI)
            print("Reaction added")
        else:
            print("Message already has reactions")

    except Exception as e:
        print("Error:", e)


client.run(TOKEN)
