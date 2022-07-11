from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardMarkup,
)
from pyrogram.errors import FloodWait
import config as c
import os
import requests
import hmtai
import nekos
app = Client("wc", bot_token=c.BOT_TOKEN, api_id=c.API_ID, api_hash=c.API_HASH)

start_message = "**Hello Degens and pure people** I'm Anna.. I can give you both **SFW** & `NSFW` Images and GIFs..Please Use buttons to get whatever you want\n\n**Note:** NSFW means Adult Contents and SFW means not adult contents.So when you choosing please reconsider your choice\n\nPowered By: **@otaku_network**\nOngoing Animes Channel: @OngoingAnimeNet\nIf you like join above channels.."
start_message_btn =[
    [
        ("🏖 Let's Goo 🏖")
    ]
]
choose_message_btn =[
    [
        ("🎀 SFW 🎀")
    ],
    [
        ("🔞 NSFW 🔞")
    ],
    [
        ("🏕 Home 🏕")
]]

sfw_btns = [
    [
     ("❤️ Wallpaper  ❤️"),("🧡 Mobile Wallpaper 🧡")
    ],
    [
     ("💙 Wallpaper v2 💙"),("💜 Coffee Arts 💜")
    ],
    [
     ("💛 Neko Arts 💛"),("💚 Neko 💚")
    ],
    [
     ("🖤 Wave 🖤"),("🤍 Tea 🤍")
    ],
    [
     ("🤎 Punch 🤎"),("💔 Poke 💔")
    ],
    [
     ("❤️‍🔥 Feed ❤️‍🔥"),("❤️‍🩹 Tickle ❤️‍🩹")
    ],
    [
     ("❣️ Pat ❣️"),("💕 Kiss 💕")
    ],
    [
     ("💞 Hug 💞"),("💓 Cuddle 💓")
    ],
[
     ("💝 Cry 💝"),("❤️ Slap ❤️")
    ],
[
     ("🧡 Lick 🧡"),("💛 Bite 💛")
    ],
[
     ("💚 Dance 💚"),("💙 Sleep 💙")
    ],
[
     ("💜 Like 💜"),("🖤 Kill 🖤")
    ],
[
     ("🤍 Nosebleed 🤍"),("🤎 Threaten 🤎")
    ],
[
     ("💔 Depression 💔"),("❤️‍🔥 Jahy Arts ❤️‍🔥")
    ],
[
     ("❤️‍🩹 Waifu ❤️‍🩹"),("❣️ Foxgirl ❣️")
    ],
[
     ("💕 Smug 💕"),("💞 Kanna 💞")
    ],
[
     ("💓 Holo 💓"),("💗 Kemonomimi 💗")
    ],
    [
        ("🔙")
    ],
    ]

nsfw_btns = [[
        ("❤️ Anal ❤️"),("❤️ Ass ❤️ ")
    ],
[
        ("🧡 BDSM 🧡"),("🧡 Cum 🧡 ")
    ],
[
        ("💛 Classic 💛"),("💛 Creampie 💛 ")
    ],
[
        ("💚 Manga 💚"),("💚 Femdom 💚 ")
    ],
[
        ("💙 Hentai 💙"),("💙 Incest 💙 ")
    ],
[
        ("💜 Masturbation 💜"),("💜 Public 💜")
    ],
[
        ("🖤 Ero 🖤"),("🖤 Orgy 🖤 ")
    ],
[
        ("🤍 Elves 🤍"),("🤍 Yuri 🤍 ")
    ],
[
        ("🤎 Pantsu 🤎"),("🤎 Glasses 🤎 ")
    ],
[
        ("💔 Cuckold 💔"),("💔 Blowjob 💔")
    ],
[
        ("❤️‍🔥 Boobjob❤️‍🔥"),("❤️‍🔥 Footjob ❤️‍🔥 ")
    ],
[
        ("❤️‍🩹 Boobs ❤️‍🩹"),("❤️‍🩹 Thighs ❤️‍🩹 ")
    ],
[
        ("❣️ Pussy ❣️"),("❣️Ahegao❣️ ")
    ],
[
        ("💕 Uniform 💕"),("💕 Gangbang💕 ")
    ],
[
        ("💞 Tentacles 💞"),("💞 GIF 💞")
    ],
[
        ("💓Neko💓"),("💓 Mobile Wallpaper💓 ")
    ],
[
        ("💗 ZettaiRyouiki 💗"),
    ],
[
        ("🔙")
    ],
]    
@app.on_message(filters.command("start"))
async def start(_, message: Message):
    text = start_message
    pic = "https://wallpapercave.com/dwp1x/wp6998898.png"
    reply_markup = ReplyKeyboardMarkup(start_message_btn,one_time_keyboard=True,resize_keyboard=True)
    await message.reply_photo(photo=pic,caption=start_message,reply_markup=reply_markup)

