from http.server import BaseHTTPRequestHandler
import telebot
import json
import os

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not set")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Бот успешно запущен на Vercel")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        update = telebot.types.Update.de_json(post_data.decode('utf-8'))
        bot.process_new_updates([update])
        
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Bot is running</h1>")
