import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
Tekrar = ("False")
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}(Çöpçü)')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Temizlik'):
        await message.channel.send("Hangisini Seçerdin?                                                                                                                                                                                                      (Hedef Kitle :one:):Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen gençler                                                                                                                                                                                                      (Hedef Kitle :two:):Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen yetişkinler.                                                                                                                                                                                                      (Hedef Kitle :three:):Çevreye yardım etmek isteyenler.                                                                                                                                                                                                      (Hedef Kitle :four:):Çevre botu almak isteyenler.                                                                                                                                                                                                      (Hedef Kitle :five:):Sadece çöp resimlerine bakmak isteyenler")
    elif message.content.startswith('Hedef Kitle 1️⃣'):
        RNameM = random.choice(os.listdir('1'))
        print(message.content)
        with open(f'1/{RNameM}', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        await message.channel.send("Hiç bir şeyi israf etmeyin ve geri dönüşüm kutusuna çöplerinizi atın")
    elif message.content.startswith('Hedef Kitle 2️⃣'):
        with open(f'0/HavaliCopcu.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        await message.channel.send("Çocuğunuzdan bu sunucuda (Hedef Kitle :one:) yazmasını isteyin")
    elif message.content.startswith('Hedef Kitle 3️⃣'):
        RNameM = random.choice(os.listdir('3'))
        with open(f'3/{RNameM}', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        await message.channel.send("Yerlere çöp atmayın ve yerde çöp görürseniz alın, çöplerinizi geri dönüşüm kutusuna atın")
    elif message.content.startswith('Hedef Kitle 4️⃣'):
        with open(f'0/Envbot.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        await message.channel.send("Bu linke tıklayın:")
        await message.channel.send("https://devpost.com/software/envbot")
    elif message.content.startswith('Hedef Kitle 5️⃣'):
        RNameM = random.choice(os.listdir('5'))
        with open(f'5/{RNameM}', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)


client.run(Token)
