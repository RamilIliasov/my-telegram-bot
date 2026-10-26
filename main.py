import os
import telebot

# ВСТАВЬТЕ СЮДА ВАШ ТОКЕН ИЗ ТЕЛЕГРАМА (МЕЖДУ КАВЫЧКАМИ)
TOKEN = "ВАШ_ТОКЕН"

# Если на сервере Render задана переменная BOT_TOKEN, берем её
if not TOKEN or TOKEN == "ВАШ_ТОКЕН":
    TOKEN = os.environ.get("BOT_TOKEN")

print("Проверка подключения к Telegram...")

if not TOKEN:
    print("[ОШИБКА] Токен не найден! Проверьте, что вставили его в кавычки.")
    input("\nНажмите Enter для выхода...")
    exit()

try:
    bot = telebot.TeleBot(TOKEN)


    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        bot.reply_to(
            message, "Привет! Бот GLD/XAU успешно работает на сервере!"
        )


    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, f"Вы написали: {message.text}")


    print("Бот успешно запущен! Проверьте его в Telegram.")
    bot.infinity_polling()

except Exception as e:
    print(f"\n[ОШИБКА В РАБОТЕ БОТА]: {e}")
    input("\nНажмите Enter для выхода...")
