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


def categories_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    categories = manager.category.get_categories()
    markup.row(
        KeyboardButton(text="Назад")
    )
    buttons = [KeyboardButton(text=category) for category in categories]

    markup.add(*buttons)
    return markup


def get_products_by_category(category_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    products = manager.product.get_products_by_category(category_id)
    markup.row(
        KeyboardButton(text="Назад")
    )
    buttons = [KeyboardButton(text=product) for product in products]

    markup.add(*buttons)
    return markup


