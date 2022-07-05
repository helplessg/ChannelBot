from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.regex(r'^Report a Problem$') | filters.command('report'))
async def _manage(_, msg):
    how = '**📍Report a Problem📍** \n\n'
    how += "If something **unexpected** happens, you can report it to us. (You can also suggest features.)\n\n"
    how += '**💌 Steps 💌** \n'
    how += '➥ (1) Try whatever you did again. If it shows the same unexpected thing, move to step 2 \n'
    how += '➥ (2) Visit **@GlitchAssistantBot** \nor @the_glitchs and define your problem **completely**, i.e, what you expected and what happened instead.'
    how += "If you don't get a reply, tag an admin in Support Group."
    await msg.reply(
        how,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('📮 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 📮', url='https://t.me/hddubhub4uhelp')]
        ]),
        quote=True
    )
