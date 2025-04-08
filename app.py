import tkinter as tk
from tkinter import ttk
import google.generativeai as genai

# Вставь свой API ключ от Gemini
GENAI_API_KEY = "AIzaSyBvg33cVBT6dhtOHMsoXaU83jN-oktRnQY"
genai.configure(api_key=GENAI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-002")

def simplify_text():
    audience = audience_var.get()
    input_text = input_box.get("1.0", tk.END).strip()
    prompt = f"напиши только несколько (по возможности) вариантов понятных для аудитории: {audience} синонимов слова {input_text}. Без воды и лишних слов. Если их нет, то просто ничего не пиши. Используй только самые близкие по значению синонимы"

    try:
        response = model.generate_content(prompt)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, response.text)
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"[Ошибка]: {str(e)}")

# Интерфейс
root = tk.Tk()
root.title("Упрощение формального текста")

root.geometry("800x600")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# Верхняя панель
tk.Label(root, text="Выберите аудиторию:").pack()
audience_var = tk.StringVar(value="Школьник")
audience_menu = ttk.Combobox(root, textvariable=audience_var)
audience_menu["values"] = ["Школьник", "Студент", "Широкая публика", "Пожилые люди", "Иностранцы"]
audience_menu.pack(fill=tk.X, padx=10, pady=5)

# Ввод
tk.Label(root, text="Формальный текст:").pack()
input_box = tk.Text(root, height=10, wrap=tk.WORD)
input_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Кнопка
tk.Button(root, text="Упростить текст", command=simplify_text).pack(pady=10)

# Вывод
tk.Label(root, text="Упрощённый текст:").pack()
output_box = tk.Text(root, height=10, wrap=tk.WORD, bg="#f0f0f0")
output_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

root.mainloop()
