import discord
import responses

async def send_message(message, message_content, is_private):
  try:
    response = responses.handle_response(message_content)
    if response:
      if is_private:
        await message.author.send(response)
      else:
        await message.channel.send(response)
  except Exception as e:
    print(e)

def run_discord_bot():
  TOKEN = "MTE4ODgyNjI1NDIyNTQ0MDc4OA.GpRg5O.59T2jcwI7HYAcnHdY_aZc3VZ-R40Yy5ijmOEQM"
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
    print(f'{client.user} is now runnign!')

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
    
    username = str(message.author)
    message_content = str(message.content)
    channel = str(message.channel)

    if message_content[0] == "?":
      message_content = message_content[1:]
      await send_message(message, message_content, is_private=True)
    else:
      await send_message(message, message_content, is_private=False)

  client.run(TOKEN)