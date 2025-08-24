import discord
import asyncio
TOKEN = "" #ボブ
client = discord.Client(intents=discord.Intents.all())




   
@client.event    #ヌリ・での発言をbotが削除
async def on_message(message):
    if not message.author.bot:
        return
    if message.content == "ご商談・ご歓談は<#1408578827856248905>にてどうぞ": #メッセージが /a だったら /a を変えることで反応させるメッセージ変更
       await asyncio.sleep(10)  #60秒間待つ
       await message.delete()  #/a を削除する



   

client.run(TOKEN)
