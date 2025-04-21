from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


from app import Keyboards as kb



router =  Router()




@router.message(CommandStart())
async def start(message:Message):
    from app.DataBase import requests
    try:
        await requests.add_user(message.from_user.id, message.from_user.id)
        await message.answer("Привет! Чего ищешь?" , reply_markup=kb.Main)
    except ValueError as e:
        await message.answer(str(e))

@router.message(F.text == "БД")
async def base_data(message: Message):
    await message.answer("выберите ваш курс", reply_markup=kb.BaseData)

@router.message(F.text == "Алгоритмитизация")
async def algoritm_data(message: Message):
    await message.answer ("выберите ваш курс", reply_markup=kb.Algoritm)

@router.message(F.text == "Проверить счёт")
async def cashe(message: Message):
    from app.DataBase import requests
    user = await requests.get_user(message.from_user.id)
    if user:
        await message.answer(f"Ваш баланс: {user.balance}", reply_markup=kb.cashe)
    else:
        await message.answer("Пользователь не найден", reply_markup=kb.cashe)

@router.message(F.text == "О боте")
async def about(message: Message):
    await message.answer("Этот бот предназначен для упрощения обучения базе данным и алгоритмитизации систем начиная от первого курса и заканчивая четвёртым. Считайте его вашим личным помощником :)   ")

#Переход в начало
@router.message(F.text == "В главное меню")
async def in_started (message: Message):
    await message.answer("Главное меню", reply_markup=kb.Main)

# Обработчик для кнопки "В главное меню" в инлайн-клавиатурах
@router.callback_query(F.data == "in_started")
async def in_started_callback(callback: CallbackQuery):
    # Determine the previous state and provide the appropriate reply_markup
    if callback.data == "kbnote1":
        await callback.message.answer("Выберите ваш курс", reply_markup=kb.BaseData)
    elif callback.data == "kbnote2":
        await callback.message.answer("Выберите ваш курс", reply_markup=kb.BaseData)
    elif callback.data == "kbnote3":
        await callback.message.answer("Выберите ваш курс", reply_markup=kb.BaseData)
    elif callback.data == "kbnote4":
        await callback.message.answer("Выберите ваш курс", reply_markup=kb.BaseData)
    elif callback.data == "kanote1":
        await callback.message.answer("Выберите ваш курс", reply_markup=kb.Algoritm)
    elif callback.data == "kanote2":
        await callback.message.answer("Выберите ваш курс", reply_markup=kb.Algoritm)
    elif callback.data == "kanote3":
        await callback.message.answer("Выберите ваш курс", reply_markup=kb.Algoritm)
    elif callback.data == "kanote4":
        await callback.message.answer("Выберите ваш курс", reply_markup=kb.Algoritm)
    else:
        await callback.message.answer("Главное меню", reply_markup=kb.Main)
    await callback.answer()

