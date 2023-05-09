from aiogram import Bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import  Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from settings import TELEGRAM_TOKEN_TOKEN
from settings import support_ids
import random

bot = Bot(token=TELEGRAM_TOKEN_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

support_callback = CallbackData("ask_support", "messages", "user_id", "as_user")
cancel_support = CallbackData("cancel_support", "user_id")


@dp.message_handler(Command("start"))
async def ask_support(message: types.Message):
    text = 'Хотите написать сообщение Техподдержке? Нажмите на кнопку ниже!'
    keyboard = await support_keyboard(messages='one')
    await message.answer(text, reply_markup=keyboard)

@dp.callback_query_handler(support_callback.filter(messages='one'))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    user_id = int(callback_data.get("user_id"))
    
    await call.message.answer('Пришлите сообщение')
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)

@dp.message_handler(state="wait_for_support_message",content_types=types.ContentTypes.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data['second_id']

    await bot.send_message(second_id, "Вам пришло письмо, Ответь нажав на кнопку снизу")
    keyboard = await support_keyboard(messages='one', user_id=message.from_user.id)
    await message.copy_to(second_id, reply_markup=keyboard)

    await message.answer('Вы отправили это сообщение')
    await state.reset_state()
    



async def check_support_available(support_id):
    state = dp.current_state(chat=support_id, user=support_id)
    state_str = str(
        await state.get_state()
    )
    if state_str == "in_support":
        return
    else:
        return support_id


async def get_support_manager():
    random.shuffle(support_ids)
    for support_id in support_ids:
        support_id = await check_support_available(support_id)
        if support_id:
            return support_id
        else:
            return


async def support_keyboard(messages, user_id=None):
    if user_id:
        contact_id = int(user_id)
        as_user = 'no'
        text = 'ответить пользователю'
    else:
        contact_id = await get_support_manager()
        as_user = 'yes'
        if messages == "many" and contact_id is None:
            return False
        elif messages == "one" and contact_id is None:
            contact_id = random.choice(support_ids)   
        if messages == 'one':
            text = 'Написать одно сообщение в техподдержку'
        else:
            text = 'Написать оператору'

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            text=text,
            callback_data=support_callback.new(
                messages=messages,
                user_id=contact_id,
                as_user=as_user
             )
        )
    )

    if messages == 'many':
        keyboard.add(
            types.InlineKeyboardButton(
            text='Завершить сеанс',
            callback_data=cancel_support.new(
            user_id=contact_id
            )
            )
        )
    return keyboard




if __name__ == '__main__':
    executor.start_polling(dp)