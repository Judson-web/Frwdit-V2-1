#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import sys
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram.errors import FloodWait
from config import Config
from translation import Translation

FILTER = Config.FILTER_TYPE
IS_CANCELLED = False
lock = asyncio.Lock()

@Client.on_callback_query(filters.regex(r'^start_public$'))
async def pub_(bot, message):
    global files_count, IS_CANCELLED
    await message.answer()
    await message.message.delete()
    from plugins.public import FROM, TO, SKIP, LIMIT
    if lock.locked():
        await message.message.reply_text('__Pʀᴇᴠɪᴏᴜs ᴘʀᴏᴄᴇss ʀᴜɴɴɪɴɢ 🥺..__', parse_mode="md")
    else:
        m = await message.message.reply_text(
            text="<i>Pʀᴏᴄᴇssɪɴɢ...⏳</i>"
        )
        total_files=0
        async with lock:
            try:
                pling=0
                async for message in bot.USER.search_messages(chat_id=FROM,offset=int(SKIP),limit=int(LIMIT),filter=FILTER):
                    if IS_CANCELLED:
                        IS_CANCELLED = False
                        break
                    try:
                        if message.video:
                            file_name = message.video.file_name
                        elif message.document:
                            file_name = message.document.file_name
                        elif message.audio:
                            file_name = message.audio.file_name
                        else:
                            file_name = None
                        await bot.copy_message(
                            chat_id=TO,
                            from_chat_id=FROM,
                            parse_mode="md",       
                            caption=Translation.CAPTION.format(file_name),
                            message_id=message.message_id
                        )
                        total_files += 1
                        await asyncio.sleep(1)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                        await bot.copy_message(
                            chat_id=TO,
                            from_chat_id=FROM,
                            parse_mode="md",       
                            caption=Translation.CAPTION.format(file_name),
                            message_id=message.message_id
                        )
                        total_files += 1
                        await asyncio.sleep(1)
                    except Exception as e:
                        print(e)
                        pass
                    pling += 1
                    if pling == 10: 
                        buttons = [[
                            InlineKeyboardButton('Cᴀɴᴄᴇʟ', 'terminate_frwd')
                        ]]
                        reply_markup = InlineKeyboardMarkup(buttons)
                        await m.edit_text(
                            text=f'<b><u>Fᴏʀᴡᴀʀᴅ Sᴛᴀᴛᴜs</b></u>\n\n<b>Sᴜᴄᴄᴇғᴜʟʟʏ ғᴏʀᴡᴀʀᴅᴇᴅ ғɪʟᴇ ᴄᴏᴜɴᴛ :</b> <code>{total_files} ғɪʟᴇs</code>',
                            reply_markup=reply_markup, 
                            parse_mode="html"
                        )
                        pling -= 10
            except Exception as e:
                print(e)
                await m.edit_text(f'Error: {e}')
            else:
                buttons = [[
                    InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url='https://t.me/STMbOTsUPPORTgROUP')
                    ],[
                    InlineKeyboardButton('Mᴏᴠɪᴇ Gʀᴏᴜᴘ', url='https://t.me/storytym')
                ]]
                reply_markup = InlineKeyboardMarkup(buttons)
                await m.edit_text(
                    text=f"<u><i>Sᴜᴄᴄᴇssғᴜʟʟʏ Fᴏʀᴡᴀʀᴅᴇᴅ</i></u>\n\n<b>Tᴏᴛᴀʟ Fᴏʀᴡᴀʀᴅᴇᴅ Fɪʟᴇs:-</b> <code>{total_files}</code> <b>Fɪʟᴇs</b>\n<b>Tʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ❤️</b>",
                    reply_markup=reply_markup,
                    parse_mode="html")
      
@Client.on_callback_query(filters.regex(r'^terminate_frwd$'))
async def terminate_frwding(bot, update):
    global IS_CANCELLED
    IS_CANCELLED = True
    
@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close(bot, update):
    await update.answer()
    await update.message.delete()
