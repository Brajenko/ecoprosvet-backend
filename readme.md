# Экопросвет backend

## Зависимости (надо установить отдельно для поддержки не .mp4 видео форматов)
ffmpeg
```bash
sudo apt install ffmpeg
```

## Установка зависимостей
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Настройка
Необходимые переменные окружения, поместите в файл .env
```
DEBUG=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DADATA_API_KEY=
DADATA_SECRET_KEY=
DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_PASSWORD=
```

## Запуск
python manage.py runserver

