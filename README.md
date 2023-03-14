# app_api
app_api
### Технологии
Python 3.9
Django 2.2.19
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
python3 -m venv venv
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команды:
```
python3 manage.py migrate
python3 manage.py load_listings_data
python3 manage.py runserver
```
- Автор Kostya
- tr202@ya.ru