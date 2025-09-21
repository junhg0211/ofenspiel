import discord
from discord import app_commands
from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 단일 슬래시 커맨드
    @app_commands.command(name="ping", description="핑을 확인합니다.")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("🏓 Pong!")

    # 그룹 만들기
    group = app_commands.Group(name="game", description="게임 관련 명령어")

    @group.command(name="start", description="게임을 시작합니다.")
    async def start(self, interaction: discord.Interaction):
        await interaction.response.send_message("🎮 게임이 시작되었습니다!")

    @group.command(name="stop", description="게임을 종료합니다.")
    async def stop(self, interaction: discord.Interaction):
        await interaction.response.send_message("🛑 게임이 종료되었습니다!")

async def setup(bot: commands.Bot):
    await bot.add_cog(ExampleCog(bot))
