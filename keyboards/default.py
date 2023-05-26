from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from data.loader import manager


def start_menu(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    user_id = manager.user.get_user_id(chat_id)
    if not user_id:
        markup.row(
            KeyboardButton(text="Регистрация")
        )
        return markup

    markup.row(
        KeyboardButton(text="Смотреть товары"),
        KeyboardButton(text="Корзина")
    )
    return markup

