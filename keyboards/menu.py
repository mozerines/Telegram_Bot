from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_kb_buttons = [
    [InlineKeyboardButton(text='Задания 📝', callback_data='Tasks')],
    [InlineKeyboardButton(text='Дополнительная практика 📚', callback_data='Learn')]
]

main_kb = InlineKeyboardMarkup(inline_keyboard=main_kb_buttons, row_width=1)
