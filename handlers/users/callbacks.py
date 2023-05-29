from telebot.types import CallbackQuery
from data.loader import bot, manager
from keyboards.inline import to_cart_menu


@bot.callback_query_handler(func=lambda call: "prev" in call.data)
def prev_products(callback: CallbackQuery):
    chat_id = callback.message.chat.id

    _, product_id, quantity = callback.data.split("_")

    product_total_quantity = manager.product.get_product_quantity(int(product_id))
    if int(quantity) > product_total_quantity:
        return

    bot.edit_message_reply_markup(
        chat_id,
        message_id=callback.message.message_id,
        reply_markup=to_cart_menu(
            product_id=int(product_id),
            current_quantity=int(quantity)
        )
    )


@bot.callback_query_handler(func=lambda call: "next" in call.data)
def next_products(callback: CallbackQuery):
    chat_id = callback.message.chat.id

    _, product_id, quantity = callback.data.split("_")

    product_total_quantity = manager.product.get_product_quantity(int(product_id))
    if int(quantity) > product_total_quantity:
        return

    bot.edit_message_reply_markup(
        chat_id,
        message_id=callback.message.message_id,
        reply_markup=to_cart_menu(
            product_id=int(product_id),
            current_quantity=int(quantity)
        )
    )


@bot.callback_query_handler(func=lambda call: "cart" in call.data)
def add_to_cart(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    # print(callback.data)
    _, product_id, quantity = callback.data.split("_")