##Курсы по БД
@router.callback_query(F.data == ("kbnote1"))
async def bnote1(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    course = course_info["kbnote1"]
    await callback.message.edit_text(f"{course['title']}\n\n{course['description']}", reply_markup=kb.bkurs1)

@router.callback_query(F.data ==  ("kbnote2"))
async def bnote2(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    course = course_info["kbnote2"]
    await callback.message.edit_text(f"{course['title']}\n\n{course['description']}", reply_markup=kb.bkurs2)

@router.callback_query(F.data == ("kbnote3"))
async def bnote3(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    course = course_info["kbnote3"]
    await callback.message.edit_text(f"{course['title']}\n\n{course['description']}", reply_markup=kb.bkurs3)

@router.callback_query(F.data == ("kbnote4"))
async def bnote4(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    course = course_info["kbnote4"]
    await callback.message.edit_text(f"{course['title']}\n\n{course['description']}", reply_markup=kb.bkurs4)

##Лекции 1 курса по БД
@router.callback_query(F.data == ("k1bnote1"))
async def bnote1_k1b(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote1"]["lectures"]["k1bnote1"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k1bnote2"))
async def bnote2(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote1"]["lectures"]["k1bnote2"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k1bnote3"))
async def bnote3(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote1"]["lectures"]["k1bnote3"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k1bnote4"))
async def bnote4(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote1"]["lectures"]["k1bnote4"]
    await callback.message.answer(lecture)


##Лекции 2 курса по БД
@router.callback_query(F.data == ("k2bnote1"))
async def bnote1(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote2"]["lectures"]["k2bnote1"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k2bnote2"))
async def bnote2(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote2"]["lectures"]["k2bnote2"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k2bnote3"))
async def bnote3(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote2"]["lectures"]["k2bnote3"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k2bnote4"))
async def bnote4(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote2"]["lectures"]["k2bnote4"]
    await callback.message.answer(lecture)


##Лекции 3 курса по БД
@router.callback_query(F.data == ("k3bnote1"))
async def bnote1(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote3"]["lectures"]["k3bnote1"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k3bnote2"))
async def bnote2(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote3"]["lectures"]["k3bnote2"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k3bnote3"))
async def bnote3(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote3"]["lectures"]["k3bnote3"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k3bnote4"))
async def bnote4(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote3"]["lectures"]["k3bnote4"]
    await callback.message.answer(lecture)


##Лекции 4 курса по БД
@router.callback_query(F.data == ("k4bnote1"))
async def bnote1(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote4"]["lectures"]["k4bnote1"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k4bnote2"))
async def bnote2(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote4"]["lectures"]["k4bnote2"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k4bnote3"))
async def bnote3(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote4"]["lectures"]["k4bnote3"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k4bnote4"))
async def bnote4(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kbnote4"]["lectures"]["k4bnote4"]
    await callback.message.answer(lecture)


##Курсы по Алгоритмам
@router.callback_query(F.data == ("kanote1"))
async def bnote1(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    course = course_info["kanote1"]
    await callback.message.edit_text(f"{course['title']}\n\n{course['description']}", reply_markup=kb.akurs1)

@router.callback_query(F.data == ("kanote2"))
async def bnote2(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    course = course_info["kanote2"]
    await callback.message.edit_text(f"{course['title']}\n\n{course['description']}", reply_markup=kb.akurs2)

@router.callback_query(F.data == ("kanote3"))
async def bnote3(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    course = course_info["kanote3"]
    await callback.message.edit_text(f"{course['title']}\n\n{course['description']}", reply_markup=kb.akurs3)

@router.callback_query(F.data == ("kanote4"))
async def bnote4(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    course = course_info["kanote4"]
    await callback.message.edit_text(f"{course['title']}\n\n{course['description']}", reply_markup=kb.akurs4)

#Лекции 1 курса
@router.callback_query(F.data == ("k1anote1"))
async def k1anote1_k1a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote1"]["lectures"]["k1anote1"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k1anote2"))
async def k1anote2_k1a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote1"]["lectures"]["k1anote2"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k1anote3"))
async def k1anote3_k1a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote1"]["lectures"]["k1anote3"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k1anote4"))
async def k1anote4_k1a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote1"]["lectures"]["k1anote4"]
    await callback.message.answer(lecture)

#Лекции 2 курса

@router.callback_query(F.data == ("k2anote1"))
async def k2anote1_k2a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote2"]["lectures"]["k2anote1"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k2anote2"))
async def k2anote2_k2a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote2"]["lectures"]["k2anote2"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k2anote3"))
async def k2anote3_k2a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote2"]["lectures"]["k2anote3"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k2anote4"))
async def k2anote4_k2a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote2"]["lectures"]["k2anote4"]
    await callback.message.answer(lecture)

#Лекции 3 курса

@router.callback_query(F.data == ("k3anote1"))
async def k3anote1_k3a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote3"]["lectures"]["k3anote1"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k3anote2"))
async def k3anote2_k3a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote3"]["lectures"]["k3anote2"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k3anote3"))
async def k3anote3_k3a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote3"]["lectures"]["k3anote3"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k3anote4"))
async def k3anote4_k3a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote3"]["lectures"]["k3anote4"]
    await callback.message.answer(lecture)
    
#Лекции 4 курса

@router.callback_query(F.data == ("k4anote1"))
async def k4anote1_k4a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote4"]["lectures"]["k4anote1"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k4anote2"))
async def k4anote2_k4a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote4"]["lectures"]["k4anote2"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k4anote3"))
async def k4anote3_k4a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote4"]["lectures"]["k4anote3"]
    await callback.message.answer(lecture)

@router.callback_query(F.data == ("k4anote4"))
async def k4anote4_k4a(callback: CallbackQuery):
    from app.DataBase.course_info import course_info
    lecture = course_info["kanote4"]["lectures"]["k4anote4"]
    await callback.message.answer(lecture)

## ⁡⁢⁢⁢​‌‍‌Добавление Регистрации​⁡

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(Command('reg'))
async def reg_first(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer( "Введите ваше имя")


@router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Reg.number)
    await message.answer("Введите ваш номер",reply_markup=kb.request_phone_number())
    

@router.message(Reg.number, F.contact)
async def reg_three(message: Message, state: FSMContext):
    from app.DataBase import requests
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    user = await requests.get_user(message.from_user.id)
    if user:
        user.number = data['number']
        await requests.update_user(user)
        await message.answer(f"Телефон принят \n {data['name']} \n {data['number']} ", reply_markup=kb.Main)
    else:
        await message.answer("Пользователь не найден", reply_markup=kb.Main)
    await state.clear()
