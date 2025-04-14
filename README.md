<p align="center">
  <img src="https://i.ibb.co/MkHwcFYS/cute-black-cat-in-glasses-black-wallpaper.jpg" alt="CatiWeb Team"/>
</p>

## Проект сделан для международного фестиваля «Технострелка»
Кейс «Адаптация формальных текстов» от Лаборатории Инклюзивных Технологий при правительстве Нижегородской области.
## Цель проекта
Создание инсрумента для трансформации сложных официальных текстов в доступный формат, понятный широкой аудитории.
## Справка по проекту
Данный проект создан для людей, у которых возникают трудности с написанием или упрощением текста.
### Функции
**Редактор** - помогает человеку написать текст в реальном времени, предлагая сделать замену сложных и непонятных слов в синонимы, которые входят в общеупотребильную лексику.
<p align="center">
  <img src="app\static\img\editor.png" alt="Editor" width="536" height="352"/>
</p>

**Упроститель** - необходим для анализа и адаптации уже существующих текстов в более простые и понятные для широкой массы людей.
<p align="center">
  <img src="app\static\img\simplifier.png" alt="Simplifier" width="536" height="352"/>
</p>


## Настройка проекта
Устанавливаем проект в ручную или через git
```
git clone https://github.com/lSLENDYl/AFT-CatiWeb
```
Создаём окружение в папке с проектом
```
python -m venv venv
```
Активируем окружение
```
venv\Scripts\activate
```
Устанавливаем нужные библиотеки
```
pip install -r requirements.txt
```
## Запуск
```
flask run
```
> [!NOTE]
> Убедитесь, что у вас установились все словари для корректной работы библиотеки autocorrect.
