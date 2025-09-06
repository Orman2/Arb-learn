# bot_learning_full.py
# pip install python-telegram-bot==20.3

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ==========================
# КОНФИГ
# ==========================
TOKEN = "7769932722:AAE4ILgHUzgqW4u3lnIQdqlYnBCM-wuRynM"

# Тексты уроков
lessons = {
    "1": """📘 Урок 1

Добро пожаловать на Тест Драйв нашего Обучения по Арбитражу без карт где я покажу тебе как Зарабатывать от 50% в месяц к Депозиту на Криптовалюте, Абсолютно без Никаких рисков 🔥

И да, это не Р2Р Арбитраж и даже не Трейдинг, это Ниша про которую сейчас не знает никто ты узнаешь Первым🤯
Тебе нужен только Телефон и Знания, которые нужно использовать чтобы Заходить в сделки и Зарабатывать, ничем не рискуя 👇

На Тест-Драйве, у нас будет 6 Уроков:
1️⃣ Я покажу тебе как ты сможешь Зарабатывать от $10.000 в месяц, как Новичок без Рисков на Арбитраже без карт 
2️⃣ Разберем какие инструменты нам нужны для Заработка? Какими Биржами нужно пользоваться, где самые прибыльные монеты, как правильно пройти Верификацию и подготовиться перед Торговлей
3️⃣ Я покажу тебе, как купить Криптовалюту и как переводить ее с биржи на биржу в Доли секунды чтобы Максимизировать наш Заработок на каждой связке 
4️⃣ Какие есть риски? Как заходить в сделки? Как искать связки для Заработка и покажу как работает наш Бот
5️⃣ Покажу и Расскажу про самый денежный способ Заработка внутри Арбитража без карт
6️⃣ Я покажу тебе как Использовать все Инструменты которым Обучу тебя и как используя их начать Стабильно Зарабатывать

Первый урок уже вышел, чтобы его посмотреть нажми на Кнопку ниже 👇""",

    "2": """📘 Урок 2

2 урок Тест-Драйва уже вышел ⏰ 

На нем я Показал какие биржи нужны для Старта в Арбитраже без карт и как правильно проходить Регистрацию и Верификацию, чтобы его посмотреть нажми на Кнопку ниже 👇""",

    "3": """📘 Урок 3

3 урок тест-драйва уже ВЫШЕЛ! 

На нем я показал: 
🧠 Как купить первую Криптовалюту
🧠 Как правильно переводить монеты с Биржи на Биржу 
🧠 Какие есть риски при Покупке USDT 

Чтобы его посмотреть нажми на Кнопку ниже 👇""",

    "4": """📘 Урок 4

Как Стабильно Зарабатывать на Арбитраже без Карт и Искать связки - Рассказал на 4 Уроке 👇

В нем:
1. Показал, как искать связки с потенциалом от 5% за Круг в Арбитраже без Карт 💸
2. Подробно показал откуда берутся Заработки и как находить Монеты с наибольшим Заработком 🧠
3. Какие есть риски и как правильно их Обходить чтобы всегда быть только в +🤯""",

    "5": """📘 Урок 5

Хочешь узнать, как Можно Зарабатывать до 100% всего на 1 Одной сделке в Арбитраже без карт? Тогда бегом смотреть 5 урок 👇

В нем:
1. Показал на Практике как правильно Заходить и выходить из сделки чтобы Зарабатывать💸
2. Какие есть подводные Камни
3. Как искать готовые и рабочие связки 🤯""",

    "6": """📘 Урок 6

Остался последний шаг перед твоим Стартом в Арбитраже без карт 🚀

В нем:
1. Рассказал как тебе теперь правильно начать свою Торговлю💸
2. Какие есть подводные Камни перед началом Активного Заработка🧠
3. Как построить Стабильный Заработок от $2000+ / мес 🤯

Приятного просмотра 👇"""
}

