# Описание

Данный проект представляет собой RESTful API для социальной сети, где пользователи могут публиковать посты, комментировать их, подписываться на других пользователей и создавать группы с общими интересами. Проект использует Django и Django REST framework.

# Установка

1. Клонируйте репозиторий на свой компьютер.
2. Создайте виртуальное окружение и активируйте его:
    
    ```
    python -m venv venv
    source venv/bin/activate
    
    ```
    
3. Установите зависимости:
    
    ```
    pip install -r requirements.txt
    
    ```
    
4. Создайте миграции:
    
    ```
    python manage.py makemigrations
    python manage.py migrate
    
    ```
    
5. Создайте суперпользователя:
    
    ```
    python manage.py createsuperuser
    
    ```
    
6. Запустите сервер:
    
    ```
    python manage.py runserver
    
    ```
    

# Примеры

Примеры запросов к API:

- Получение списка всех постов:
    
    ```
    GET /api/v1/posts/
    
    ```
    
- Создание нового поста:
    
    ```
    POST /api/v1/posts/
    {
        "text": "Hello, World!",
        "image": "data:image/png;base64,iVBORw0KGg...."
    }
    
    ```
    
- Получение списка комментариев к посту:
    
    ```
    GET /api/v1/posts/1/comments/
    
    ```
    
- Создание нового комментария:
    
    ```
    POST /api/v1/posts/1/comments/
    {
        "text": "Nice post!"
    }
    
    ```
    
- Получение списка всех групп:
    
    ```
    GET /api/v1/groups/
    
    ```
    
- Получение списка постов в группе:
    
    ```
    GET /api/v1/groups/test-group/posts/
    
    ```
    
- Создание новой подписки:
    
    ```
    POST /api/v1/follow/
    {
        "following": "testuser"
    }
    
    ```
