from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "Buy premium":
        await query.message.edit_text(
            text=f"@Hentai_ Cinema all Channels Premium Benefits & Perks\nDirect Channel Links, No Ad Links\nSpecial Access In Events\n\n<blockquote>Pricing Rates\n•𝗣𝗿𝗶𝗰𝗲\n1 𝗺𝗼𝗻𝘁𝗵 -  ₹100\n•𝗣𝗿𝗶𝗰𝗲 3 𝗺𝗼𝗻𝘁𝗵 -  ₹250\n•𝗣𝗿𝗶𝗰𝗲 6 𝗺𝗼𝗻𝘁𝗵 -  ₹400\n•𝗣𝗿𝗶𝗰𝗲 1 𝘆𝗲𝗮𝗿   -  ₹700 - Contact to Buy<a href=https://t.me/Kira_Yagamai>Owner</a></blockquote>\n\n<blockquote>Want To Buy?\@Kira_Yagamai\n\nWe Have Limited Seats For Premium Users",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Buy Now", url="https://t.me/Kira_Yagamai"),
                        InlineKeyboardButton("Main Channel", url="https://t.me/+bLmBM2XnZSk1NDg1")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass