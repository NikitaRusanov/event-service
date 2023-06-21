# Это сервис, автоматизирующий отслеживание актуальных мероприятий в городе

Сервис разработан в качестве учебного проекта и представляет из себя REST HTTP API. Основная цель проекта научится работать c fastapi и разобраться с основами SQLAlchemy. 

Технологии использующиеся в проекте: 
* Fastapi
* SQLAlchemy

# Установка и запуск

1. Склонировать репозиторий
2. Выполнить команду ```pip install -r requirements.txt``` в корне проекта
3. Создать базу данных SQLite (файл с расширением .db)
4. Создать файл с переменными окружения (.env) и задать в нём переменную окружения ```DB_URL = 'sqlite://путь_файла_с_базой_данных'```
5. Выполнить комманду ```python -m uvicorn main:app```
6. Теперь всё готово