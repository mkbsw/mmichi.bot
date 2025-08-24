import discord
import asyncio
TOKEN = "MTQwODgxNjQ1MDAyNTgyMDI1MA.G20F7h.fRuN8bhhJGqxFjkH5GniIeLcuw5Z7g_DFNFXO0"   #トレーダー
client = discord.Client(intents=discord.Intents.all())


@client.event    #ラウンジでの削除を魚拓
async def on_message_delete(message):
    if message.author.bot:
        return
    channel_ID = 1408578827856248905
    if message.channel.id == channel_ID:
     await message.channel.send(f"{message.author.name}様の言質はこちらになります\n```\n{message.content}\n```")



@client.event    #ヌリ・でのユーザー発言をbotが削除
async def on_message(message):
    if message.author.bot:   #botはスルー
        return
    channel_ID = 1408579006894178495
    if message.channel.id == channel_ID:
      if not message.attachments:
       await message.delete()#メッセージの削除　ヌリ
       await message.channel.send("ご商談・ご歓談は<#1408578827856248905>にてどうぞ")

    channel_ID = 1408579108593598464
    if message.channel.id == channel_ID: 
     if not message.attachments:
      await message.delete()#メッセージの削除　野生動物
      await message.channel.send("ご商談・ご歓談は<#1408578827856248905>にてどうぞ")

    channel_ID = 1408579461967908964
    if message.channel.id == channel_ID: 
     if not message.attachments:
      await message.delete()#メッセージの削除　モブ
      await message.channel.send("ご商談・ご歓談は<#1408578827856248905>にてどうぞ")
      
    channel_ID = 1408579677303476254
    if message.channel.id == channel_ID: 
     if not message.attachments:
      await message.delete()#メッセージの削除　ソロ
      await message.channel.send("ご商談・ご歓談は<#1408578827856248905>にてどうぞ")      

    channel_ID = 1408580828388266035
    if message.channel.id == channel_ID: 
     if not message.attachments:
      await message.delete()#メッセージの削除　泥酔
      await message.channel.send("ご商談・ご歓談は<#1408578827856248905>にてどうぞ")



@client.event  #新規加入者メッセ
async def on_member_join(member):
    channel = client.get_channel(1408578827856248905) # Welcome channel.
    await channel.send(f'ようこそ{member.mention}様 \n ここは何でも有りの場でございます。 \n どうぞご存分にお楽しみください')









client.run(TOKEN)