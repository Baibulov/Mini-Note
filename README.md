# Mini-Note API

API-сервис для управления заметками с полным CRUD-функционалом.

## Описание

Backend-сервис для управления заметками, реализованный на FastAPI. Предоставляет RESTful API для создания, чтения, обновления и удаления заметок.

## Технологии

- **Python** - язык программирования
- **FastAPI** - современный веб-фреймворк для создания API
- **Pydantic** - библиотека для валидации данных
- **Uvicorn** - ASGI-сервер для запуска приложения

## Функционал

- ✅ **Create** - создание новой заметки
- ✅ **Read** - получение заметок (всех или по ID)
- ✅ **Update** - обновление существующей заметки
- ✅ **Delete** - удаление заметки

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd Petproject
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
```

### 3. Активация виртуального окружения

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 5. Запуск приложения

```bash
python main.py
```

или

```bash
uvicorn main:app --reload
```

Сервер запустится на `http://localhost:8000`

## API Endpoints

### Корневой endpoint
- `GET /` - информация об API

### Заметки
- `POST /notes` - создать новую заметку
- `GET /notes` - получить все заметки
- `GET /notes/{note_id}` - получить заметку по ID
- `PUT /notes/{note_id}` - обновить заметку
- `DELETE /notes/{note_id}` - удалить заметку

## Документация API

После запуска сервера доступна интерактивная документация:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Примеры использования

### Создание заметки

```bash
curl -X POST "http://localhost:8000/notes" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Моя первая заметка",
    "content": "Это содержимое заметки",
    "tags": ["важное", "работа"]
  }'
```

### Получение всех заметок

```bash
curl -X GET "http://localhost:8000/notes"
```

### Обновление заметки

```bash
curl -X PUT "http://localhost:8000/notes/{note_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Обновленный заголовок",
    "content": "Обновленное содержимое"
  }'
```

### Удаление заметки

```bash
curl -X DELETE "http://localhost:8000/notes/{note_id}"
```

## Структура проекта

```
Petproject/
├── main.py              # Основной файл приложения
├── requirements.txt     # Зависимости проекта
├── README.md           # Документация
└── .gitignore          # Игнорируемые файлы
```

## Автор

Проект разработан в рамках обучения FastAPI и REST API.

