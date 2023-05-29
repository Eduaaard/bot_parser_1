from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from data.loader import bot, manager
from keyboards.default import start_menu, categories_menu, get_products_by_category
from keyboards.inline import to_cart_menu


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


@bot.message_handler(func=lambda msg: msg.text == "Смотреть товары")
def show_categories_menu(message: Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Выберите категорию 👉🏿👌🏿", reply_markup=categories_menu() )


@bot.message_handler(func=lambda msg: msg.text in manager.category.get_categories() or msg.text == "Назад" )
def show_category(message:Message):
    chat_id = message.chat.id
    if message.text == "Назад":
        bot.send_message(chat_id, "Шаг назад", reply_markup=start_menu(chat_id))
        return

    category_id = manager.category.get_category_id(message.text)

    bot.send_message(chat_id, f"Товары категории: {message.text}", reply_markup=get_products_by_category(category_id))
    bot.register_next_step_handler(message, get_product_info)


def get_product_info(message: Message):
    chat_id = message.chat.id
    if message.text == "Назад":
        show_categories_menu(message)
        return

    product_info = manager.product.get_product_info(message.text)
    if not product_info:
        bot.send_message(chat_id, "Такого товара не существует, СУС")
        bot.register_next_step_handler(message, get_product_info)
        return

    product_id, img_url, price, quantity, description = product_info

    bot.send_photo(chat_id, photo=img_url, caption=f"""
    {message.text}
Цена: {price} сум
Количество: {quantity}
{description[90:300]}
""", reply_markup=to_cart_menu(product_id))


