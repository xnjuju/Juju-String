from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

{} dibuat untuk Membantu Anda Mengambil String Session Telethon atau Pyrogram dengan Mudah dan AMAN!
━━━━━━━━━━━━━━━━━━━━━━━━

Jika Anda Tidak Mempercayai Bot Ini,
1) Berhenti Membaca Pesan Ini
2) Hapus Obrolan dan Blokir Bot Ini
━━━━━━━━━━━━━━━━━━━━━━━━
Managed By @xnotzu
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("𝗦𝗧𝗔𝗥𝗧 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("𝗦𝗧𝗔𝗥𝗧 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("𝗦𝗧𝗔𝗥𝗧 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡", callback_data="generate")],
        [
            InlineKeyboardButton("𝗛𝗘𝗟𝗣", callback_data="help"),
            InlineKeyboardButton("𝗔𝗕𝗢𝗨𝗧", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
✨ **Perintah yang tersedia** ✨

/about - Tentang Bot ini
/start - Mulai Bot
/generate - Mulai Mengambil String
/cancel - Batalkan Proses Pengambilan String
/restart - Mulai Ulang Proses Pengambilan String
"""

    # About Message
    ABOUT = """
**Tentang Bot ini** 

{} dibuat untuk Membantu Anda Mengambil String Session Telethon atau Pyrogram dengan Mudah dan AMAN!

Source Code : [ᴊᴜ ᴜꜱᴇʀʙᴏᴛ](https://t.me/JuUserbot)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)

Develoved by @xnjuju
    """
