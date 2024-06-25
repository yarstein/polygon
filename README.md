# Polygon Token Balance API

## Описание
Этот проект(тестовое) представляет собой веб-приложение, которое взаимодействует с сетью Polygon.
Приложение позволяет получить баланс и некоторую информацию адресов.

## Функционал
- **Получение баланса конкретного адреса**: `GET http://127.0.0.1:8000/get_balance/?addresses="address"`
- **Получение балансов нескольких адресов**: `GET http://127.0.0.1:8000/get_balance_batch/?addresses=["address1", "address2"]`
- **Получение балансов нескольких адресов**: `POST http://127.0.0.1:8000/get_balance_batch/` с телом запроса JSON: {"addresses": ["address1", "address2"]}
- **Получение информации о токене**: `GET http://127.0.0.1:8000/get_token_info/?address=<address>`

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone polygon
    cd polygon
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```
