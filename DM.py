import discord
import asyncio
import datetime

token = "토큰"
client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('구문') #<- 봇 상태 구문
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'): #<- 봇 명령어
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 677902081193017395: #<-본인 디코아이디 기재 (사용할 유저등록)
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="공지") 
                        embed.add_field(name="카키 디자인", value=msg, inline=True)
                        embed.set_footer(text=f"현우#7324")
                        await i.send(embed=embed)
                except:
                    pass


client.run(token)