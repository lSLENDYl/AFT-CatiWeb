# import os
# import requests
from openai import OpenAI
from bs4 import BeautifulSoup
from app.config import API_KEY
from autocorrect import Speller


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

spell = Speller("ru")

def simplify_text(input_html):
    input_html = spell(input_html)
    try:
        soup = BeautifulSoup(input_html, 'html.parser')

        # Игнорировать текст в уже заменённых участках
        elements = soup.find_all(text=True)
        filtered_text = ' '.join([
            el.strip() for el in elements
            if not el.find_parents(class_=["replaced-word", "simplify-mark"])
        ])

        response = client.responses.create(
            model="gpt-3.5-turbo",
            input=f"""Найди сложные слова или фразы и упрости их по контексту.

Формат:
оригинал → упрощение

Текст:
{filtered_text}"""
        )

        simplified_pairs = []
        for line in response.output_text.split("\n"):
            if "→" in line:
                parts = line.split("→")
                original = parts[0].strip()
                simple = parts[1].strip()
                simplified_pairs.append([original, simple])

        # Вставка меток
        for original, simple in simplified_pairs:
            for el in soup.find_all(text=True):
                if original in el and not el.find_parents(class_=["replaced-word", "simplify-mark"]):
                    new_html = str(el).replace(
                        original,
                        f'<span class="simplify-mark" data-original="{original}" data-simple="{simple}">{original}</span>'
                    )
                    el.replace_with(BeautifulSoup(new_html, 'html.parser'))

        return str(soup), simplified_pairs

    except Exception as e:
        return f"[Ошибка]: {str(e)}", []
