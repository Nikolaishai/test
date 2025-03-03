from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Переменная для хранения последнего полученного веб-хука
latest_webhook = None

# Главная страница, отображающая последний полученный веб-хук
@app.route('/')
def home():
    print("Отправляем данные на страницу:", latest_webhook)  # Отладочный вывод
    return render_template('index.html', webhook=latest_webhook)

# Веб-хук
@app.route('/webhook', methods=['POST'])
def webhook():
    global latest_webhook
    if request.method == 'POST':
        # Получаем данные из запроса
        data = request.get_json()

        # Сохраняем только последний веб-хук
        latest_webhook = data

        # Выводим данные в консоль на сервере
        print("Received webhook data:", data)

        # Ответ на успешный прием данных
        return jsonify({"status": "success", "message": "Webhook received!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
