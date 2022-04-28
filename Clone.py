
from os import system
import psutil
from pypresence import Presence
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

██╗░░░██╗███╗░░░███╗░█████╗░░██████╗
██║░░░██║████╗░████║██╔══██╗██╔════╝
╚██╗░██╔╝██╔████╔██║██║░░██║╚█████╗░
░╚████╔╝░██║╚██╔╝██║██║░░██║░╚═══██╗
░░╚██╔╝░░██║░╚═╝░██║╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░

{Style.RESET_ALL}
{Fore.MAGENTA}Cloner sever làm bởi VMOS-PRO{Style.RESET_ALL}
        """)
token = input(f'Hãy nhập token của bạn\n |==> ')
guild_s = input('Hãy nhập ID máy chủ bạn cần sao chép\n |==> ')
guild = input('Nhập ID máy chủ bạn cần xây dựng\n |==> ')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")
from serverclone import Clone
@client.event
async def on_ready():
    extrem_map = {}
    print(f"Đã đăng nhập với {client.user}")
    print("Bắt đầu xây dựng")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
██╗░░░██╗███╗░░░███╗░█████╗░░██████╗
██║░░░██║████╗░████║██╔══██╗██╔════╝
╚██╗░██╔╝██╔████╔██║██║░░██║╚█████╗░
░╚████╔╝░██║╚██╔╝██║██║░░██║░╚═══██╗
░░╚██╔╝░░██║░╚═╝░██║╚█████╔╝██████╔╝
░░░╚═╝░░░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░

          Đã clone thành công !
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)