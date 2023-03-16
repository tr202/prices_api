# app_api
app_api
### Технологии
Python 3.9
Django 2.2.19
Docker
### Запуск проекта в dev-режиме
- Скопируйте проект на хост с докер 
```
git clone https://github.com/tr202/prices_api.git
```
- В папке с Dockerfile выполните команды
```
docker build .
docker run -it 8000:8000 <номер контейнера из вывода предыдущей команды>
``` 
- Автор Kostya
- tr202@ya.ru