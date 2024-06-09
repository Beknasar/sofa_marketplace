FROM python:3.10.0-slim

# Установление рабочей директории в контейнере
WORKDIR /app/source

# Копируем файлы с зависимостями и проект в контейнер
COPY requirements.txt /app/
COPY source /app/source/

# Устанавливаем зависимости
RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Установка переменных окружения (если необходимо)
# ENV SUPERUSER_PASSWORD=<your_password>

