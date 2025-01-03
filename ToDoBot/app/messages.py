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
"""
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
"""
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
"""
        }
    }

    @staticmethod
    def get_message(language_code: str, key: str):
        return Message.messages.get(language_code, Message.messages["en"]).get(key, "Message not found.")