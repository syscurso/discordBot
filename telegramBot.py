#https://my.telegram.org/apps
#Instagram syscursos
#Telegram t.me/syscursos

from telethon import TelegramClient, events
from datetime import datetime
import pyjokes


api_id = 15209149
api_hash = '7016b258a72b41bd7047d7cb8f4ac3f7'
chatName = '@syscursos'

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
joke = pyjokes.get_joke(language='es', category='all')


client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=chatName))

async def my_event_handler(event):

  respuesta = answer(event.text)
  print(event.text)
  await client.send_message(chatName, respuesta)

def answer(word):
      
  if word == '/broma':
      return joke
  
  if word == '/hora':
      return current_time

client.start()
client.run_until_disconnected()
