from flask import Flask, request, jsonify
import os

app = Flask(__name__)
chat_log_path = 'chatlogs.txt'

@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    if message:
        with open(chat_log_path, 'a') as f:
            f.write(message + '\n')
    return '', 204

@app.route('/chat-log', methods=['GET'])
def get_chat_log():
    if os.path.exists(chat_log_path):
        with open(chat_log_path, 'r') as f:
            messages = f.readlines()
        messages = [msg.strip() for msg in messages]
    else:
        messages = []
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
