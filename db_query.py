import requests

url = 'http://127.0.0.1:8000/get_form/' #/Этот запрос я тоже сделала из Postman/

data = {
    'user_email': 'test@example.com',
    'user_phone': '+7 123 456 78 90',
    'order_date': '2024-12-11',
    'lead_text': 'Some lead text'
}

response = requests.post(url, data=data)

print(response.json()) # ответ от сервера