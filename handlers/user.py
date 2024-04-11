import datetime
import random

from aiogram.types import LabeledPrice, Message,ReplyKeyboardMarkup,KeyboardButton, PreCheckoutQuery, ContentType, ShippingQuery, ShippingOption
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters import ContentTypeFilter
from services.sql import DataBase
import config
import time
from bot import bot, dp
from config import Config
predlog = []
db = DataBase()


@dp.message_handler(Command('start'))
async def start(message: Message):
    print(message.chat.id)
    try:
        markup = ReplyKeyboardMarkup()
        katalog = KeyboardButton('Каталог')
        qr = KeyboardButton('QR_Code')
        helps = KeyboardButton('Помощь')
        markup.row(katalog)
        markup.row(qr,helps)
        admins = ReplyKeyboardMarkup()
        spisanie = KeyboardButton('Списание товара')
        add_price = KeyboardButton('Добавить товар')
        del_price = KeyboardButton('Удалить товар')
        accouting = KeyboardButton('Ввод/Вывод учета')
        exitWork = KeyboardButton('Завершить работу')
        admins.row(katalog,spisanie)
        admins.row(add_price,del_price,accouting)
        admins.row(exitWork)

        if message.chat.id == config.get_admins(message.chat.id):
            await bot.send_message(message.chat.id, f'Добро пожаловать, Администратор {message.from_user.first_name} {message.from_user.last_name}',reply_markup=admins)
            await db.create_tableSum(f'{message.chat.id}')
            await db.create_tableSpis(f'{message.chat.id}')
            await bot.send_message(message.chat.id, f'База-данных: magasin{message.chat.id} создана для отслеживания суммы, и База-данных:spis{message.chat.id} для списанных товаров')
            await bot.send_message(message.chat.id,f'Предупреждение: за завершения работы раньше чем 22 грозит штраф, база- данных не резиновая и с радостью накидает вам ошибок и за отключения бота от сервера грозит штраф, так как сессия считает весь доход а по окончанию сессии доход обнуляется, если сессия окончилась непредвиденно, обратитесь за помощью к главному программисту c причиной и заголовком "ЛОГ"')
        elif message.chat.id != config.get_admins(message.chat.id):
            await bot.send_message(message.chat.id, f'Добро пожаловать!!! {message.from_user.first_name} {message.from_user.last_name}. Ваше сегодняшнее предложение: {config.get_pledlog()}',reply_markup=markup)
    except Exception as e:
        await bot.send_message(message.chat.id,f'{e}')

