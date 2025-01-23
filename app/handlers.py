from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

def cmd_start(message):
    router.message(CommandStart(), cmd_start)
    message.answer("вечер в хату", reply_markup=kb.main)
    message.reply("часик в радость")

def cmd_help(message):
    message.answer("Бог в помощь бродяга")

def nice(message):
    message.answer("Вилкой в глаз или в жопу раз?")