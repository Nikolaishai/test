from flask import Flask, request, jsonify

app = Flask(__name__)


# Главная страница
@app.route('/')
def home():
    return 'Welcome to the homepage!'


# Веб-хук
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Получаем данные из запроса
        data = request.get_json()

        # Обрабатываем данные (например, выводим их в консоль)
        print("Received webhook data:", data)

        # Ответ на успешный прием данных
        return jsonify({"status": "success", "message": "Webhook received!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
