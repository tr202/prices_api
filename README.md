# app_api
Test task, api with query filtering and csv data import, dockerized
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
Проверьте работу
```
http://<ip или имя вашего хоста например - localhost>:8080/listings?min_price=0.0081&max_price=0.15&min_min_cpm=1&max_min_cpm=2
```
- Автор Kostya
- tr202@ya.ru
