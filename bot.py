import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return

    if any(word in message.content.lower() for word in ['to', 'too', 'two', '2']):
      await message.channel.send('tuah MENTCH')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQxMDQ4NjU4MTgwMjA0MTQzNw.GcFzQO.eO4MuzqWiflcB5zO8JRYzn1xpQkOIrYS7KMRNg')