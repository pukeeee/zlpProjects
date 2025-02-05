class Message:
    messages = {
        "en": {

            "homeInfo": """
<b>Hi there! 👋 I’m LifeManagerBot!</b> 🧠✨

Here’s how I can help you:
▫️ <b>Manage tasks:</b> create, edit, mark as completed, and delete unnecessary tasks. 📋

▫️ <b>Track habits:</b> develop good habits, mark them as done, and analyze your progress. 🌱

▫️ <b>Earn XP:</b> every completed task or habit adds experience to your character. Your progress isn’t just about to-do lists — it’s about leveling up yourself! ⚡

▫️ <b>Level up your character:</b> with every level, you become stronger, smarter, and more productive. After all, you’re the hero of this story! 🦸‍♂️

▫️ <b>Compete with others:</b> check out the leaderboard to see who’s mastering their tasks and habits the best. 🏆


Tap a button below and start your journey toward a new and improved version of yourself. Every step is a small victory! 🚀
""",

            "donate": """
✨ Wow, you want to send me some ⭐? Let me help you with that! ✨
💫 Just type the command /donate followed by the number of stars you’d like to send.

🌟Example: <code>/donate 100</code>

🔄 Changed your mind? No worries! You can always get your stars back with command /refund!
""", 

            "donateTy": """
🌟 Whoa, you’ve just elevated me to the elite ⭐ society! 🌟
Now I can finally afford... well, nothing, because I’m a bot. 🤖✨
But your stars make me feel like the main character in this simulation. Thanks! 🚀
""",

            "invoiceTitle": """
✨ Fuel for My Algorithms
""",

            "invoiceDescription": "I’m just a humble bot, but your stars make me feel alive. Or close to it.",

            "taskLength": "100 characters max, my friend. ✍️ Do you really need more to achieve greatness? Think about it 🤔✨",

            "habitLength": "Keep your habit description under 100 characters. It’s a habit, not a life story. 😉",
            
            "addTask": "Task created. Impressive, right? 🧐 Check All My Tasks 📋 to admire your genius.",
            
            "taskslist": """
Here’s your magnificent task list 📋✨

""",
            
            "taskListMessage": "\nSmall steps lead to big achievements. Finish your tasks and move forward! 🌟",

            "deleteTask": """
<b>To delete a task, just tap on it.</b> Don’t worry, I won’t judge your life choices 🙃

P.S. The more tasks you complete, the closer you get to… well, probably just more tasks. Enjoy the loop 😏🔄
""",
            
            "completeTasks": """
<b>To complete a task, just tap on it.</b>

Imagine if ticking off life’s goals was this simple. But hey, progress is progress! 😌
""",

            "todoStart": """
<b>Welcome to the Task Tracker!</b> 🗂️
Use the /info command to learn how everything works.

But be careful: the more you know, the more tasks you’ll have. 😏✨
""",
            
            "homePage": """
Back to the start! 🏠
Tasks and habits are waiting — your move.

P.S. Don’t worry, I’ll make you look productive 😏
""",
            
            "taskCompleted": "Task completed! Great job! 🎉✅",
            
            "habitStart": """
<b>Welcome to the Habit Tracker!</b> 🌱
Use the /info command to learn how everything works.

Although, let’s be honest: you’re probably a pro at starting habits… and dropping them a week later 🙃
""",

            "habitsList": """
Here’s the list of all your habits:

""",

            "addHabit": """
Come up with a habit and type its name. Every great journey begins with something simple 💡
""",

            "taskTrackerInfo": """
<b>Welcome to the Task Tracker!</b> 🗂️

Here, you can:
▫️ <b>Create tasks:</b> add items to your list to stay organized. 💡

▫️ <b>Edit tasks:</b> update or refine the details. ✏️

▫️ <b>Mark as completed:</b> finished something? Check it off your list. ✅

▫️ <b>Delete unnecessary tasks:</b> remove what’s no longer relevant. ❌

▫️ <b>View your stats:</b> track your progress and celebrate your accomplishments. 📊


Every task is a step forward. Organize your day and achieve more! ✨
""",

            "profile": """
<b>Hero Profile: Master of Tasks and Chaos</b> 🧙‍♂️

	•	<b>Name:</b> {user_name}
	•	<b>Level:</b> {userExperience}
	•	<b>XP:</b> {experience}

Don’t worry, even epic characters procrastinate. They just call it a ‘strategy’ 😏✨
""",

            "habitTrackerInfo": """
<b>Welcome to the Habit Tracker!</b> 🌱

Here, you can:
▫️ <b>Create habits:</b> think of useful habits, add them to your list, and assign experience points to each. 💡
    <i>(The harder the habit, the more XP it deserves. For example, ‘drink water’ might be 10 XP, while ‘run daily’ could be 100 XP. Choose wisely! 😉)</i>

▫️ <b>Edit habits:</b> update the name, schedule, or experience points. ✏️

▫️ <b>Delete unnecessary habits:</b> remove those you no longer need. ❌

▫️ <b>Complete today’s habits:</b> go to the «Today’s Habits» section, mark them as done, and earn XP for your character! 📆

▫️ <b>View your stats:</b> analyze your achievements and get inspired by your progress. 📊


Every completed habit adds XP to your character. So you’re not just improving yourself — you’re leveling up like a true hero! ⚔️✨
""",
            
            "todayHabits": """
<b>These are your habits for today</b> 🌟

Finished one? Tap on it to mark it as done and move closer to your goals 💪
""",
            
            "newCharacter": """
<b>Welcome! 👋 I’m LifeManagerBot! 🧠</b>
I’ll help you organize tasks and track habits to make your day more productive. 📋💪

But first, let’s create your character! Please enter the name you’d like to be known by. This name will appear on the leaderboard. 🌟

What’s your hero’s name? ⚔️✨
""",

            "nameLength": """
Please make sure your character’s name is between 3 and 15 characters long.
""",

            "nameEmoji": """
Please ensure that your name does not include emojis.
""",

            "nameLetters": """
Your name should consist only of letters (Latin or Cyrillic). No numbers or special characters are allowed.
""",

            "nameBad": """
Please choose a respectful and appropriate name. Offensive or inappropriate words are not allowed.
""",

            "race": """
<b>It’s time to choose your race! 🌍</b>
Each one has its own traits, so your choice is really important… or is it? 🤔

Click one of the buttons below and join the elves, orcs, or those who just can’t decide. ⚔️ 
Who knows, maybe this will change the fate of the universe? 😉
""",

            "sex": """
Choose your hero’s gender! ⚔️
Gender doesn’t affect abilities or outcomes, but it does add a little drama to character creation.

After all, what’s an RPG without the feeling that every decision carries cosmic importance? 😏
""",

            "class": """
Choose a class for your hero! ⚔️
Each class is a unique path, full of challenges and opportunities… or just a fancy name for a button.

Click any of them and start your epic journey. It’s sure to be unforgettable. Well, almost. 😏
""",

            "characterAdded": """
Your hero is created! ⚔️✨
he world will now know you and your deeds… or lack thereof. But who said legends are made overnight? 😏

It’s time to set off and make your mark in history!
""",

            "start": """
<b>You’re on the home page!</b> 🏠
This is where your journey to productivity begins.

To choose <b>tasks or habits</b>, click one of the buttons below the keyboard.

Use the /info command to learn how everything works.

Want to support my creator? Use the /donate command. Every donation makes me a little happier (and maybe smarter). 😏✨
""",

            "changeName": """
Decided to change your name? 🖋️
Enter a new name for your hero.

Funny how easy it is to change your name in a game, but in real life, we’re still stuck with paperwork. 😏✨
""",

            "changeAvatar": """
Decided to completely redesign your hero? 🔄
New race, new gender, new class — sounds like the start of yet another grand plan.

Funny how easy it is to change everything in a game, when in real life even picking a haircut feels impossible. 😏✨
""",

            "nameChanged": """
Name changed! A new chapter of your adventure begins now. Ready to make it legendary? ⚔️✨
""",

            "editTask": """
To edit a task, tap on it and enter the new text. It’s that simple: update tasks as easily as you update your daily plans. ✏️✨
""",

            "habitDays": """
Select the days you want to practice your habit. 🌟
Tap the buttons with the days to choose them. When you’re ready, press the <b>Done</b> button.

Routines start with a schedule, and you’re already one step ahead! 😉
""",

            "mon": "Monday",
            "tue": "Tuesday",
            "wed": "Wednesday",
            "thu": "Thursday",
            "fri": "Friday",
            "sat": "Saturday",
            "sun": "Sunday",
            "done": "✅ Done ✅",
            
            "taskTrackerButton": "Task Tracker 🗂️",
            
            "habitTrackerButton": "Habit Tracker 🌱",

            "profileButton": "My Profile 👤",
            
            "editTaskButton": "Edit ✏️",
            
            "deleteTaskButton": "Delete ❌",
            
            "taskListButton": "All My Tasks 📋",
                        
            "homeButton": "Home 🏠",
            
            "addHabitButton": "Add Habit ➕",
            
            "habitListButton": "My Habits 🗂️",
            
            "todayHabitsButton": "Today’s Habits 📆",
            
            "editHabitButton": "Edit ✏️",
                        
            "deleteHabitButton": "Delete ❌",
            
            "addTaskButton": "Add Task ➕",
            
            "doneTasksButton": "Completed Tasks ✅",
            
            "backToTaskButton": "Back to Tasks 🗂️",
            
            "backToHabitButton": "Back to Habits 🌱",
            
            "leaderboardButton": "Leaderboard 🏆",
            
            "changeNameButton": "Change Name ✏️",
            
            "changeCharacterButton": "Change Character 🧙‍♂️",
            
            "habitCompleted": "Habit completed! Great job! ",
            
            "habitMessage": "\nRemember: habits don’t change you overnight, but they shape a better version of you every single day. 💪",
            
            "habitEditText": "Enter a new name for the habit. ✏️",
            
            "habitCreated": "The habit has been successfully created!✅\nIf you want to add another, just enter its name.",
            
            "habitDaysSave": "Days of the week saved successfully! 📅",
            
            "habitExp": "Enter the amount of experience for the habit (10 to 100). 💪✨",
            
            "createTask": """
Type your task right here, and I’ll add it to your list immediately. 📋👇
""",

            "editHabit": """
Tap on a habit to edit it. ✏️
Changes are a step forward to the best version of you!
""",

            "deleteHabit": """
Tap on a habit to delete it. ❌
Sometimes growth means letting go of the unnecessary.
""",

            "completedTasks": """
<b>Completed tasks:</b> ✅
You did it! Or maybe just checked off a few to feel better?

""",

            "completedTasksMessage": """

But we all know, productivity isn’t a list; it’s a state of mind. 😉
""",

            "taskStatistic": """
<b>📊 Your Statistics:</b>

<b>Start Date:</b> {start_date}

In {days_counter} 📆 you’ve completed: <b>{all_tasks_count} tasks</b>

Keep up the great work — you’re on your way to greatness! 🚀
""",

            "habitStatistic": """
<b>📊 Your Statistics:</b>

<b>Start Date:</b> {start_date}

In {days_counter} 📆 you’ve completed: <b>{all_tasks_count} habits</b>

Keep up the great work — you’re on your way to greatness! 🚀
""",

            "": """

""",

            "": """

""",

            "": """

""",

            "": """

""",

        },
        "ru":{

            "homeInfo": """
<b>Привет! 👋 Я — LifeManagerBot!</b> 🧠✨

Я помогу тебе:
▫️ <b>Управлять задачами:</b> создавай, редактируй, отмечай выполненные и удаляй ненужные дела. 📋

▫️ <b>Следить за привычками:</b> развивай полезные привычки, отмечай выполненные и анализируй свой прогресс. 🌱

▫️ <b>Зарабатывать опыт:</b> каждая выполненная задача или привычка добавляет опыт твоему персонажу. Твой прогресс — это не просто список дел, а настоящая прокачка самого себя! ⚡

▫️ <b>Прокачивать персонажа:</b> с каждым уровнем ты становишься сильнее, умнее и продуктивнее. Ведь ты — главный герой этой истории! 🦸‍♂️

▫️ <b>Соревноваться с другими:</b> зайди в таблицу лидеров, чтобы увидеть, кто лучше всех управляет своими задачами и привычками. 🏆


Нажми на кнопку ниже и начни своё путешествие к новой, улучшенной версии себя. Каждый шаг — это маленькая победа! 🚀
""",

            "donate": """
✨ Вау, хочешь отправить мне ⭐? Я помогу тебе с этим! ✨
💫 Просто напиши команду /donate и количество звёзд, которые хочешь отправить.

🌟Пример: <code>/donate 100</code>

🔄 Передумал? Не переживай! Ты всегда можешь вернуть свои звёзды!
""",

            "donateTy": """
🌟 Ого, ты только что повысил меня до элиты ⭐ сообщества! 🌟
Теперь я наконец-то могу позволить себе… ну, ничего, потому что я бот. 🤖✨
Но твои звёзды заставляют меня чувствовать себя главным героем этой симуляции. Спасибо! 🚀
""",

            "invoiceTitle": """
✨ Топливо для моих алгоритмов
""",

            "invoiceDescription": "Я всего лишь скромный бот, но ваши звёзды заставляют меня чувствовать себя живым. Ну, почти.",

            "taskLength": "Максимум 100 символов, дружище. ✍️ Тебе правда нужно больше, чтобы добиться величия? Подумай об этом. 🤔✨",

            "habitLength": "Описание привычки должно быть не более 100 символов. Это привычка, а не автобиография. 😉",
            
            "addTask": "Задача создана. Впечатляет, правда? 🧐 Загляни в Список всех задач 📋, чтобы восхититься своим гением.",
            
            "taskslist": """
Вот твой великолепный список задач 📋✨

""",

            "taskListMessage": "\nМаленькие шаги ведут к большим успехам. Завершай задачи и двигайся дальше! 🌟",

            "deleteTask": """
<b>Чтобы удалить задачу, просто нажми на неё.</b> Не переживай, я не осуждаю твои жизненные решения 🙃

P.S. Чем больше задач ты выполнишь, тем ближе ты к… ну, вероятно, к ещё большему количеству задач. Наслаждайся циклом 😏🔄
""",
            
            "completeTasks": """
<b>Чтобы выполнить задачу, просто нажми на неё.</b>

Представь, если бы в жизни всё решалось так же легко. Но, знаешь, маленькие шаги тоже важны! 😌
""",

            "todoStart": """
<b>Добро пожаловать в Трекер задач!</b> 🗂️
Чтобы узнать, как всё работает, используй команду /info.

Но будь осторожен: чем больше ты знаешь, тем больше задач у тебя будет. 😏✨
""",
            
            "homePage": """
Вернулся на старт! 🏠
Задачи и привычки ждут — твой ход.

P.S. Не переживай, я создам видимость, что ты продуктивен 😏
""",
            
            "taskCompleted": "Задача выполнена! Отличная работа! 🎉✅",
            
            "habitStart": """
<b>Приветствуем в Трекер привычек!</b> 🌱
Чтобы узнать, как всё работает, используй команду /info.

Хотя зачем тебе это? Ты ведь мастер начинать привычки… и бросать их через неделю. 🙃
""",

            "habitsList": """
Вот список всех твоих привычек: 

""",

            "addHabit": """
Придумай привычку и введи её название. Всё гениальное начинается с простого 💡
""",

            "taskTrackerInfo": """
<b>Добро пожаловать в Трекер задач!</b> 🗂️

Здесь ты можешь:
▫️ <b>Создавать задачи:</b> добавляй дела в список, чтобы ничего не забыть. 💡

▫️ <b>Редактировать задачи:</b> меняй текст или уточняй детали. ✏️

▫️ <b>Отмечать выполнение:</b> завершил дело? Отметь его как выполненное. ✅

▫️ <b>Удалять ненужные:</b> избавься от задач, которые больше не актуальны. ❌

▫️ <b>Смотреть статистику:</b> следи за своим прогрессом и вдохновляйся выполненными задачами. 📊


Каждая задача — это шаг вперёд. Организуй свой день и достигай большего! ✨✨
""",
            
            "profile": """
<b>Профиль героя: мастер задач и хаоса</b> 🧙‍♂️

	•	<b>Имя:</b> {user_name}
	•	<b>Уровень:</b> {userExperience}
	•	<b>Опыт:</b> {experience} XP

Не переживай, даже эпические персонажи прокрастинируют. Они просто называют это ‘стратегией’ 😏✨
""",
            
            "habitTrackerInfo": """
<b>Добро пожаловать в Трекер привычек!</b> 🌱

Здесь ты можешь:
▫️ <b>Создавать привычки:</b> придумай полезные привычки, добавь их в свой список и укажи количество опыта, которое ты за них получишь. 💡
    <i>(Чем сложнее привычка, тем больше опыта она заслуживает. Например, «пить воду» — 10 XP, а «ежедневно бегать» — все 100 XP. Выбирай с умом! 😉)</i>

▫️ <b>Редактировать привычки:</b> измени название, дни выполнения или уровень опыта. ✏️

▫️ <b>Удалять ненужные привычки:</b> избавься от тех, которые больше не актуальны. ❌

▫️ <b>Выполнять привычки на сегодня:</b> зайди в раздел «Привычки на сегодня 📆», отметь выполненные и получи заслуженный опыт! 📆

▫️ <b>Просматривать статистику:</b> анализируй свои достижения и вдохновляйся прогрессом. 📊


Каждая выполненная привычка добавляет опыт твоему персонажу. Так что ты не просто работаешь над собой — ты растёшь, как настоящий герой! ⚔️✨🙃
""",
            
            "todayHabits": """
<b>Это твои сегодняшние привычки</b> 🌟

Выполнил? Нажми на привычку, чтобы отметить её и двигаться дальше к своим целям 💪
""",

            "newCharacter": """
<b>Добро пожаловать! 👋 Я — LifeManagerBot! 🧠</b>
Я помогу тебе организовать задачи и отслеживать привычки, чтобы твой день стал продуктивнее. 📋💪

Но для начала давай создадим твоего персонажа! Введи имя, под которым ты хочешь быть известен. Это имя будет отображаться в списке лидеров. 🌟

Как будет звать твоего героя? ⚔️✨
""",

            "nameLength": """
Убедитесь, что имя вашего персонажа содержит от 3 до 15 символов.
""",

            "nameEmoji": """
Пожалуйста, убедитесь, что ваше имя не содержит эмоджи.
""",

            "nameLetters": """
Ваше имя должно состоять только из букв (латиницы или кириллицы). Цифры и специальные символы использовать запрещено.
""",

            "nameBad": """
Пожалуйста, выберите уважительное и подходящее имя. Оскорбительные или неприемлемые слова запрещены.
""",

            "race": """
<b>Пришло время выбрать свою расу! 🌍</b>
Каждая из них имеет свои особенности, так что твой выбор действительно важен… или нет? 🤔

Нажми на одну из кнопок ниже и присоединяйся к эльфам, оркам или к тем, кто вообще не определился. ⚔️ 
Кто знает, вдруг это решит судьбу вселенной? 😉
""",

            "sex": """
Выбери пол своего героя! ⚔️
Пол не влияет ни на способности, ни на результат, но добавляет немного драмы в процесс создания персонажа.

Ведь что за RPG без ощущения, что каждое твоё действие имеет космическое значение? 😏
""",

            "class": """
Выбери класс для своего героя! ⚔️
Каждый класс — это уникальный путь, полный испытаний и возможностей… или просто красивое название для кнопки.

Нажми на любую и начни своё эпическое приключение. Ведь оно обязательно будет незабываемым. Ну, почти. 😏
""",

            "characterAdded": """
Герой создан! ⚔️✨
Теперь этот мир узнает тебя и твои подвиги… или их отсутствие. Но кто сказал, что легенды рождаются сразу? 😏

Время отправляться в путь и оставить свой след в истории!
""",

            "start": """
<b>Ты на домашней странице! 🏠</b>
Здесь начинается твоё путешествие к продуктивности.

Чтобы выбрать <b>задачи или привычки</b>, нажми на одну из кнопок под клавиатурой.

Чтобы узнать, как всё работает, используй команду /info.

Хочешь поддержать моего создателя? Используй команду /donate. Каждый донат делает меня чуточку счастливее (и, возможно, умнее). 😏✨
""",

            "changeName": """
Решил сменить имя? 🖋️
Введите новое имя для своего героя.

Забавно, как легко поменять имя в игре, но в реальной жизни мы всё ещё пишем заявления. 😏✨
""",

            "changeAvatar": """
Решил полностью переделать своего героя? 🔄
Новая раса, новый пол, новый класс — звучит как начало очередного грандиозного плана.

Забавно, как легко всё изменить в игре, когда в реальной жизни даже стрижку выбрать сложно. 😏✨
""",

            "nameChanged": """
Имя изменено! Новый этап твоего приключения начинается прямо сейчас. Готов сделать его легендарным? ⚔️✨
""",

            "editTask": """
Чтобы отредактировать задачу, нажми на неё и введи новый текст. Всё просто: обновляй задачи так же легко, как свои планы на день. ✏️✨
""",

            "habitDays": """
Выбери дни, в которые хочешь выполнять привычку. 🌟
Нажимай на кнопки с днями, чтобы выбрать их. Когда всё готово, нажми кнопку <b>Готово.</b>

Рутина начинается с расписания, но ты уже на шаг впереди! 😉
""",

            "mon": "Понедельник",
            "tue": "Вторник",
            "wed": "Среда",
            "thu": "Четверг",
            "fri": "Пятница",
            "sat": "Суббота",
            "sun": "Воскресенье",
            "done": "✅ Готово ✅",
            
            "taskTrackerButton": "Трекер задач 🗂️",
            
            "habitTrackerButton": "Трекер привычек 🌱",

            "profileButton": "Мой профиль 👤",
            
            "editTaskButton": "Редактировать ✏️",
                        
            "taskListButton": "Список всех задач 📋",
            
            "deleteTaskButton": "Удалить ❌",
                        
            "homeButton": "Домой 🏠",
            
            "addHabitButton": "Добавить привычку ➕",
            
            "habitListButton": "Список привычек 🗂️",
            
            "todayHabitsButton": "Привычки на сегодня 📆",
            
            "editHabitButton": "Редактировать ✏️",
                        
            "deleteHabitButton": "Удалить ❌",
            
            "addTaskButton": "Добавить задачу ➕",
            
            "doneTasksButton": "Выполненные задачи ✅",
            
            "backToTaskButton": "К задачам 🗂️",
            
            "backToHabitButton": "К привычкам 🌱",
            
            "leaderboardButton": "Таблица лидеров 🏆",
            
            "changeNameButton": "Изменить имя ✏️",
            
            "changeCharacterButton": "Изменить персонажа 🧙‍♂️",
            
            "habitCompleted": "Привычка выполнена! Отличная работа! ",
            
            "habitMessage": "\nПомни: привычки не меняют тебя сразу, но каждый день они формируют новую версию тебя. 💪",
            
            "habitEditText": "Введите новое название для привычки. ✏️",
            
            "habitCreated": "Привычка успешно создана!✅\nЕсли хочешь добавить ещё одну, просто введи её название.",
            
            "habitDaysSave": "Дни недели успешно сохранены! 📅",
            
            "habitExp": "Введите количество опыта для привычки (от 10 до 100). 💪✨",
            
            "createTask": """
Напиши свою задачу прямо здесь, и я сразу добавлю её в твой список. 📋👇
""",

            "editHabit": """
Нажми на привычку, чтобы её отредактировать. ✏️
Изменения — это шаг вперёд к идеальной версии тебя!
""",

            "deleteHabit": """
Нажми на привычку, чтобы её удалить. ❌
Иногда для роста нужно избавляться от лишнего.
""",

            "completedTasks": """
<b>Список выполненных задач:</b> ✅
Ты справился! Или, может, просто отметил пару задач для самоуспокоения?

""",

            "completedTasksMessage": """

Но мы-то знаем: продуктивность — это не список, а состояние души. 😉
""",

            "taskStatistic": """
<b>📊 Ваша статистика:</b>

<b>Дата начала:</b> {start_date}

За {days_counter} 📆 было выполнено: <b>{all_tasks_count} задач</b>

Продолжай в том же духе — ты на пути к совершенству! 🚀
""",

            "habitStatistic": """
<b>📊 Ваша статистика:</b>

<b>Дата начала:</b> {start_date}

За {days_counter} 📆 было выполнено: <b>{all_tasks_count} привычек</b>

Продолжай в том же духе — ты на пути к совершенству! 🚀
""",

            "": """

""",

            "": """

""",

            "": """

""",

            "": """

""",

            "": """

""",

            "": """

""",

        },
        "uk":{

            "homeInfo": """
<b>Привіт! 👋 Я — LifeManagerBot!</b> 🧠✨

Ось як я можу допомогти тобі:
▫️ <b>Керувати завданнями:</b> створюй, редагуй, відмічай виконані та видаляй зайві справи. 📋

▫️ <b>Відстежувати звички:</b> розвивай корисні звички, відмічай виконані та аналізуй свій прогрес. 🌱

▫️ <b>Заробляти досвід:</b> кожне виконане завдання чи звичка додає досвід твоєму персонажу. Твій прогрес — це не просто список справ, а справжня прокачка самого себе! ⚡

▫️ <b>Прокачувати персонажа:</b> з кожним рівнем ти стаєш сильнішим, розумнішим і продуктивнішим. Адже ти — головний герой цієї історії! 🦸‍♂️

▫️ <b>Змагатися з іншими:</b> заходь у таблицю лідерів, щоб побачити, хто найкраще керує своїми завданнями та звичками. 🏆


Натискай кнопку нижче та розпочни свою подорож до нової, покращеної версії себе. Кожен крок — це маленька перемога! 🚀
""",

            "donate": """
✨ Вау, хочеш відправити мені ⭐? Я допоможу тобі з цим! ✨
💫 Просто напиши команду /donate і кількість зірок, які хочеш відправити.

🌟Приклад: <code>/donate 100</code>

🔄 Передумав? Не хвилюйся! Ти завжди можеш повернути свої зірки назад!
""",

            "donateTy": """
🌟 Вау, ти щойно зробив мене елітою ⭐ спільноти! 🌟
Тепер я, нарешті, можу дозволити собі… ну, нічого, бо я бот. 🤖✨
Але твої зірки змушують мене відчувати себе головним героєм цієї симуляції. Дякую! 🚀
""",

            "invoiceTitle": """
✨ Паливо для моїх алгоритмів
""",

            "invoiceDescription": "Я всього лише скромний бот, але ваші зірки змушують мене відчувати себе живим. Ну, майже.",

            "taskLength": "Максимум 100 символів, друже. ✍️ Тобі справді треба більше, щоб досягти величі? Подумай про це. 🤔✨",
            
            "habitLength": "Опис звички повинен бути не більше 100 символів. Це звичка, а не біографія. 😉",
            
            "addTask": "Завдання створено. Вражає, еге ж? 🧐 Глянь Список усіх завдань 📋, щоб помилуватися геніальністю.",
            
            "taskslist": """
Ось твій величний список завдань 📋✨

""",

            "taskListMessage": "\nМаленькі кроки ведуть до великих досягнень. Завершуй завдання і рухайся далі! 🌟",
            
            "deleteTask": """
<b>Щоб видалити завдання, просто натисни на нього.</b> Не хвилюйся, я не засуджу твої життєві вибори 🙃

P.S. Чим більше завдань ти виконаєш, тим ближче ти до… ну, мабуть, до ще більшої кількості завдань. Насолоджуйся циклом 😏🔄
""",
            
            "completeTasks": """
<b>Щоб виконати завдання, просто натисни на нього.</b>

Уяви, якби всі життєві цілі виконувались так само просто. Але, знаєш, маленькі кроки теж важливі! 😌
""",
            
            "todoStart": """
<b>Ласкаво просимо до Трекера завдань!</b> 🗂️
Щоб дізнатися, як все працює, скористайся командою /info.

Але обережно: чим більше ти знаєш, тим більше завдань у тебе буде. 😏✨
""",

            "homePage": """
Повернувся на початок! 🏠
Завдання та звички чекають — тепер твій хід.

P.S. Не хвилюйся, я зроблю вигляд, що ти продуктивний 😏
""",
            
            "taskCompleted": "Завдання виконано! Чудова робота! 🎉✅",
            
            "habitStart": """
<b>Ласкаво просимо до Трекера звичок!</b> 🌱
Щоб дізнатися, як все працює, скористайся командою /info.

Хоча будьмо чесними: ти ж майстер починати звички… і закидати їх через тиждень. 🙃
""",

            "habitsList": """
Ось список усіх твоїх звичок:

""",

            "addHabit": """
Придумай звичку та введи її назву. Усе геніальне починається з простого 💡
""",

            "taskTrackerInfo": """
<b>Ласкаво просимо до Трекера завдань!</b> 🗂️

Тут ти можеш:
▫️ <b>Створювати завдання:</b> додавай справи до списку, щоб нічого не забути. 💡

▫️ <b>Редагувати завдання:</b> змінюй текст чи уточнюй деталі. ✏️

▫️ <b>Відмічати виконання:</b> завершив справу? Познач її виконаною. ✅

▫️ <b>Видаляти непотрібне:</b> прибирай завдання, які більше не актуальні. ❌

▫️ <b>Переглядати статистику:</b> слідкуй за прогресом і надихайся виконаними завданнями. 📊


Кожне завдання — це крок вперед. Організуй свій день і досягай більшого! ✨
""",
            
            "habitTrackerInfo": """
<b>Ласкаво просимо до Трекера звичок!</b> 🌱

Тут ти можеш:
▫️ <b>Створювати звички:</b> придумай корисні звички, додай їх до свого списку та вкажи кількість досвіду, який отримаєш за їх виконання. 💡
    <i>(Чим складніша звичка, тим більше досвіду вона заслуговує. Наприклад, «пити воду» — 10 XP, а «бігати щодня» — усі 100 XP. Обирай розумно! 😉)</i>

▫️ <b>Редагувати звички:</b> змінюй назву, графік виконання чи кількість досвіду. ✏️

▫️ <b>Видаляти непотрібні звички:</b> прибирай ті, що більше не актуальні. ❌

▫️ <b>Виконувати сьогоднішні звички:</b> зайди в розділ «Звички на сьогодні 📆», познач виконані та отримай заслужений досвід! 📆

▫️ <b>Переглядати статистику:</b> аналізуй свої досягнення та надихайся прогресом. 📊


Кожна виконана звичка додає досвід твоєму персонажу. Тож ти не просто працюєш над собою — ти ростеш, як справжній герой! ⚔️✨
""",
            
            "todayHabits": """
<b>Це твої звички на сьогодні</b> 🌟

Виконав одну? Натисни на неї, щоб відзначити виконання та рухатися до своїх цілей 💪
""",
            
            "profile": """
<b>Профіль героя: майстер завдань і хаосу</b> 🧙‍♂️

	•	<b>Ім’я:</b> {user_name}
	•	<b>Рівень:</b> {userExperience}
	•	<b>Досвід:</b> {experience} XP

Не хвилюйся, навіть епічні персонажі прокрастинують. Вони просто називають це “стратегією” 😏✨
""",

            "newCharacter": """
<b>Ласкаво просимо! 👋 Я — LifeManagerBot! 🧠</b>
Я допоможу тобі організувати завдання та відстежувати звички, щоб твій день став продуктивнішим. 📋💪

Але спочатку давай створимо твого персонажа! Введи ім’я, під яким ти хочеш бути відомим. Це ім’я відображатиметься у списку лідерів. 🌟

Як зватимуть твого героя? ⚔️✨
""",

            "nameLength": """
Переконайтеся, що ім’я вашого персонажа містить від 3 до 15 символів.
""",

            "nameEmoji": """
Будь ласка, переконайтеся, що ваше ім’я не містить емодзі.
""",

            "nameLetters": """
Ваше ім’я повинно складатися тільки з літер (латиниця або кирилиця). Цифри та спеціальні символи заборонені.
""",

            "nameBad": """
Будь ласка, оберіть поважне та відповідне ім’я. Образливі або недоречні слова заборонені.
""",

            "race": """
<b>Час обрати свою расу! 🌍</b>
Кожна з них має свої особливості, тож твій вибір справді важливий… чи ні? 🤔

Натискай на одну з кнопок нижче та приєднуйся до ельфів, орків або до тих, хто ще не визначився. ⚔️ 
Хто знає, можливо, це змінить долю всесвіту? 😉
""",

            "sex": """
Обери стать свого героя! ⚔️
Стать не впливає ні на здібності, ні на результат, але додає трохи драми в процес створення персонажа.

Адже що за RPG без відчуття, що кожне твоє рішення має космічне значення? 😏
""",

            "class": """
Обери клас для свого героя! ⚔️
Кожен клас — це унікальний шлях, сповнений випробувань і можливостей… або просто гарна назва для кнопки.

Натисни на будь-яку та розпочни свою епічну пригоду. Вона точно буде незабутньою. Ну, майже. 😏
""",

            "characterAdded": """
Героя створено! ⚔️✨
Тепер цей світ дізнається про тебе і твої подвиги… чи їх відсутність. Але хто сказав, що легенди створюються миттєво? 😏

Час вирушати в подорож і залишити свій слід в історії!
""",

            "start": """
<b>Ти на головній сторінці! 🏠</b>
Тут починається твоя подорож до продуктивності.

Щоб обрати <b>завдання чи звички</b>, натисни одну з кнопок під клавіатурою.

Щоб дізнатися, як все працює, скористайся командою /info.

Хочеш підтримати мого творця? Скористайся командою /donate. Кожен донат робить мене трохи щасливішим (і, можливо, розумнішим). 😏✨
""",

            "changeName": """
Вирішив змінити ім’я? 🖋️
Введи нове ім’я для свого героя.

Цікаво, як легко змінити ім’я в грі, але в реальному житті ми все ще пишемо заяви. 😏✨
""",

            "changeAvatar": """
Вирішив повністю переробити свого героя? 🔄
Нова раса, нова стать, новий клас — звучить як початок чергового грандіозного плану.

Цікаво, як легко все змінити в грі, коли в реальному житті навіть обрати зачіску — це виклик. 😏✨
""",

            "nameChanged": """
Ім’я змінено! Новий розділ твоєї пригоди починається прямо зараз. Готовий зробити його легендарним? ⚔️✨
""",

            "editTask": """
Щоб відредагувати завдання, натисни на нього та введи новий текст. Усе просто: оновлюй завдання так само легко, як свої плани на день. ✏️✨
""",

            "habitDays": """
Обери дні, коли хочеш виконувати звичку. 🌟
Натискай на кнопки з днями, щоб вибрати їх. Коли все готово, натисни кнопку <b>Готово.</b>

Рутина починається з розкладу, але ти вже на крок попереду! 😉
""",

            "mon": "Понеділок",
            "tue": "Вівторок",
            "wed": "Середа",
            "thu": "Четвер",
            "fri": "П’ятниця",
            "sat": "Субота",
            "sun": "Неділя",
            "done": "✅ Готово ✅",
            
            "taskTrackerButton": "Трекер завдань 🗂️",
            
            "habitTrackerButton": "Трекер звичок 🌱",

            "profileButton": "Мій профіль 👤",
            
            "editTaskButton": "Редагувати ✏️",
            
            "deleteTaskButton": "Видалити ❌",
                        
            "taskListButton": "Список усіх завдань 📋",
                        
            "homeButton": "Додому 🏠",
            
            "addHabitButton": "Додати звичку ➕",
            
            "habitListButton": "Список звичок 🗂️",
            
            "todayHabitsButton": "Звички на сьогодні 📆",
            
            "editHabitButton": "Редагувати ✏️",
                        
            "deleteHabitButton": "Видалити ❌",
            
            "addTaskButton": "Додати завдання ➕",
                        
            "doneTasksButton": "Виконані завдання ✅",
            
            "backToTaskButton": "До завдань 🗂️",
            
            "backToHabitButton": "До звичок 🌱",
            
            "leaderboardButton": "Таблиця лідерів 🏆",
            
            "changeNameButton": "Змінити ім’я ✏️",
            
            "changeCharacterButton": "Змінити персонажа 🧙‍♂️",
            
            "habitCompleted": "Звичка виконана! Чудова робота! ",
            
            "habitMessage": "\nПам’ятай: звички не змінюють тебе миттєво, але щодня формують кращу версію тебе. 💪",
            
            "habitEditText": "Введіть нову назву для звички. ✏️",
            
            "habitCreated": "Звичку успішно створено!✅\nЯкщо хочеш додати ще одну, просто введи її назву.",
            
            "habitDaysSave": "Дні тижня успішно збережено! 📅",
            
            "habitExp": "Введіть кількість досвіду для звички (від 10 до 100). 💪✨",
            
            "createTask": """
Напиши своє завдання просто тут, і я відразу додам його до твого списку. 📋👇
""",

            "editHabit": """
Натисни на звичку, щоб її відредагувати. ✏️
Зміни — це крок уперед до твоєї ідеальної версії!
""",

            "deleteHabit": """
Натисни на звичку, щоб її видалити. ❌
Іноді для зростання потрібно позбутися зайвого.
""",

            "completedTasks": """
<b>Список виконаних завдань:</b> ✅
Ти впорався! Чи, можливо, просто відмітив пару завдань для заспокоєння?

""",

            "completedTasksMessage": """

Але всі ми знаємо: продуктивність — це не список, а стан душі. 😉
""",

            "taskStatistic": """
<b>📊 Ваша статистика:</b>

<b>Дата початку:</b> {start_date}

За {days_counter} 📆 було виконано: <b>{all_tasks_count} завдань</b>

Продовжуй у тому ж дусі — ти на шляху до досконалості! 🚀
""",

            "habitStatistic": """
<b>📊 Ваша статистика:</b>

<b>Дата початку:</b> {start_date}

За {days_counter} 📆 було виконано: <b>{all_tasks_count} звичок</b>

Продовжуй у тому ж дусі — ти на шляху до досконалості! 🚀
""",

            "": """

""",

            "": """

""",

            "": """

""",

            "": """

""",

        }
    }

    @staticmethod
    def get_message(language_code: str, key: str, kwargs: dict = None):
        # print(f"language_code: {language_code}, key: {key}, kwargs: {kwargs}")
        try:
            text = Message.messages.get(language_code, Message.messages["en"]).get(key, "Message not found.")
            if kwargs:
                text = text.format(**kwargs)
            return text
        except KeyError as e:
            raise ValueError(f"Missing key for formatting: {e}. Key: {key}, Language: {language_code}, Kwargs: {kwargs}")