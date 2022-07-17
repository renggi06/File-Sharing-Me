#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys, time

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, FORCE_SUB_CHANNEL2

StartTime = time.time()

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot Tidak Dapat Mengekspor Tautan Undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Eror : Pastikan Bot Kamu adalah Admin di Channel Force Subs, \nPeriksa Kembali. ID Channel Subs Kamu Pada Channel 1 ({FORCE_SUB_CHANNEL} )")
                self.LOGGER(__name__).info("Bot Berhenti! ☹️")
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot Tidak Dapat Mengekspor Tautan Undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Eror : Pastikan Bot Kamu adalah Admin di Channel Force Subs, \nPeriksa Kembali. ID Channel Subs Kamu Pada Channel 2 ( {FORCE_SUB_CHANNEL2} )")
                self.LOGGER(__name__).info("Bot Berhenti! ☹️")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Kirim Pesan.")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Eror : Pastikan Bot Kamu adalah Admin di Channel Database, \nPeriksa Kembali. ID Channel Database Kamu {CHANNEL_ID}")
            self.LOGGER(__name__).info("Bot Berhenti! ☹️")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info("Bot Berjalan 😎💯")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Berhenti! ☹️")
