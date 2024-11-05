from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                             InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder


Main =  ReplyKeyboardMarkup (keyboard = [[KeyboardButton(text= 'БД')],
                                          [KeyboardButton(text = "Алгоритмитизация")],
                                          [KeyboardButton(text= "Проверить счёт"),
                                          KeyboardButton(text= "О боте")]],
                                resize_keyboard=True, 
                                input_field_placeholder="Выберите кнопку")

BaseData = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Курс 1" , callback_data="kbnote1")],
                                                [InlineKeyboardButton(text= "Курс 2", callback_data="kbnote2")],
                                                [InlineKeyboardButton(text= "Курс 3", callback_data="kbnote3")],
                                                [InlineKeyboardButton(text= "Курс 4 ", callback_data="kbnote4")]])

bkurs1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Лекция 1" , callback_data="k1bnote1")],
                                                [InlineKeyboardButton(text= "Лекция 2", callback_data="k1bnote2")],
                                                [InlineKeyboardButton(text= "Лекция 3", callback_data="k1bnote3")],
                                                [InlineKeyboardButton(text= "Лекция 4 ", callback_data="k1bnote4")]])

bkurs2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Лекция 1" , callback_data="k2bnote1")],
                                                [InlineKeyboardButton(text= "Лекция 2", callback_data="k2bnote2")],
                                                [InlineKeyboardButton(text= "Лекция 3", callback_data="k2bnote3")],
                                                [InlineKeyboardButton(text= "Лекция 4 ", callback_data="k2bnote4")]])

bkurs3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Лекция 1" , callback_data="k3bnote1")],
                                                [InlineKeyboardButton(text= "Лекция 2", callback_data="k3bnote2")],
                                                [InlineKeyboardButton(text= "Лекция 3", callback_data="k3bnote3")],
                                                [InlineKeyboardButton(text= "Лекция 4 ", callback_data="k3bnote4")]])

bkurs4 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Лекция 1" , callback_data="k4bnote1")],
                                                [InlineKeyboardButton(text= "Лекция 2", callback_data="k4bnote2")],
                                                [InlineKeyboardButton(text= "Лекция 3", callback_data="k4bnote3")],
                                                [InlineKeyboardButton(text= "Лекция 4 ", callback_data="k4bnote4")]])

Algoritm = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Курс 1" , callback_data="kanote1")],
                                                [InlineKeyboardButton(text= "Курс 2", callback_data="kanote2")],
                                                [InlineKeyboardButton(text= "Курс 3", callback_data="kanote3")],
                                                [InlineKeyboardButton(text= "Курс 4 ", callback_data="kanote4")]])

akurs1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Лекция 1" , callback_data="k1anote1")],
                                                [InlineKeyboardButton(text= "Лекция 2", callback_data="k1anote2")],
                                                [InlineKeyboardButton(text= "Лекция 3", callback_data="k1anote3")],
                                                [InlineKeyboardButton(text= "Лекция 4 ", callback_data="k1anote4")]])

akurs2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Лекция 1" , callback_data="k2anote1")],
                                                [InlineKeyboardButton(text= "Лекция 2", callback_data="k2anote2")],
                                                [InlineKeyboardButton(text= "Лекция 3", callback_data="k2anote3")],
                                                [InlineKeyboardButton(text= "Лекция 4 ", callback_data="k2anote4")]])

akurs3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Лекция 1" , callback_data="k3anote1")],
                                                [InlineKeyboardButton(text= "Лекция 2", callback_data="k3anote2")],
                                                [InlineKeyboardButton(text= "Лекция 3", callback_data="k3anote3")],
                                                [InlineKeyboardButton(text= "Лекция 4 ", callback_data="k3anote4")]])

akurs4 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Лекция 1" , callback_data="k4anote1")],
                                                [InlineKeyboardButton(text= "Лекция 2", callback_data="k4anote2")],
                                                [InlineKeyboardButton(text= "Лекция 3", callback_data="k4anote3")],
                                                [InlineKeyboardButton(text= "Лекция 4 ", callback_data="k4anote4")]])

cashe = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text= "Пополнить" , callback_data="replenish")],
                                                [InlineKeyboardButton(text= "Служба поддежки", callback_data="support")]])




