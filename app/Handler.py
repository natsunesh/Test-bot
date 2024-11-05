from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


from app import Keyboards as kb



router =  Router()



@router.message(CommandStart())
async def start(message:Message):
    #await rq.set_user(message.from_user.id)
    await message.answer("Привет! Чего ищешь?" , reply_markup=kb.Main)

@router.message(F.text == "БД")
async def base_data(message: Message):
    await message.answer ("выберите ваш курс", reply_markup=kb.BaseData)

@router.message(F.text == "Алгоритмитизация")
async def base_data(message: Message):
    await message.answer ("выберите ваш курс", reply_markup=kb.Algoritm)

@router.message(F.text == "Проверить счёт")
async def cashe(message: Message):
    await message.answer(f"Ваш баланс: " , reply_markup= kb.cashe)

@router.message(F.text == "О боте")
async def about(message: Message):
    await message.answer("Этот бот предназначен для упрощения обучения базе данным и алгоритмитизации систем начиная от первого курса и заканчивая четвёртым. Считайте его вашим личным помощником :)   ")


##Курсы по БД
@router.callback_query(F.data == ("kbnote1"))
async def bnote1(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 1 курс по базе данных ", reply_markup= kb.bkurs1 )

@router.callback_query(F.data ==  ("kbnote2"))
async def bnote2(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 2 курс по базе данных ", reply_markup=kb.bkurs2 )

@router.callback_query(F.data == ("kbnote3"))
async def bnote3(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 3 курс по базе данных ", reply_markup=kb.bkurs3 )

@router.callback_query(F.data == ("kbnote4"))
async def bnote4(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 4 курс по базе данных ", reply_markup=kb.bkurs4 )

##Лекции 1 курса по БД
@router.callback_query(F.data == ("k1bnote1"))
async def bnote1(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 1 лекцию по базе данных " )

@router.callback_query(F.data == ("k1bnote2"))
async def bnote2(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 2 лекцию по базе данных ")

@router.callback_query(F.data == ("k1bnote3"))
async def bnote3(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 3 лекцию по базе данных ")

@router.callback_query(F.data == ("k1bnote4"))
async def bnote4(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 4 лекцию по базе данных ")


##Лекции 2 курса по БД
@router.callback_query(F.data == ("k2bnote1"))
async def bnote1(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 1 лекцию по базе данных ")

@router.callback_query(F.data == ("k2bnote2"))
async def bnote2(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 2 лекцию по базе данных ")

@router.callback_query(F.data == ("k2bnote3"))
async def bnote3(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 3 лекцию по базе данных ")

@router.callback_query(F.data == ("k2bnote4"))
async def bnote4(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 4 лекцию по базе данных ")


##Лекции 3 курса по БД
@router.callback_query(F.data == ("k3bnote1"))
async def bnote1(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 1 лекцию по базе данных ")

@router.callback_query(F.data == ("k3bnote2"))
async def bnote2(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 2 лекцию по базе данных ")

@router.callback_query(F.data == ("k3bnote3"))
async def bnote3(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 3 лекцию по базе данных ")

@router.callback_query(F.data == ("k3bnote4"))
async def bnote4(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 4 лекцию по базе данных ")


##Лекции 4 курса по БД
@router.callback_query(F.data == ("k4bnote1"))
async def bnote1(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 1 лекцию по базе данных ")

@router.callback_query(F.data == ("k4bnote2"))
async def bnote2(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 2 лекцию по базе данных ")

@router.callback_query(F.data == ("k4bnote3"))
async def bnote3(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 3 лекцию по базе данных ")

@router.callback_query(F.data == ("k4bnote4"))
async def bnote4(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 4 лекцию по базе данных ")


##Курсы по Алгоритмам
@router.callback_query(F.data == ("kanote1"))
async def bnote1(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 1 курс по алгоритмитизации систем ", reply_markup=kb.akurs1)

@router.callback_query(F.data == ("kanote2"))
async def bnote2(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 2 курс по алгоритмитизации систем ", reply_markup=kb.akurs2 )

@router.callback_query(F.data == ("kanote3"))
async def bnote3(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 3 курс по алгоритмитизации систем ", reply_markup=kb.akurs3 )

@router.callback_query(F.data == ("kanote4"))
async def bnote4(callback: CallbackQuery):
    await callback.message.answer(" вы выбрали 4 курс по алгоритмитизации систем ", reply_markup=kb.akurs4 )

#Лекции 1 курса
@router.callback_query(F.data == ("k1anote1"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 1 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k1anote2"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 2 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k1anote3"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 3 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k1anote4"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 4 лекцию по алгоритмитизации ")

#Лекции 2 курса

@router.callback_query(F.data == ("k2anote1"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 1 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k2anote2"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 2 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k2anote3"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 3 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k2anote4"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 4 лекцию по алгоритмитизации ")

#Лекции 3 курса

@router.callback_query(F.data == ("k3anote1"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 1 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k3anote2"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 2 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k3anote3"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 3 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k3anote4"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 4 лекцию по алгоритмитизации ")
    
#Лекции 4 курса

@router.callback_query(F.data == ("k4anote1"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 1 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k4anote2"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 2 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k4anote3"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 3 лекцию по алгоритмитизации ")

@router.callback_query(F.data == ("k4anote4"))
async def k1anote1(callback: CallbackQuery):
    await callback.answer(" Вы выбрали 4 лекцию по алгоритмитизации ")