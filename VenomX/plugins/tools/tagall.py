import asyncio
import html
import re
from random import shuffle
from time import time

from pyrogram import filters, Client
from pyrogram.enums import ParseMode
from pyrogram.types import ChatPermissions, Message

from VenomX.misc import SUDOERS, db

__MODULE__ = "Tagall"
__HELP__ = """
/all atau @all - untuk tag semua member.
/stoptg - untuk menghentikan tagall.
"""

from VenomX.utils.decorators.admins import list_admins

chat_id = message.chat.id
tagallgcid = []

@app.on_message(filters.command("all","/") & filters.chat(chat_id) & ~filters.private)
async def on_tagall_handler_cmd(client, message: Message):
    if message.from_user.id not in (await list_admins(message.chat.id)):
        return
    if message.chat.id in tagallgcid:
        return await message.reply_text("sedang ada perintah: <code>all</code> yang digunakan")
    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    m = message.reply_to_message or message
    users = []
    async for member in message.chat.get_members():
        if (member.user.is_bot or member.user.is_deleted):
            continue
        users.append(member.user.mention)
        if message.chat.id not in tagallgcid:
            break
        if len(users) < 5:
            continue
        await asyncio.sleep(1.5)
        await m.reply_text(
            ", ".join(users) + "\n\n" + text, quote=bool(message.reply_to_message)
        )
        users.clear()
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass


@app.on_message(filters.command("stoptg",["/","."]) & filters.chat(chat_id) & ~filters.private)
async def on_stop_tag_handler(c: Client, m: Message):
    if m.from_user.id not in (await list_admins(m.chat.id)):
        return
    if m.chat.id not in tagallgcid:
        return await m.reply_text(
            "sedang tidak ada perintah: <code>all</code> yang digunakan"
        )
    try:
        tagallgcid.remove(m.chat.id)
    except Exception:
        pass
    await m.reply_text("ok tagall berhasil dibatalkan")
