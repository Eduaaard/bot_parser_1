from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from data.loader import bot, manager
from keyboards.default import start_menu


@bot.message_handler(func=lambda msg: msg.text == "Регистрация")
def start_register(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Напишите ваше имя")
    bot.register_next_step_handler(message, get_name)


def get_name(message: Message):
    chat_id = message.chat.id

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(KeyboardButton(text="Отправить контакт", request_contact=True))

    bot.send_message(chat_id, "Отправь мне свой контакт", reply_markup=kb)
    bot.register_next_step_handler(message, register, message.text)


def register(message: Message, name):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number

    manager.user.add_user(name, phone_number, chat_id)
    bot.send_message(chat_id, "Регистрация закончилась", reply_markup=start_menu(chat_id))



