import discord

from environment.own_button import OwnButton


class OwnDisplay(discord.ui.View):
    def __init__(self, current_player: int, tour: int):
        self.current_player = current_player
        self.tour = tour
        super().__init__()

        for x in range(5):
            for y in range(5):
                self.add_item(OwnButton(x, y, tour))


