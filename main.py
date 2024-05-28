import os
from dotenv import load_dotenv
from discord import Intents, Client, Embed, ui, SelectOption, Interaction
from responses import get_response
import json

# Load token from secret lair
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# Setup
intents = Intents.default()
intents.message_content = True 
client = Client(intents=intents)

## COLOR ROLES SELECT MENU
class color_roles_select_menu(ui.View):
    @ui.select(
        placeholder="Please Select a Color Role...",
        min_values=1,
        max_values=1,
        options=[
            SelectOption(
                label="Green",
                description="Pick this if you would like the Green role!",
            )
        ]
    )
    async def select_callback(self, interaction: Interaction, select: ui.Select):
        load_roles = json.load(open('responses.json'))

        selected_option = select.options[0].value
        
        await interaction.response.send_message(f"You selected {selected_option}!")

        role_to_assign = interaction.guild.get_role(int(load_roles["roles"]["color_roles"][str(selected_option.lower())]))
        
        try:
            await interaction.user.add_roles(role_to_assign)
            await interaction.followup.send(f"Role, {selected_option}, assigned successfully.")
        except Exception as e:
            await interaction.followup.send(f"Failed to assign role: {e}")

# Functionality
async def send_message(message, user_message) -> None:
    if not user_message:
        print("(Message was empty, Intents not enabled)")
        return

    if is_private := user_message[0] == "~":
        user_message = user_message[1:]

    if user_message.startswith("?colorroles"):
        await message.channel.send("COLOR ROLES", view=color_roles_select_menu())
        return
    
    try:
        response = get_response(user_message)

        if type(response) is list:
            embed = Embed(title=response[0], description=response[1], color=response[2])
            await message.author.send(embed=embed) if is_private else await message.channel.send(embed=embed)

        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Startup
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")

@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'[{channel}], {username}: "{user_message}"')
    
    await send_message(message, user_message)

def main() -> None:
    client.run(TOKEN)

if __name__ == "__main__":
    main()
