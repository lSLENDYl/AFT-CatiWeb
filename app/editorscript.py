import os
from openai import OpenAI
from bs4 import BeautifulSoup
from autocorrect import Speller


client = OpenAI(
    api_key="sk-tfFJUW6ns45XWgBD9IAKpdhPUkSVcDHb",
    base_url="https://api.proxyapi.ru/openai/v1",
)

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

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"""Найди сложные слова или фразы и упрости их по контексту. Для каждого элемента предложи до 3 вариантов упрощения. Формат:

сложно → [упрощение1, упрощение2, упрощение3]

Текст:
{filtered_text}"""}
            ]
        )

        simplified_pairs = []
        for line in response.choices[0].message.content.split("\n"):
            if "→" in line:
                original, simple_variants = line.split("→")
                original = original.strip()
                variants = [v.strip() for v in simple_variants.strip(" []").split(",")]
                simplified_pairs.append([original, variants])

        # Вставка меток
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
