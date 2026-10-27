from http.server import BaseHTTPRequestHandler
import telebot

# ВСТАВЬТЕ СЮДА ВАШ НАСТОЯЩИЙ ТОКЕН ИЗ ТЕЛЕГРАМА (В КАВЫЧКИ)
TOKEN = "8950796201:AAGMWqXnZ2ftTuVy75kL5RSKLYHyuHrSHnI"

bot = telebot.TeleBot(TOKEN, threaded=False)
handler = bot # Это та самая переменная, которую ищет Vercel!

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Бот GLD/XAU успешно запущен на Vercel!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        update = telebot.types.Update.de_json(post_data)
        bot.process_new_updates([update])
        self.send_response(200)
        self.end_headers()
