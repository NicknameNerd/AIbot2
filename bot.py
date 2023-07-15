import discord
import responses

# https://discord.com/api/oauth2/authorize?client_id=1129723240256897094&permissions=21434035338304&scope=bot

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "example adress ******************"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message, user_message=None):
        if message.author == client.user:
            return

        username = str(message.author)
        user_name = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

#removing type errors like '?' in the beginning of "?Hello!" of usermessages to "Hello!"
        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
