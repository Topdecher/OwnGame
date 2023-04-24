import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord import Interaction

from environment.own_button import OwnButton
from environment.registration_form import RegistrationForm

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command(name="register", help="регистрирует участника")
async def register(ctx: Context):
    button = OwnButton(1, 1, 1)
    response = discord.InteractionResponse(Interaction())
    await discord.InteractionResponse()
