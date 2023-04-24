import discord
from discord import ui


class RegistrationForm(ui.Modal, title="Регистрация на игру"):
    name = ui.TextInput(label="Ваш никнейм:", row=0)

    async def on_submit(self, interaction: discord.Interaction):
        pass