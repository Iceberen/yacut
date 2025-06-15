# 🐍 YA_CUT
Проект для укорачивания длинных ссылок.    

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

## ⚙️ Установка
- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Iceberen/yacut.git
cd yacut
```
- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

- Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
- Создать файл ".env" и прописать константы как в .env.example:
- Применить миграции:
```
flask db upgrade
```
- запуск проетка:
```
flask run
```
Проект будет доступен по адресу [http://localhost:5000/](http://localhost:5000/)     

### Технологии:
- Python 3.9+
- Flask
- SQLAlchemy

#### Автор - студен когорты 50+:
[Васильев Вячеслав](https://github.com/Iceberen).