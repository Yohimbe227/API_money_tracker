import requests

bot_token = '6554711613:AAFpxdYy4YEzkiO4LfmGBjH-s7JlmXKvMQo'
chat_id = "400425347"
message_text = 'Привет, это я!'

api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
payload = {
    'chat_id': chat_id,
    'text': message_text
}

response = requests.post(api_url, json=payload)

if response.status_code == 200:
    print('Сообщение успешно отправлено.')
else:
    print('Ошибка отправки сообщения:', response.text)
