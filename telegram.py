from telethon.sync import TelegramClient
import pandas as pd
import time
import asyncio




from telethon import TelegramClient
from openpyxl import Workbook

api_id = 
api_hash = ''
channel_username = 'antifake_uz'

client = TelegramClient('session_name', api_id, api_hash)

# Kirill → Lotin
def cyrillic_to_latin(text):
    mapping = {
        'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'j','з':'z',
        'и':'i','й':'y','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r',
        'с':'s','т':'t','у':'u','ф':'f','х':'x','ц':'ts','ч':'ch','ш':'sh',
        'щ':'sh','ъ':"'",'ь':"",'э':'e','ю':'yu','я':'ya',
        'қ':'q','ғ':'gʻ','ҳ':'h','ў':'oʻ',

        'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'Yo','Ж':'J','З':'Z',
        'И':'I','Й':'Y','К':'K','Л':'L','М':'M','Н':'N','О':'O','П':'P','Р':'R',
        'С':'S','Т':'T','У':'U','Ф':'F','Х':'X','Ц':'Ts','Ч':'Ch','Ш':'Sh',
        'Щ':'Sh','Ъ':"'",'Ь':"",'Э':'E','Ю':'Yu','Я':'Ya',
        'Қ':'Q','Ғ':'Gʻ','Ҳ':'H','Ў':'Oʻ'
    }
    return ''.join(mapping.get(char, char) for char in text)

# Sarlavha ajratish (birinchi qator)
def split_title_text(text):
    lines = text.split('\n')
    title = lines[0] if lines else ""
    body = " ".join(lines[1:]) if len(lines) > 1 else ""
    return title, body

async def main():
    await client.start()

    wb = Workbook()
    ws = wb.active
    ws.title = "Telegram Data"

    # Header
    ws.append(['id', 'sarlavha', 'matn', 'sana', 'manba'])

    async for message in client.iter_messages(channel_username, limit=500):
        text = message.text or ""

        # Lotinga o‘girish
        text_latin = cyrillic_to_latin(text)

        # Sarlavha + matn ajratish
        title, body = split_title_text(text_latin)

        ws.append([
            message.id,
            title,
            body,
            str(message.date),
            channel_username
        ])

    wb.save("telegram_dataset.xlsx")
    print("✅ Tayyor: telegram_dataset.xlsx")

with client:
    client.loop.run_until_complete(main())










