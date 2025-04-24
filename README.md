# Запуск Django-приложения с PostgreSQL через Docker

## Описание

Этот проект представляет собой Django-приложение, использующее базу данных PostgreSQL. Все сервисы запускаются с помощью
`docker compose`.

## Настройка

#### 1. Склонируйте репозиторий

#### 2. Убедитесь, что у вас установлен Docker (Docker Compose)

#### 3. Создайте файл окружения `.env`:

```bash
cp example.env .env
```

#### 4. Отредактируйте .env, если необходимо:

    BACKEND_PORT=8000
    DJANGO_DEBUG=True
    DJANGO_SECRET=django-insecure-abracadabra
    DJANGO_ALLOWED_HOSTS=*
    
    POSTGRES_USER=user_name
    POSTGRES_PASSWORD=1234567890
    POSTGRES_DB=db_name
    POSTGRES_HOST=host_name
    POSTGRES_PORT=5432

> [!CAUTION]
> POSTGRES_HOST должен соответствовать названию сервиса БД из docker-compose.yml (db).

## Запуск

#### 1. Соберите и запустите контейнеры:

```bash
docker compose up -d --build
```

#### 2. Примените миграции:

```bash
docker compose exec backend python manage.py migrate
```

#### 3. Соберите статику:

```bash
docker compose exec backend python manage.py collectstatic
```

#### 3. Создайте суперпользователя (если необходимо, для доступа к админке):

```bash
docker compose exec backend python manage.py createsuperuser
```

#### 4. Приложение будет доступно по адресу: http://localhost

