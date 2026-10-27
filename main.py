from http.server import BaseHTTPRequestHandler
import telebot

TOKEN = "8950796201:AAGMWqXnZ2ftTuVy75kL5RSKLYHyuHrSHnI"
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Бот GLD/XAU успешно запущен на Vercel!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

class TelegramBotHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            res = bot.set_webhook(url="https://vercel.app")
            status_text = f"Вебхук успешно установлен! Статус: {res}"
        except Exception as e:
            status_text = f"Ошибка установки вебхука: {e}"

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(f"<h1>{status_text}</h1><p>Бот активен!</p>".encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        update = telebot.types.Update.de_json(post_data)
        bot.process_new_updates([update])
        self.send_response(200)
        self.end_headers()

# Строгая привязка переменной для Vercel
app = TelegramBotHandler
