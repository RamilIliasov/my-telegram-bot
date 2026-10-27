    def do_GET(self):
        # Автоматическая привязка вебхука при открытии сайта
        try:
            res = bot.set_webhook(url="https://vercel.app")
            status_text = f"Вебхук успешно установлен! Статус: {res}"
        except Exception as e:
            status_text = f"Ошибка установки вебхука: {e}"

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(f"<h1>{status_text}</h1><p>Бот активен!</p>".encode('utf-8'))
