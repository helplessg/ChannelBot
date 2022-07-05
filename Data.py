from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🌹 **Hey** <b>{}</b>

**Welcome to** <b>{}</b>

**ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴄʜᴀɴɴᴇʟs ᴡɪᴛʜ ᴛᴏɴs ᴏꜰ ꜰᴇᴀᴛᴜʀᴇs. ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !**

**ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❗** **@robo_glitch**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔮ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛs🔮", url="https://t.me/futurebackups")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓", callback_data="help"),
            InlineKeyboardButton("😈 ᴀʙᴏᴜᴛ 😈", callback_data="about")
        ],
        [InlineKeyboardButton("📢 ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 💡 ", url="https://t.me/hddubhub4u")],
        [InlineKeyboardButton("📮 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 📮", url="https://t.me/dubbedweb")],
    ]

    # Help Message
    HELP = """
**ᴇᴠᴇʀʏᴛʜɪɴɢ ɪs sᴇʟꜰ ᴇxᴘʟᴀɴᴀᴛᴏʀʏ ᴀꜰᴛᴇʀ ʏᴏᴜ ᴀᴅᴅ ᴀ ᴄʜᴀɴɴᴇʟ.
ᴛᴏ ᴀᴅᴅ ᴀ ᴄʜᴀɴɴᴇʟ ᴜsᴇ ᴋᴇʏʙᴏᴀʀᴅ ʙᴜᴛᴛᴏɴ 'ᴀᴅᴅ ᴄʜᴀɴɴᴇʟs' ᴏʀ ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇʟʏ ꜰᴏʀ ᴇᴀsᴇ, ᴜsᴇ `/add` ᴄᴏᴍᴍᴀɴᴅ 🔧**

🛠 **Available Commands** 🛠

/about - About The Bot
/help - This Message
/start - Start the Bot

🛠 **Alternative Commands**🛠
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

📍 **ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ ᴀᴜᴛᴏᴍᴀᴛɪᴏɴ ʙᴏᴛ**\n**ʙʏ @robo_glitch**

📞 **ᴄᴏɴᴛᴀᴄᴛ** : **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](http://t.me/GlitchAssistantBot)**

📢 **ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ** ❤ : **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/hddubhub4u)**

📮 **sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ** 📮 : **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/dubbedweb)**

😈 **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : **@the_glitchs**
    """
