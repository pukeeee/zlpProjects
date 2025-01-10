from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                        InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from app.messages import Message
from aiogram.fsm.context import FSMContext
from database.requests import getTask, getHabits, getTodayHabits
from datetime import datetime
from config import IMG_FOLDER
import os



async def startReplyKb(language_code: str):
    todoButton = "Task Tracker"
    habitButton = "Habit Tracker"
    profile = "My profile"
    replyKeyboard = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = todoButton), KeyboardButton(text = habitButton)], [KeyboardButton(text = profile)]],
                                                    resize_keyboard = True)
    return replyKeyboard

###########
"""Tasks"""
###########

async def delTasks(tg_id):
    tasks = await getTask(tg_id)
    keyboard = InlineKeyboardBuilder()
    for task in tasks:
        keyboard.add(InlineKeyboardButton(text = task.task, callback_data = f"deltask_{task.id}"))
    return keyboard.adjust(1).as_markup()



async def editTasks(tg_id):
    tasks = await getTask(tg_id)
    keyboard = InlineKeyboardBuilder()
    for task in tasks:
        keyboard.add(InlineKeyboardButton(text = task.task, callback_data = f"edittask_{task.id}"))
    return keyboard.adjust(1).as_markup()



async def todoReplyKB(language_code: str):
    taskListButton = "My tasks"
    backToMain = "🏠 Home"
    info = "Info"
    editTask = "Edit task"
    replyKeyboard = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = editTask), KeyboardButton(text = taskListButton)], 
                                                    [KeyboardButton(text = info), KeyboardButton(text = backToMain)]],
                                                    resize_keyboard = True)
    return replyKeyboard

############
"""Habits"""
############

async def habitsReplyKB(language_code: str):
    habitListButton = "My habits"
    todayHabits = "Today habits"
    backToMain = "🏠 Home"
    addHabit = "Add habit"
    info = "Info"
    replyKeyboard = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = addHabit)],
                                                    [KeyboardButton(text = habitListButton), KeyboardButton(text = todayHabits)],
                                                    [KeyboardButton(text = info) ,KeyboardButton(text = backToMain)]
                                                    ],resize_keyboard = True)
    return replyKeyboard

async def addHabitReplyKB(language_code: str):
    backToMain = "🏠 Home"
    backToHabit = "🔙 Habit"
    replyKeyboard = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = backToHabit)], 
                                                    [KeyboardButton(text = backToMain)]
                                                    ],resize_keyboard = True)
    return replyKeyboard



async def delHabits(tg_id):
    habits = await getHabits(tg_id)
    keyboard = InlineKeyboardBuilder()
    for habit in habits:
        keyboard.add(InlineKeyboardButton(text = habit.name, callback_data = f"delhabit_{habit.id}"))
    return keyboard.adjust(1).as_markup()



async def selectWeekdaysKB(selected_days = None):
    if selected_days is None:
        selected_days = []
    
    days = [
        ("Понедельник", "habitDays_mon"),
        ("Вторник", "habitDays_tue"),
        ("Среда", "habitDays_wed"),
        ("Четверг", "habitDays_thu"),
        ("Пятница", "habitDays_fri"),
        ("Суббота", "habitDays_sat"),
        ("Воскресенье", "habitDays_sun")
    ]
    
    keyboard = InlineKeyboardBuilder()
    for dayName, dayCode in days:
        buttonText = f"✅ {dayName}" if dayCode.split("_")[1] in selected_days else dayName
        keyboard.add(InlineKeyboardButton(text = buttonText, callback_data = dayCode))
    keyboard.add(InlineKeyboardButton(text="Готово", callback_data="habitDays_done"))
    keyboard.adjust(2)
    return keyboard.as_markup()



async def todayHabits(tg_id, language_code: str):
    currentDay = datetime.today().weekday()
    habits = await getTodayHabits(tg_id)
    keyboard = InlineKeyboardBuilder()

    today_habits = []
    for habit in habits:
        if len(habit.days_of_week) == 7 and habit.days_of_week[currentDay] == '1':
            today_habits.append(habit)

    if today_habits:
        for habit in today_habits:
            keyboard.add(InlineKeyboardButton(text=habit.name, callback_data=f"completedHabit_{habit.id}"))
    else:
        keyboard.add(InlineKeyboardButton(text="No habits for today", callback_data="no_today_habits"))
    return keyboard.adjust(1).as_markup()

#############
"""Profile"""
#############

async def regRase():
    keyboard = InlineKeyboardBuilder()
    items = os.listdir(IMG_FOLDER)
    
    for item in items:
        item_path =  os.path.join(IMG_FOLDER, item)
        if os.path.isdir(item_path):
            keyboard.add(InlineKeyboardButton(
                                            text=item,
                                            callback_data=f"raseFolder_{item}"
                                        )
                                    )
    keyboard.adjust(2)
    return keyboard.as_markup()



async def regSex(state):
    data = await state.get_data()
    selected_race_folder = data.get('selected_race_folder')
    keyboard = InlineKeyboardBuilder()
    race_path = os.path.join(IMG_FOLDER, selected_race_folder)
    items = os.listdir(race_path)
    
    for item in items:
        item_path = os.path.join(race_path, item)
        if os.path.isdir(item_path):
            keyboard.add(InlineKeyboardButton(
                text=item,
                callback_data=f"sexFolder_{item}"
            ))
    keyboard.adjust(2)
    return keyboard.as_markup()



async def regClass(state):
    data = await state.get_data()
    selected_race_folder = data.get('selected_race_folder')
    selected_sex_folder = data.get('selected_sex_folder')
    keyboard = InlineKeyboardBuilder()
    class_path = os.path.join(IMG_FOLDER, selected_race_folder, selected_sex_folder)
    items = os.listdir(class_path)
    
    for item in items:
        item_path = os.path.join(class_path, item)
        if os.path.isdir(item_path):
            keyboard.add(InlineKeyboardButton(
                text=item,
                callback_data=f"classFolder_{item}"
            ))
    keyboard.adjust(2)
    return keyboard.as_markup()



async def profileInLineKB():
    leaderBoardButton = InlineKeyboardButton(text="Leaderboard", callback_data="leaderboard")
    changeName = InlineKeyboardButton(text="Change Name", callback_data="changeName")
    changeAvatar = InlineKeyboardButton(text="Change Character", callback_data="changeAvatar")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[leaderBoardButton],
                                                    [changeAvatar, changeName]])
    return keyboard



async def avatarNavigationKB():
    backButton = InlineKeyboardButton(text="⬅️ Назад", callback_data="prev_gif")
    nextButton = InlineKeyboardButton(text="Вперед ➡️", callback_data="next_gif")
    doneButton = InlineKeyboardButton(text="Готово", callback_data="done_gif")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[backButton, nextButton],
                                                    [doneButton]])
    return keyboard