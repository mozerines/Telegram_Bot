from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

learn_kb_buttons = [
    [InlineKeyboardButton(text='Питонтьютор', url='https://pythontutor.ru')],
    [InlineKeyboardButton(text='Назад 🔙', callback_data='Menu')]
]

learn_kb = InlineKeyboardMarkup(inline_keyboard=learn_kb_buttons)
