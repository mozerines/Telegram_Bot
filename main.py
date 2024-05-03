from aiogram.types import Message, CallbackQuery
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command

from keyboards.menu import main_kb
from keyboards.tasks import tasks_kb, module_3_kb
from keyboards.learn import learn_kb
from keyboards.useful_links import ul_kb
from bot_token import TOKEN

dp = Dispatcher()
bot = Bot(token=TOKEN)


@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(text='Выберите раздел: ', reply_markup=main_kb)


# Здесь нам и понадобится callback_data, которую мы прописывали ранее в нажатиях на кнопки
@dp.callback_query(lambda callback: callback.data)
async def process_callback(callback: CallbackQuery):
    data = callback.data
    # Возврат в главное меню при нажатии на кнопку "Назад 🔙"
    if data == 'Menu':
        await bot.answer_callback_query(callback.id)
        await bot.edit_message_text(text='Выберите раздел: ',
                                    chat_id=callback.from_user.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=main_kb)
    # Переход к клавиатуре с модулями при нажатии на кнопку "Задания 📝"
    if data == 'Tasks':
        await bot.answer_callback_query(callback.id)
        await bot.edit_message_text(text='Выберите модуль: ',
                                    chat_id=callback.from_user.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=tasks_kb)
    if data == 'Module 3':
        await bot.answer_callback_query(callback.id)
        await bot.edit_message_text(text='Выберите урок: ',
                                    chat_id=callback.from_user.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=module_3_kb
                                    )
    if data == 'Learn':
        await bot.answer_callback_query(callback.id)
        await bot.edit_message_text(text='Сайты для дополнительной практики и обучения: ',
                                    chat_id=callback.from_user.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=learn_kb
                                    )
    if data == 'Useful_links':
        await bot.answer_callback_query(callback.id)
        await bot.edit_message_text(text='Полезные ссылки',
                                    chat_id=callback.from_user.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=ul_kb)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
