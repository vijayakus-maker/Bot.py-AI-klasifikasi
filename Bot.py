import discord
from discord.ext import commands
from model import detect_food

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Menyimpan gambar ke ./{attachment.filename}")
    else:
        await ctx.send("Anda lupa mengunggah gambar :(")


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            result = (detect_food (image_path=f"./{attachment.filename}", model="./keras_model.h5", class_names="./labels.txt" , ))
            if result[0] == "Mie Ayam\n" and result[1] >= 0.8:
                await ctx.send('Ini pasti gambar mie ayam enak sekali')
            else:
                await ctx.send(f"Ini kayanya gambar {result[0]} deh")
    else:
        await ctx.send("No file attached. womp womp")

bot.run("Token")
