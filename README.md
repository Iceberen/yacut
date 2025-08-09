# 🐍 YA_CUT
Проект для укорачивания длинных ссылок. Yacut — это веб-приложение, разработанное с использованием Python и Flask.

---

## 📊 Описание
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать   
длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь   
или предоставляет сервис.    
У API имется два эндпоинта:
```
http://localhost:5000/api/id/ для создания короткой ссылки.
```
и    
```
http://localhost:5000/api/id/{short_id} для получения оригинальной ссылки по короткой ссылки short_id.
```

---

## 📄 Документация API
Документация API доступна в формате OpenAPI:
```
openapi.yml
```
Также предоставлена коллекция Postman для удобного тестирования API:
```
postman_collection/Yacut.postman_collection.json
```

---

## 🛠 Технологии
- Python 3.9+
- Flask — веб-фреймворк
- Flask-Migrate — миграции базы данных
- Flask-SQLAlchemy — ORM для работы с базой данных
- SQLite/PostgreSQL — база данных (в зависимости от конфигурации)
- WTForms — обработка форм
- pytest — тестирование
- Postman — тестирование API

---

## ⚙️ Установка
1. Клонировать репозиторий и перейти в него:
    ```
    git clone https://github.com/Iceberen/yacut.git
    cd yacut
    ```
2. Cоздать и активировать виртуальное окружение:
    ```
    python3 -m venv venv
    source venv/bin/activate # Linux/macOS
    source venv/scripts/activate # windows
    ```

3. Установить зависимости из файла `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```
4. Создать файл `.env` и прописать константы как в `.env.example`:
5.  Применить миграции:
    ```
    flask db upgrade
    ```
6. запуск проетка:
    ```
    flask run
    ```
7. Готово! Проект будет доступен по адресу [http://localhost:5000/](http://localhost:5000/)     

---

## 🧪 Тестирование
Для запуска тестов используйте:
    ```
    pytest
    ```

---

## 🧩 Структура проекта
```
yacut
├── migrations                # Скрипты миграций базы данных
├── openapi.yml               # Спецификация OpenAPI для API
├── postman_collection        # Коллекция Postman для тестирования API
├── requirements.txt          # Зависимости проекта
├── settings.py               # Конфигурация приложения
├── tests                     # Тесты приложения
└── yacut                     # Основной пакет приложения
    ├── api_views.py          # Обработчики API маршрутов
    ├── constants.py          # Константы проекта
    ├── error_handlers.py     # Обработчики ошибок
    ├── forms.py              # Определения форм
    ├── models.py             # Модели базы данных
    ├── services.py           # Логика приложения
    ├── static                # Статические файлы (CSS, JS, изображения)
    ├── templates             # HTML-шаблоны для фронтенда
    ├── utils.py              # Вспомогательные функции
    ├── validators.py         # Кастомные валидаторы
    └── views.py              # Обработчики обычных маршрутов (не API)
```

---

## 🧑‍💻 Автор

Разработано: [Iceberen](https://github.com/Iceberen) в рамках учебного спринта по Flask.

---