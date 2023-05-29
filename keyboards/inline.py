from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.loader import manager


def to_cart_menu(product_id, current_quantity=0):
    markup = InlineKeyboardMarkup()

    product_quantity = manager.product.get_product_quantity(product_id)

    markup.add(
        InlineKeyboardButton(text="<", callback_data=f"prev_{product_id}_{current_quantity - 1}"),
        InlineKeyboardButton(text=f"{current_quantity}/{product_quantity}", callback_data=f"empty?"),
        InlineKeyboardButton(text=">", callback_data=f"prev_{product_id}_{current_quantity + 1}"),
        InlineKeyboardButton(text="Добавить в корзину🛒", callback_data=f"cart_{product_id}_{current_quantity}")
    )
    return markup


