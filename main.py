from aiogram.types import Message, CallbackQuery
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command

from keyboards.menu import main_kb
from keyboards.tasks import tasks_kb, module_3_kb
from keyboards.learn import learn_kb
from bot_token import TOKEN

dp = Dispatcher()
bot = Bot(token=TOKEN)


@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(text='Выберите раздел: ', reply_markup=main_kb)


@dp.callback_query(lambda callback: callback.data)
async def process_callback(callback: CallbackQuery):
    data = callback.data
    print(callback)
    if data == 'Menu':
        await bot.answer_callback_query(callback.id)
        await bot.edit_message_text(text='Выберите раздел: ',
                                    chat_id=callback.from_user.id,
                                    message_id=callback.message.message_id,
                                    reply_markup=main_kb)
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


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
