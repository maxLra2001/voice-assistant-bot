import requests
from config import IAM_TOKEN, FOLDER_ID

def ask_yandex_gpt(prompt):
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    headers = {
        "Authorization": f"Bearer {IAM_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt-lite",  # или yandexgpt/latest — если доступен
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": 1000
        },
        "messages": [
            {"role": "user", "text": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        return f"Ошибка YandexGPT: {response.text}"

    result = response.json()
    return result["result"]["alternatives"][0]["message"]["text"]