@app.on_message(filters.regex("🏕 Home 🏕"))
async def start_repl(_, message: Message):
    text = start_message
    pic = "https://wallpapercave.com/dwp1x/wp6998898.png"
    reply_markup = ReplyKeyboardMarkup(start_message_btn,one_time_keyboard=True,resize_keyboard=True)
    await message.reply_photo(photo=pic,caption=start_message,reply_markup=reply_markup)


@app.on_message(filters.regex("🏖 Let's Goo 🏖"))
async def start_repl(_, message: Message):
    chat_id = message.chat.id
    check_txt = "What Do You Want **SFW?** or **NSFW?**\n\n`Note:` **NSFW** Got Adult Content So Please Reconsider Your Choice kek!"
    check = ReplyKeyboardMarkup(choose_message_btn,one_time_keyboard=True,resize_keyboard=True)
    await app.send_message(chat_id,check_txt,reply_markup=check)

@app.on_message(filters.regex("🎀 SFW 🎀"))
async def sfw(_, message: Message):
    chat_id = message.chat.id
    picc = "https://wallpapercave.com/dwp1x/wp6245923.jpg"
    btns = ReplyKeyboardMarkup(sfw_btns,resize_keyboard=True)
    sfw_txt = "**Here Its The SFW Paradise**"
    await app.send_photo(chat_id,photo=picc,caption=sfw_txt,reply_markup=btns)

@app.on_message(filters.regex("🔞 NSFW 🔞"))
async def sfw(_, message: Message):
    chat_id = message.chat.id
    piccc = "https://wallpapercave.com/dwp1x/wp6998967.jpg"
    btns = ReplyKeyboardMarkup(nsfw_btns,resize_keyboard=True)
    sfw_txt = "**Here Its The NSFW World**\n\n`Note`: I guess you know what is this world kek"
    await app.send_photo(chat_id,photo=piccc,caption=sfw_txt,reply_markup=btns)
    
#------------------------- SFW--------------------------------------------------------#    
@app.on_message(filters.regex("❤️ Wallpaper  ❤️"))
async def n_wallpaper(_, message: Message):
    target = "wallpaper"
    print("working")
    await message.reply_photo(nekos.img(target),caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🧡 Mobile Wallpaper 🧡"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","mobileWallpaper")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💙 Wallpaper v2 💙"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","wallpaper")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💜 Coffee Arts 💜"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","coffee_arts")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💛 Neko Arts 💛"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","neko_arts")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💚 Neko 💚"))
async def n_wallpaper(_, message: Message):
    target = "neko"
    print("working")
    await message.reply_photo(nekos.img(target),caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🖤 Wave 🖤"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","wave")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🤍 Tea 🤍"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","tea")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🤎 Punch 🤎"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","punch")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💔 Poke 💔"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","poke")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️‍🔥 Feed ❤️‍🔥"))
async def n_wallpaper(_, message: Message):
    target = "feed"
    print("working")
    await message.reply_video(nekos.img(target),caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️‍🩹 Tickle ❤️‍🩹"))
async def n_wallpaper(_, message: Message):
    target = "tickle"
    print("working")
    await message.reply_video(nekos.img(target),caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❣️ Pat ❣️"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","pat")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💕 Kiss 💕"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","kiss")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💞 Hug 💞"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","hug")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💓 Cuddle 💓"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","cuddle")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💝 Cry 💝"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","cry")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️ Slap ❤️"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","slap")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🧡 Lick 🧡"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","lick")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💛 Bite 💛"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","bite")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💚 Dance 💚"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","dance")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💙 Sleep 💙"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","sleep")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")    

