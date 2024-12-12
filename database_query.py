import requests

# URL базы данных. /Этот запрос я сделала из Postman на свой локальный сервер с развернутым проектом/
url = "http://127.0.0.1:8000/get_form/"

# GET-запрос
response = requests.get(url)

# Если запрос был успешным
if response.status_code == 200:
    # Данные в формате JSON
    data = response.json()

    # Обработка полученных данных
    for user in data:
        print(f"Name: {user['name']}, Email: {user['email']}")
else:
    print(f"Error: {response.status_code} - {response.text}")