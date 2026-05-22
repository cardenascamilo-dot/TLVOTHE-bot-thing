# the main code for moving around the map

from discord import app_commands
import discord

from game.player import players, create_player
from game.movement import move_player

GAME_ROLE_ID = 123456789012345678  # replace with your role id


@bot.tree.command(name="move", description="Move through the train")
@app_commands.describe(direction="Choose where to move")

@app_commands.choices(direction=[
    app_commands.Choice(name="Front", value="front"),
    app_commands.Choice(name="Back", value="back")
])

async def move(
    interaction: discord.Interaction,
    direction: app_commands.Choice[str]
):

    member = interaction.user

    # check if player has the passenger role
    has_role = any(role.id == GAME_ROLE_ID for role in member.roles)

    if not has_role:
        await interaction.response.send_message(
            "You ain't playing.",
            ephemeral=True
        )
        return

    user_id = str(member.id)

    # create player if they existn't
    if user_id not in players:
        create_player(user_id)

    # move player
    result = move_player(
        players[user_id],
        direction.value
    )

    if result is None:
        await interaction.response.send_message(
            "You can't go that way.",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"You moved to {result}.",
        ephemeral=True
    )
