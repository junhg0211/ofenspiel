import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# 봇 초기화 (접두사는 !, 필요시 변경 가능)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Cog 자동 로드
@bot.event
async def on_ready():
    print(f"✅ 로그인 성공: {bot.user} (ID: {bot.user.id})")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    import asyncio
    load_dotenv()
    asyncio.run(load_cogs())
    bot.run(os.getenv("BOT_TOKEN"))  # <- 토큰 넣기
