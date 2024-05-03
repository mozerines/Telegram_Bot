from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#callback_data потребуется нам при обработке нажатий на кнопки
main_kb_buttons = [
    [InlineKeyboardButton(text='Задания 📝', callback_data='Tasks')],
    [InlineKeyboardButton(text='Дополнительная практика 📚', callback_data='Learn')],
    [InlineKeyboardButton(text='Полезные ссылки', callback_data='Useful_links')]
]

main_kb = InlineKeyboardMarkup(inline_keyboard=main_kb_buttons, row_width=1)
