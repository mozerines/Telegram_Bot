from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ul_kb_buttons = [
    [InlineKeyboardButton(text='Установка Python',
                          url='https://www.python.org/downloads/')],
    [InlineKeyboardButton(text='Установка PyCharm Community Edition',
                          url='https://www.jetbrains.com/pycharm/download/?section=windows')],
    [InlineKeyboardButton(text='GitHub',
                          url='https://github.com')],
    [InlineKeyboardButton(text='Назад 🔙', callback_data='Menu')]
]

ul_kb = InlineKeyboardMarkup(inline_keyboard=ul_kb_buttons)
