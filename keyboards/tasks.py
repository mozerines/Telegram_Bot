from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tasks_kb_buttons = [
    [InlineKeyboardButton(text='Модуль 3', callback_data='Module 3')],
    [InlineKeyboardButton(text='Назад 🔙', callback_data='Menu')]
]

tasks_kb = InlineKeyboardMarkup(inline_keyboard=tasks_kb_buttons, row_width=1)

module_3_kb_buttons = ([
    [
        InlineKeyboardButton(text=f'4 Урок', url=f'https://telegra.ph/M3-U4-02-09'),
        InlineKeyboardButton(text='5 Урок', url='https://telegra.ph/M3-U5-02-13'),
        InlineKeyboardButton(text='6 Урок', url='https://telegra.ph/M3-U6-02-15'),
    ],
    [
        InlineKeyboardButton(text='7 Урок', url='https://telegra.ph/M3-U7-02-20'),
        InlineKeyboardButton(text='8 Урок', url='https://telegra.ph/M3-U8-02-27'),
        InlineKeyboardButton(text='9 Урок', url='https://telegra.ph/M3-U9-03-05')
    ],
    [
        InlineKeyboardButton(text='10 Урок', url='https://telegra.ph/M3-U10-03-07')],
        [InlineKeyboardButton(text='Назад 🔙', callback_data='Tasks')]

])

module_3_kb = InlineKeyboardMarkup(inline_keyboard=module_3_kb_buttons, row_width=3)
