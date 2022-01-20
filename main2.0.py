from telethon import TelegramClient, events, Button

app_id = "9037035"
api_hash = "8d560b235403170a2c9fae863957dbc3"
token = "5231613135:AAGrl82YfLfTPJI-wuPyRz9lfb-Vgd_c380"

client = TelegramClient("Legeeteoy", app_id, api_hash).start(bot_token=token)

@client.on(events.NewMessage(incoming=True))
async def start(event):
    button = [(Button.url("Support", "https://t.me/Viraj_legacy"))]
    await client.send_message(event.chat_id, "Hello How Are  U", buttons=button)



client.run_until_disconnected()