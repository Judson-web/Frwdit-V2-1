import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hᴀɪ {}!!</b>
<i>I'ᴍ Fᴏʀᴡᴀʀᴅ Pʀᴏ Bᴏᴛ,
Tʜɪs Bᴏᴛ ғᴏʀᴡᴀʀᴅ ᴀʟʟ ғɪʟᴇs ᴛᴏ Oɴᴇ Pᴜʙʟɪᴄ ᴄʜᴀɴɴᴇʟ ᴛᴏ Yᴏᴜʀ Pᴇʀsᴏɴᴀʟ ᴄʜᴀɴɴᴇʟ
Mᴏʀᴇ ᴅᴇᴛᴀɪʟs /help</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Fᴏʟʟᴏᴡ Tʜᴇsᴇ Sᴛᴇᴘs!!
• Usᴇʀ Jᴏɪɴ Fʀᴏᴍ ᴄʜᴀɴɴᴇʟ Mᴜsᴛ(Nᴏ ɴᴇᴇᴅ Aᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ)
• Tʜᴇɴ ɢɪᴠᴇ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ ɪɴ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ
• Tʜᴇɴ ᴜsᴇ /run ᴄᴏᴍᴍᴀɴᴅ ɪɴ ʏᴏᴜʀ ʙᴏᴛ</b>

<b><u>Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅ</b></u>

* /start - <i>Bᴏᴛ Aʟɪᴠᴇ</i>
* /help - <i>Mᴏʀᴇ Hᴇʟᴘ</i>
* /run - <i>Sᴛᴀʀᴛ Fᴏʀᴡᴀʀᴅ</i>
* /about - <i>Aʙᴏᴜᴛ Mᴇ</i>
* /restart - <i>Sᴇʀᴠᴇʀ Rᴇsᴛᴀʀᴛ</i>"""
  ABOUT_TXT = """
╔════❰ Aʙᴏᴜᴛ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣ 
║┣⪼ Mʏ Nᴀᴍᴇ - <a href="http://t.me/ForwardProV2Robot">Fᴏʀᴡᴀʀᴅ Pʀᴏ</a>
║┣⪼ Cʀᴇᴀᴛᴏʀ - <a href=https://t.me/VAMPIRE_KING_NO_1>ƬЄƦƦƠƦ MƖƇƘЄƳ</a>
║┣⪼ Lɪʙʀᴀʀʏ - <a href="https://docs.pyrogram.org/"> Pʏʀᴏɢʀᴀᴍ </a>
║┣⪼ Lᴀɴɢᴜᴀɢᴇ - Pʏᴛʜᴏɴ 3 
║┣⪼ ⲂⲞⲦ Sᴇʀᴠᴇʀ - Hᴇʀᴏᴋᴜ
║╰━━━━━━━━━━━━━━━➣ ╚══════════════════❍⊱❁۪۪
"""
  FROM_MSG = "<b><u>Sᴇᴛ Fʀᴏᴍ Cʜᴀɴɴᴇʟ Usᴇʀɴᴀᴍᴇ</b></u>\n<b>Eɴᴛᴇʀ Fʀᴏᴍ Cʜᴀɴɴᴇʟ Usᴇʀɴᴀᴍᴇ</b>\n<code>ᴇɢ: @username</code>\n/cancel <code>- Cᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss</code>"
  TO_MSG = "<b><u>Sᴇᴛ Tᴏ Cʜᴀɴɴᴇʟ ID</b></u>\n<b>Eɴᴛᴇʀ Tᴏ Cʜᴀɴɴᴇʟ ɪᴅ</b>\n<code>ᴇɢ: -100xxxxxxxxxx</code>\n/cancel <code>- Cᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss</code>"
  SKIP_MSG = "<b><u>Sᴇᴛ Fɪʟᴇ Sᴋɪᴘɪɴɢ Nᴜᴍʙᴇʀ</b></u>\n<b>Sᴋɪᴘ ᴛʜᴇ ғɪʟᴇ ᴀs ᴍᴜᴄʜ ᴀs ʏᴏᴜ ᴇɴᴛᴇʀ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ᴛʜᴇ ʀᴇsᴛ ᴏғ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ ғᴏʀᴡᴀʀᴅᴇᴅ\nDᴇғᴀᴜʟᴛ Sᴋɪᴘ Nᴜᴍʙᴇʀ =</b> <code>0</code>\n<code>ᴇɢ: Yᴏᴜ ᴇɴᴛᴇʀ 0 = 0 ғɪʟᴇ sᴋɪᴘᴇᴅ\n Yᴏᴜ ᴇɴᴛᴇʀ 5 = 5 ғɪʟᴇ sᴋɪᴘᴇᴅ</code>\n/cancel <code>- Cᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss</code>"
  LIMIT_MSG = "<b><u>Sᴇᴛ Fɪʟᴇ Fᴏʀᴡᴀʀᴅ Lɪᴍɪᴛ</u></b>\n<b>Hᴇʀᴏᴋᴜ Dᴀɪʟʏ Lɪᴍɪᴛ</b> : <code>23000</code>\n<b>Dᴇғᴀᴜʟᴛ Lɪᴍɪᴛ</b> : <code>0</code>"
  CANCEL = "<b>Pʀᴏᴄᴇss Cᴀɴᴄᴇʟʟᴇᴅ Sᴜᴄᴄᴇғᴜʟʟʏ\nEɴᴛᴇʀ /run Aɢᴀɪɴ</b>"
  USERNAME = "<b>Sᴇɴᴅ Usᴇʀɴᴀᴍᴇ ᴡɪᴛʜ @</b>\n<code>ᴇɢ: @Username</code>\n<b>Eɴᴛᴇʀ /run Aɢᴀɪɴ</b>"
  INVALID_CHANNELID = "<b>Sᴇɴᴅ ᴄʜᴀɴɴᴇʟ ɪᴅ ᴡɪᴛʜ -100</b>\n<code>ᴇɢ: -100xxxxxxxxxx</code>\n<b>Eɴᴛᴇʀ /run Aɢᴀɪɴ</b>"
  DOUBLE_CHECK = """<b><u>Dᴏᴜʙʟᴇ Cʜᴇᴄᴋɪɴɢ⚠️</b></u>
