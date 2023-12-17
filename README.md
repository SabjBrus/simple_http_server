# Simple HTTP server

## Простой HTTP сервер на Python

Принимает и выдает записи, состоящие из:

- id: уникальный идентификатор записи
- data: данные в свободном формате

Между запусками сервер сохраняет все ранее сохраненные записи.  
База данных не используется.  
Зависимости отсутствуют.  

## Технологии

- Python >= 3.7

## Порядок запуска сервера

- Склонировать репозиторий:

```bash
git clone https://github.com/SabjBrus/simple_http_server.git
```

- Запуск сервера

```bash
python server.py
```

Сервер доступен по адресу:
<http://127.0.0.1:8080/>

## Примеры запросов

- Сохранение записи:  
POST запрос на ваш сервер. Например:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id":1, "data":"test data"}' http://localhost:8080
```

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id":2, "data":"test data2"}' http://localhost:8080
```

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id":3, "data":"test data3"}' http://localhost:8080
```

- Выдача записи по уникальному инетификатору:  
GET запроса на ваш сервер. Например:

```bash
curl http://localhost:8080/1
```

- Выдача всех записей:  
GET запроса на ваш сервер без указания id. Например:

```bash
curl http://localhost:8080
```