@app.on_message(filters.regex("💜 Like 💜"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","like")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")
    
@app.on_message(filters.regex("🖤 Kill 🖤"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","kill")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")    

@app.on_message(filters.regex("🤍 Nosebleed 🤍"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","nosebleed")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🤎 Threaten 🤎"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","threaten")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💔 Depression 💔"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","depression")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️‍🔥 Jahy Arts ❤️‍🔥"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","jahy_arts")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️‍🩹 Waifu ❤️‍🩹"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("nekos","waifu")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❣️ Foxgirl ❣️"))
async def n_wallpaper(_, message: Message):
    target = "fox_girl"
    print("working")
    await message.reply_photo(nekos.img(target),caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💕 Smug 💕"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("nekos","smug")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💞 Kanna 💞"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("nekobot","kanna")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💓 Holo 💓"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("nekobot","holo")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💗 Kemonomimi 💗"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("nekobot","kemonomimi")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🔙"))
async def start_repl(_, message: Message):
    chat_id = message.chat.id
    check_txt = "What Do You Want **SFW?** or **NSFW?**\n\n`Note:` **NSFW** Got Adult Content So Please Reconsider Your Choice kek!"
    check = ReplyKeyboardMarkup(choose_message_btn,one_time_keyboard=True,resize_keyboard=True)
    await app.send_message(chat_id,check_txt,reply_markup=check)


#------------------------- NSFW--------------------------------------------------------#
@app.on_message(filters.regex("🔙"))
async def start_repl(_, message: Message):
    chat_id = message.chat.id
    check_txt = "What Do You Want **SFW?** or **NSFW?**\n\n`Note:` **NSFW** Got Adult Content So Please Reconsider Your Choice kek!"
    check = ReplyKeyboardMarkup(choose_message_btn,one_time_keyboard=True,resize_keyboard=True)
    await app.send_message(chat_id,check_txt,reply_markup=check)

@app.on_message(filters.regex("❤️ Anal ❤️"))
async def n_wallpaper(_, message: Message):
    print("working")
    target = hmtai.get("hmtai","anal")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️ Ass ❤️"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","ass")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🧡 BDSM 🧡"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","bdsm")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🧡 Cum 🧡"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","cum")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💛 Classic 💛"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","classic")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💛 Creampie 💛"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","creampie")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💚 Manga 💚"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","manga")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💚 Femdom 💚"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","femdom")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💙 Hentai 💙"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","hentai")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💙 Incest 💙"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","incest")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💜 Masturbation 💜"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","masturbation")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💜 Public 💜"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","public")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🖤 Ero 🖤"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","ero")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🖤 Orgy 🖤"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","orgy")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🤍 Elves 🤍"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","elves")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🤍 Yuri 🤍"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","yuri")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🤎 Glasses 🤎"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","glasses")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💔 Cuckold 💔"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","cuckold")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("🤎 Pantsu 🤎"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","pantsu")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💔 Blowjob 💔"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","blowjob")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️‍🔥 Boobjob❤️‍🔥"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","boobjob")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️‍🔥 Footjob ❤️‍🔥"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","footjob")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️‍🩹 Boobs ❤️‍🩹"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","boobs")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❤️‍🩹 Thighs ❤️‍🩹"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","thighs")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❣️ Pussy ❣️"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","pussy")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("❣️Ahegao❣️"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","ahegao")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💕 Uniform 💕"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","uniform")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💕 Gangbang💕"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","gangbang")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💞 Tentacles 💞"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","tentacles")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💞 GIF 💞"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","gif")
    print("working")
    await message.reply_video(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💓Neko💓"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","nsfwNeko")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💓 Mobile Wallpaper💓"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","nsfwMobileWallpaper")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

@app.on_message(filters.regex("💗 ZettaiRyouiki 💗"))
async def n_wallpaper(_, message: Message):
    target = hmtai.get("hmtai","zettaiRyouiki")
    print("working")
    await message.reply_photo(target,caption ="Powered By: **@Otaku_Network**")

app.run()
print("Bot Started Successfully\n")
