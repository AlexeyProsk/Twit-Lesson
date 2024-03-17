ТЗ:
1. Необходимо разработать REST API, предоставляющее возможность ведения блога.

2. API должен иметь минимум 2 сущности:

    Пользователь
    Пост

3. Пользователь должен иметь возможность:

    создать
    прочитать
    изменить
    удалить пост

4. Задание должно быть выполнено с помощью фреймворка Flask.

5. Задание необходимо предоставить в виде архива с исходными кодом или ссылки на репозиторий в github/gitlab

    помимо кода, должна быть краткая инструкция по запуску задания
    в инструкции необходимо указать примеры тела запросов, HTTP метод и соответствующие URL для осуществления операций

Инструкция:

1. **Запуск приложения:**
- Убедитесь, что у вас установлен Python и Flask.
- Клонируйте репозиторий с помощью следующей команды:
```
git clone https://github.com/AlexeyProsk/Twit-Lesson.git
```
- Запустите приложение с помощью команды python app.py.
2. **Примеры операций:**
- **Создание поста (Create):**
- HTTP метод: POST
- URL: http://127.0.0.1:5000/twit
- Тело запроса:
json
{
"body": "Текст поста",
"author": "Имя автора"
}


- **Получение всех постов (Read):**
- HTTP метод: GET
- URL: http://127.0.0.1:5000/twit


- **Обновление поста (Update):**
- HTTP метод: PUT
- URL: http://127.0.0.1:5000/twit/<id_поста>
- Тело запроса (можно обновить body и/или author):
json
{
"body": "Новый текст поста",
"author": "Новое имя автора"
}


- **Удаление поста (Delete):**
- HTTP метод: DELETE
- URL: http://127.0.0.1:5000/twit/<id_поста>
3. **Пример использования:**
- Создайте новый пост: отправьте POST запрос с указанным телом запроса.
- Получите все посты: отправьте GET запрос на /twit.
- Обновите пост: отправьте PUT запрос с новым телом запроса и указанием id поста.
- Удалите пост: отправьте DELETE запрос с указанием id поста.