<code>Bᴇғᴏʀᴇ ғᴏʀᴡᴀʀᴅɪɴɢ ᴛʜᴇ ғɪʟᴇ Cʟɪᴄᴋ ᴛʜᴇ Yᴇs ʙᴜᴛᴛᴏɴ ᴏɴʟʏ ᴀғᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ</code>

<i>° Mᴜsᴛ ʙᴇ ᴀ ᴜsᴇʀ ᴊᴏɪɴ ɪɴ Fʀᴏᴍ ᴄʜᴀɴɴᴇʟ ᴄʜᴇᴄᴋ ᴛʜᴀᴛ sᴛᴀᴛᴜs</i>
<i>Usᴇʀ ᴊᴏɪɴ ᴛʜɪs ᴄʜᴀɴɴᴇʟ : <b>{}</b></i>
<b><u>Nᴏᴛᴇ</u></b> : <i>Aᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ ɪs ɴᴏᴛ ᴍᴀɴᴅᴀᴛᴏʀʏ</i>
<i>° Aᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ ғᴏʀ ᴛʜᴇ ʙᴏᴛ ᴏɴ ᴛʜᴇ Tᴏ ᴄʜᴀɴɴᴇʟ ᴄʜᴇᴄᴋ ᴛʜᴀᴛ sᴛᴀᴛᴜs</i>
<b><u>Nᴏᴛᴇ</u></b> : <i>Tʜᴇʀᴇ ɪs ɴᴏ ʀᴇᴏ̨ᴜɪʀᴇᴍᴇɴᴛ ғᴏʀ ᴀ ᴜsᴇʀ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ Tᴏ ᴄʜᴀɴɴᴇʟ</i>

<b>Iғ ᴛʜᴇ ᴀʙᴏᴠᴇ ɪs ᴄʜᴇᴄᴋᴇᴅ ᴛʜᴇɴ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ᴄᴀɴ ʙᴇ ᴄʟɪᴄᴋᴇᴅ</b>"""
