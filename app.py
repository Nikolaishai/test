from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Список для хранения полученных веб-хуков
received_webhooks = []

# Главная страница, отображающая полученные веб-хуки
@app.route('/')
def home():
    return render_template('index.html', webhooks=received_webhooks)

# Веб-хук
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Получаем данные из запроса
        data = request.get_json()

        # Добавляем данные веб-хука в список
        received_webhooks.append(data)

        # Выводим данные в консоль на сервере
        print("Received webhook data:", data)

        # Ответ на успешный прием данных
        return jsonify({"status": "success", "message": "Webhook received!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
