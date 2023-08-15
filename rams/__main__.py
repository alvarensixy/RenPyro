import time
import importlib 
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from rens import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from rens.split.misc import create_botlog, git, heroku
from rens.modules import ALL_MODULES

MSG_ON = """
🔥 **RenPyro-Bot Aktif** 🔥
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
🤖 **Userbot Version -** `{}`
⌨️ **Ketik** `{}ren` **untuk check Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""
MSG_BOT = (f"**Ren Pyro Assistant**\nis alive...")


async def main():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"rens.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("nguyungg")
            await bot.join_chat("rensixy")
            await bot.join_chat("AnonymousChatGroupIND")
            await bot.join_chat("senaex")
            ids.append(bot.me.id)
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
                await app.send_message(BOTLOG_CHATID, MSG_BOT)
            except BaseException:
                pass
            LOGGER("rens").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("master").warning(a)
    LOGGER("rens").info(f"RenPyro-Bot v{BOT_VER} [RenPyro Sudah aktif ✅]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("rens").info("Starting RenPyro-Bot")
    install()
    heroku()
    LOOP.run_until_complete(main())
