import os
import requests

API_KEY = os.environ["API_KEY"]

url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def simplify_text(input_text):
    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"""Задача:
                    Найди в тексте сложные слова и формулировки и выведи в виде списка их упрощения следуя контексту и их самих.

                    Дополнительные условия:
                    Без воды, лишнего текста и информации. Только сухой ответ следуя формату.
                    Упрощения должны быть написаны так, чтобы их можно было подставить в текст сразу, без изменения вручную.
                    В конце выведи текст с изменёнными формулировками и словами, которые ты сгенерировал.

                    Формат:
                    слово или формулировка → упрощение
                    слово или формулировка → упрощение
                    слово или формулировка → упрощение

                    Текст:
                    {input_text}"""
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        data = response.json()
        # pprint(data)

        text = data['choices'][0]['message']['content']
        return text.split('</think>\n\n')[1]
    except Exception as e:
        return f"[Ошибка]: {str(e)}"