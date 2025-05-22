import os
from openai import OpenAI
from bs4 import BeautifulSoup
from autocorrect import Speller
from config import API_KEY


client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)

spell = Speller("ru")

def simplify_text(input_html):
    input_html = spell(input_html)
    try:
        soup = BeautifulSoup(input_html, 'html.parser')

        elements = soup.find_all(text=True)
        filtered_text = ' '.join([
            el.strip() for el in elements
            if not el.find_parents(class_=["replaced-word", "simplify-mark"])
        ])

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"""Ты — умный помощник, упрощающий текст. 
Найди трудные или громоздкие слова и фразы в тексте, и предложи до 3 вариантов более простых замен.
‼️ Важно:
- Упрощения должны **сохранять падеж, число, род** и **смысл в контексте**.
- Не предлагай форм, нарушающих грамматику.
- Не меняй уже упрощённые или заменённые слова.
Формат:

сложное_слово → [вариант1, вариант2, вариант3]

Текст:
{filtered_text}"""
                }
            ]
        )

        simplified_pairs = []
        for line in response.choices[0].message.content.split("\n"):
            if "→" in line:
                original, simple_variants = line.split("→")
                original = original.strip()
                variants = [v.strip() for v in simple_variants.strip(" []").split(",")]
                simplified_pairs.append([original, variants])

        for original, simple in simplified_pairs:
            for el in soup.find_all(text=True):
                if original in el and not el.find_parents(class_=["replaced-word", "simplify-mark"]):
                    new_html = str(el).replace(
                        original,
                        f'<span class="simplify-mark" data-original="{original}" data-options="{",".join(variants)}">{original}</span>'

                    )
                    el.replace_with(BeautifulSoup(new_html, 'html.parser'))

        return str(soup), simplified_pairs

    except Exception as e:
        return f"[Ошибка]: {str(e)}", []
