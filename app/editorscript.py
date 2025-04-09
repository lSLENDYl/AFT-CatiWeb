# import os
# import requests
from openai import OpenAI

client = OpenAI(
    api_key="sk-tfFJUW6ns45XWgBD9IAKpdhPUkSVcDHb",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# API_KEY = os.environ["API_KEY"]
#
# url = "https://api.intelligence.io.solutions/api/v1/chat/completions"
#
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {API_KEY}"
# }

def simplify_text(input_text):
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=f"""Задача:
Найди в тексте сложные слова и формулировки и выведи в виде списка их упрощения следуя контексту и их самих.

Дополнительные условия:
Без воды, лишнего текста и информации. Только сухой ответ следуя формату.
Упрощения должны быть написаны так, чтобы их можно было подставить в текст сразу, без изменения вручную.

Формат:
слово или формулировка → упрощение
слово или формулировка → упрощение
слово или формулировка → упрощение

Текст:
{input_text}"""
    )

    try:
        simple = [i.split(" → ") for i in response.output_text.split("\n")]
        print(response.output_text)
        print(simple)
        for i in simple:
            if i[0].strip() != "" and i[0] in input_text:
                input_text = input_text.replace(i[0], i[1])
        print(input_text)
        return input_text
    except Exception as e:
        return f"[Ошибка]: {str(e)}"







#     data = {
#         "model": "deepseek-ai/DeepSeek-R1",
#         "messages": [
#             {
#                 "role": "system",
#                 "content": "You are a helpful assistant."
#             },
#             {
#                 "role": "user",
#                 "content": f"""Задача:
# Найди в тексте сложные слова и формулировки и выведи в виде списка их упрощения следуя контексту и их самих.
#
# Дополнительные условия:
# Без воды, лишнего текста и информации. Только сухой ответ следуя формату.
# Упрощения должны быть написаны так, чтобы их можно было подставить в текст сразу, без изменения вручную.
# В конце выведи текст с изменёнными формулировками и словами, которые ты сгенерировал.
#
# Формат:
# слово или формулировка → упрощение
# слово или формулировка → упрощение
# слово или формулировка → упрощение
#
# Текст:
# {input_text}"""
#             }
#         ]
#     }

    # pprint(data)
    #
    # try:
    #     response = requests.post(url, headers=headers, json=data)
    #     data = response.json()
    #     print("\n\n\n\n\n\n\n")
    #     pprint(data)
    #
    #     text = data['choices'][0]['message']['content']
    #     return text.split('</think>\n\n')[1]
    # except Exception as e:
    #     return f"[Ошибка]: {str(e)}"