class Message:
    messages = {
        "en": {
            "start": """
Hi there! 👋 I’m your ToDoBot! ✨
I’ll help you save all your tasks and organize your day! 📋💡

💼 How I work:
Write down your task, and I’ll save it to your list! 📝
To see all your tasks, press the "My tasks" button ⬇️ on the keyboard.
If you’ve completed a task, just tap on it, and it will disappear! ✅

🌟 Support:
If you’d like to show your appreciation, send me some golden stars through the /donate command. It’ll make me the happiest bot ever! 🤩⭐

Ready to get started? Write your first task and let’s boost your productivity! 🚀
""",

            "donate": """
✨ Wow, you want to send me some ⭐? Let me help you with that! ✨
💫 Just type the command /donate followed by the number of stars you’d like to send.

🌟Example: /donate 100 

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

            "taskLength": "100 characters max, my friend. ✍️ Do you really need more to achieve greatness? Think about it. 🤔✨",
            
            "addTask": "Task created. Impressive, right? 🧐 Check My Tasks to admire your genius.",
            
            "taskListButton": "My Tasks📝"
        },
        "ru":{
            "start": """
Привет! 👋 Я — твой ToDoBot! ✨
Я помогу тебе сохранять все твои задачи и организовать твой день! 📋💡

💼 Как я работаю:
Напиши свою задачу, и я её сохраню в списке! 📝
Чтобы увидеть список всех задач, нажми кнопку "My tasks" ⬇️ под клавиатурой.
Если задача выполнена, просто нажми на неё, и она исчезнет! ✅

🌟 Поддержка:
Если хочешь выразить благодарность, отправь мне золотые звёзды через команду /donate. Это сделает меня самым счастливым ботом! 🤩⭐

Готов начинать? Напиши первую задачу и вперед к продуктивности! 🚀
""",

            "donate": """
✨ Вау, хочешь отправить мне ⭐? Я помогу тебе с этим! ✨
💫 Просто напиши команду /donate и количество звёзд, которые хочешь отправить.

🌟Пример: /donate 100 

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
            
            "addTask": "Задача создана. Впечатляет, правда? 🧐 Загляни в Мои Задачи, чтобы восхититься своим гением.",
            
            "taskListButton": "Мои Задачи📝"
        },
        "uk":{
            "start": """
Привіт! 👋 Я — твій ToDoBot! ✨
Я допоможу тобі зберігати всі твої завдання та організувати день! 📋💡

💼 Як я працюю:
Напиши своє завдання, і я його збережу у списку! 📝
Щоб переглянути список усіх завдань, натисни кнопку "My tasks" ⬇️ на клавіатурі.
Якщо завдання виконано, просто натисни на нього, і воно зникне! ✅

🌟 Підтримка:
Якщо хочеш подякувати, надішли мені золоті зірки через команду /donate. Це зробить мене найщасливішим ботом! 🤩⭐

Готовий почати? Напиши своє перше завдання — і вперед до продуктивності! 🚀
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
            
            "addTask": "Завдання створено. Вражає, еге ж? 🧐 Глянь Мої Завдання, щоб помилуватися геніальністю.",
            
            "taskListButton": "Мої Завдання📝"
        }
    }

    @staticmethod
    def get_message(language_code: str, key: str, kwargs: dict = None):
        text = Message.messages.get(language_code, Message.messages["en"]).get(key, "Message not found.")
        if kwargs:
            text = text.format(**kwargs)
        return text