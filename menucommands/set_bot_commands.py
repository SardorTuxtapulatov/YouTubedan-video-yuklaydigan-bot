from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/count", description="Assalomu alaykum bu SIFAT o'quv markazi o'quvchisi To'xtapulatov Sardor yaratgan \n Admin:@Sardor_Tuxtapulatov \nYosh:15yosh\n O'quv Markaz:SIFAT-o'quv markazi"),
        BotCommand(command="/admin", description="Admin panel"),

    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())