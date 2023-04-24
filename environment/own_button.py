import discord


class OwnButton(discord.ui.Button):
    def __init__(self, x: int, y: int, tour: int):
        self.value = y * 100 * tour
        self.x = x
        self.y = y
        super().__init__(style=discord.ButtonStyle.green, label=str(self.value), row=x)

    def callback(self, interaction: discord.Interaction):
        if self.view is None:
            await interaction.response.send_message(content="Something went wrong")
            return
        display = self.view
        button_state = display
