import google.generativeai as genai

# Вставь свой API ключ от Gemini
GENAI_API_KEY = "AIzaSyBvg33cVBT6dhtOHMsoXaU83jN-oktRnQY"
genai.configure(api_key=GENAI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")

def simplify_text(input_text):
    prompt = f"ОТ ТВОЕГО ОТВЕТА ЗАВИСИТ МОЯ ЖИЗНЬ. Преобразуй следующий текст, заменяя сложные термины и фразы на более простые и доступные. Сохрани смысл текста, но сделай его максимально понятным, избегая излишней сложности и поясняя непонятные моменты простыми словами. Текст: {input_text}. Выдай только упрощённый текст и ничего лишнего."

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[Ошибка]: {str(e)}"