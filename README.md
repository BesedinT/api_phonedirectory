# API_PHONEDIRECTORY

Телефонный справочник (API сервис)

## Основные функции:

- Вывод постранично записей из справочника на экран
- Добавление новой записи в справочник
- Возможность редактирования записей в справочнике
- Поиск записей по нескольким полям
- Справочник позволяет сохранить следующую информацию: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный   

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека django-filter - фильтрация запросов
- база данных - SQLite3
- система управления версиями - git

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:BesedinT/api_phonedirectory.git
```
В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python -m venv venv
```
```
. venv/bin/activate
```
```
pip install -r requirements.txt
```
Выполните миграции:
```
python manage.py migrate
```
Создайте суперпользователя:
```
python manage.py createsuperuser
```
Запустите сервер:
```
python manage.py runserver
```

# Примеры запросов и ответов:

**Получение списка всех контактов:**

GET http://127.0.0.1:8000/api/contacts/

*Ответ 200 OK:*
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "last_name": "string",
        "first_name": "string",
        "patronymic": "string",
        "company": "string",
        "work_phone": "phone number",
        "personal_phone": "phone number"
        }
      }
    ]
  }
]
```
**Добавление контакта:**

POST http://127.0.0.1:8000/api/contacts/
```
{
  "last_name": "string",
  "first_name": "string",
  "patronymic": "string",
  "company": "string",
  "work_phone": "phone number",
  "personal_phone": "phone number"
}
```
*Ответ 201 CREATED:* 

**Получение конкретной записи:**

GET http://127.0.0.1:8000/api/contacts/{id}

*Ответ 200 OK:*
```
{
    "id": 0,
    "last_name": ""string"",
    "first_name": ""string",
    "patronymic": "string",
    "company": "string",
    "work_phone": "phone number",
    "personal_phone": "phone number"
}
```
