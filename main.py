import asyncio
import logging
import random
import json

from aiogram import types, Dispatcher, Bot
from aiogram.filters.command import Command

from dataparser import DataParser
from utils import get_next_date, get_current_date, get_name
from config import (token,
                    API,
                    answer_preset_current,
                    answer_preset_next,
                    names, usernames)


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()
table = DataParser(API)


async def init():
    await dp.start_polling(bot)


@dp.callback_query()
async def callback(call: types.CallbackQuery):
    if call.message.from_user.username != call.data.replace('OK_', ''):
        await call.answer('Кажется не Вы указаны в сообщении. Зачем тогда вообще нажали на кнопку?', show_alert=True)
    else:
        await call.answer('Приятного дежурства!', show_alert=True)



@dp.message(Command('current'))
async def current(message: types.Message):
    date = get_current_date()
    name = get_name(date)
    username = usernames[names.index(name)]

    kblist = [[types.InlineKeyboardButton(text='👍', callback_data=f'OK_{names.index(name)}')]]
    mk = types.InlineKeyboardMarkup(inline_keyboard=kblist)

    if username:
        await message.answer(f'{random.choice(answer_preset_current)}\n<a href="t.me/{username}">{name}</a>',
                             parse_mode='HTML', reply_markup=mk, disable_web_page_preview=True)
    else:
        await message.answer(f'{random.choice(answer_preset_current)}{name}', reply_markup=mk)




@dp.message(Command('next'))
async def next(message: types.Message):
    date = get_next_date()
    name = get_name(date)
    username = usernames[names.index(name)]

    kblist = [[types.InlineKeyboardButton(text='👍', callback_data=f'OK_{names.index(name)}')]]
    mk = types.InlineKeyboardMarkup(inline_keyboard=kblist)

    if username:
        await message.answer(f'{random.choice(answer_preset_next)}\n<a href="t.me/{username}">{name}</a>',
                             parse_mode='HTML', disable_web_page_preview=True, reply_markup=mk)
    else:
        await message.answer(f'{random.choice(answer_preset_current)}{name}', reply_markup=mk)


if __name__ == '__main__':
    asyncio.run(init())
