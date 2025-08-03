import uuid
import uuid
import requests
from config import IAM_TOKEN, FOLDER_ID

def synthesize_text(text):
    url = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"
    headers = {
        "Authorization": f"Bearer {IAM_TOKEN}",
    }
    data = {
        "text": text,
        "lang": "ru-RU",
        "voice": "oksana",  # другие: ermil, zahar, jane
        "folderId": FOLDER_ID,
        "format": "oggopus",
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code != 200:
        raise RuntimeError(f"Ошибка синтеза: {response.text}")

    filename = f"audio_{uuid.uuid4().hex}.ogg"
    with open(filename, "wb") as f:
        f.write(response.content)

    return filename