# Домашние задания
homeworks = {
    "1.1": """📝 Домашнее задание 1

Если ты видишь это сообщение значит ты уже Посмотрел 1 Урок ✅

Не забудь выполнить домашнее задание и после можешь переходить ко 2 Уроку.

Вопросы к Куратору: @O01NM10""",

    "2.2": """📝 Домашнее задание 2

Поздравляю с просмотром 2 Урока ✅

Теперь тебе нужно выполнить Домашнее Задание и Зарегаться на Биржах:

1. [ByBit](https://www.bybit.com/invite?ref=J8W02L)  
2. [MEXC](https://promote.mexc.com/r/I9vLmWxt)  
3. [Binance](https://www.binance.com/referral/earn-together/refer-in-hotsummer/claim?hl=en&ref=GRO_20338_9T9YL&utm_source=default)  
4. [Gate.io](https://www.gate.com/signup/VGCWVGWLAA?ref_type=103&utm_cmp=PEYEQdSb)  
5. [LBank](https://lbank.com/ref/57T7S)  
6. [BingX](https://bingx.com/invite/YOH7MA/)  

Если не открываются ссылки — используй VPN (как на уроке).  

Домашнее Задание скидывай Куратору: @O01NM10""",

    "3.3": """📝 Домашнее задание 3

Теперь ты знаешь, как нужно покупать USDT ✅

Домашнее Задание: Купить USDT на бирже (как я показывал на уроке).

Вопросы и ответы Куратору: @O01NM10""",

    "4.4": """📝 Домашнее задание 4

Теперь нужно выполнить Домашнее Задание и купить свою первую монету (как на уроке).

Вопросы к Куратору: @O01NM10""",

    "5.5": """📝 Домашнее задание 5

Теперь в твоем Арсенале есть Оружие, но нужно научиться стрелять 💸

Домашнее Задание: Зайди во Фьючерсную сделку на Демо счете (как я показывал).

Вопросы к Куратору: @O01NM10""",

    "6.6": """📝 Домашнее задание 6

Отлично, ты прошел курс Молодого Бойца! 🚀  

Теперь готов врываться в Арбитраж без карт!  

Если собрал все ключевые слова и выполнил ДЗ — пиши Куратору: @O01NM10"""
}

# Ссылки на видео для уроков
lesson_links = {
    "1": "https://orman2.github.io/lesson1/",
    "2": "https://orman2.github.io/lesson2/",
    "3": "https://orman2.github.io/lesson3/",
    "4": "https://orman2.github.io/lesson4/",
    "5": "https://orman2.github.io/lesson5/",
    "6": "https://orman2.github.io/lesson6/",
}

# ==========================
# СТАРТ
# ==========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать 👋\nНажмите кнопку, чтобы начать обучение:",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▶️ Урок 1", callback_data="lesson_1")]]
        ),
    )

# ==========================
# ОБРАБОТКА УРОКОВ
# ==========================
async def lesson_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lesson_id = query.data.split("_")[1]
    text = lessons.get(lesson_id, "Урок не найден")

    keyboard = [
        [InlineKeyboardButton("🎥 Смотреть урок", url=lesson_links[lesson_id])],
        [InlineKeyboardButton("📝 Домашнее задание", callback_data=f"hw_{lesson_id}")]
    ]

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True
    )

# ==========================
# ОБРАБОТКА ДЗ
# ==========================
async def homework_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lesson_id = query.data.split("_")[1]
    hw_id = f"{lesson_id}.{lesson_id}"

    text = homeworks.get(hw_id, "ДЗ не найдено")

    next_lesson = str(int(lesson_id) + 1) if lesson_id != "6" else None
    keyboard = []
    if next_lesson:
        keyboard.append([InlineKeyboardButton("➡️ Следующий урок", callback_data=f"lesson_{next_lesson}")])

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard) if keyboard else None,
        disable_web_page_preview=True
    )

# ==========================
# MAIN
# ==========================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(lesson_handler, pattern="^lesson_"))
    app.add_handler(CallbackQueryHandler(homework_handler, pattern="^hw_"))

    app.run_polling()

if __name__ == "__main__":
    main()
