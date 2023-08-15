# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs.ram.helpers.basic import edit_or_reply
from geezlibs.ram.helpers.PyroHelpers import ReplyCheck
from config import CMD_HANDLER as cmd
from config import IG_ALIVE, CH_SFS, REPO_URL
from .help import add_command_help


@Client.on_message(filters.command("p", cmd) & filters.me)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum, aku anak nguyung🥷!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("pe", cmd) & filters.me)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum dek",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("l", cmd) & filters.me)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam dek",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("el", cmd) & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam wahai para kacung",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("oi", cmd) & filters.me)
async def salken(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Haii Salken Saya {client.me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("Kalian Anjing,Anak Haram Titisan Asmodeus, Bocah tengik, Penyembah tongkat Kera Sakti, nguyung opmem dek")


@Client.on_message(filters.command("ass", cmd) & filters.me)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Gua..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")


@Client.on_message(filters.command("j", cmd) & filters.me)
async def jakasem(client: Client, message: Message):
    xx = await edit_or_reply(message, "**Woi Kontol....**")
    await asyncio.sleep(3)
    await xx.edit("**Muka lo jelek Bgt Kaya memek lacur tele!!!🔥**")


@Client.on_message(filters.command("k", cmd) & filters.me)
async def ngegas(client: Client, message: Message):
    xx = await edit_or_reply(message, f"**Hi semua aku adalah {client.me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("**Nguyung opmem dek 🥷**")


@Client.on_message(filters.command("mutu", cmd) & filters.me)
async def igehh(client: Client, message: Message):
    xx = await message.reply("**Mutualan IG Yuk!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih IG Ku = [TEKAN](https://instagram.com/{IG_ALIVE})", disable_web_page_preview=True)


@Client.on_message(filters.command("sfs", cmd) & filters.me)
async def channel(client: Client, message: Message):
    xx = await message.reply("**Yok SFS!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih CH Ku = [TEKAN](https://t.me/{CH_SFS})", disable_web_page_preview=True)


@Client.on_message(filters.command("repo", cmd) & filters.me)
async def reporl(client: Client, message: Message):
    xx = await message.reply("**Jan Bawel!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih REPONYA = [TEKAN](https://github.com/alvarensixy/RenPyro)", disable_web_page_preview=True)


@Client.on_message(filters.command("getstring", cmd) & filters.me)
async def string(client: Client, message: Message):
    xx = await message.reply("**Jan Bawel!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih String = [TEKAN](https://t.me/rensixy)", disable_web_page_preview=True)


@Client.on_message(filters.command("keluar", cmd) & filters.me)
async def keluar(client: Client, message: Message):
    xx = await message.reply("`Processing...`")
    await asyncio.sleep(1)
    await xx.edit(f"{client.me.first_name} has left this group, bye!!")

