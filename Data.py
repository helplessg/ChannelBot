from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🌹 Hey {}

Welcome to {}

You can use me to manage channels with tons of features. Use below buttons to learn more !

ᴘᴏᴡᴇʀᴇᴅ ʙʏ ❗ @robo_glitch
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔮ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛs🔮", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓", callback_data="help"),
            InlineKeyboardButton("😈 ᴀʙᴏᴜᴛ 😈", callback_data="about")
        ],
        [InlineKeyboardButton("📢 ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ❤ ", url="https://t.me/hddubhub4u")],
        [InlineKeyboardButton("📮 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 📮", url="https://t.me/dubbedweb")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

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

📍 A telegram channel automation bot by @robo_glitch

📞 **ᴄᴏɴᴛᴀᴄᴛ** : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](http://t.me/GlitchAssistantBot)

📢 **ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ** ❤ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/hddubhub4u)

📮 **sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ** 📮 : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/dubbedweb)

😈 **ᴅᴇᴠᴇʟᴏᴘᴇʀ** : **@the_glitchs**
    """
