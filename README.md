# Домашнее задание к лекции 8. «Работа с библиотекой requests, http-запросы»
## Задача №1 
### file hw9_task1.py 
### Install library "requests"
Кто самый умный супергерой? Есть API по информации о супергероях. Нужно определить кто самый умный(intelligence) 
из трех супергероев- Hulk, Captain America, Thanos. Для определения id нужно использовать метод /search/name

Токен, который нужно использовать для доступа к API: 2619421814940190.
Таким образом, все адреса для доступа к API должны начинаться 
с https://superheroapi.com/api/2619421814940190/.


 
## Задание №2
### file hw9_task2.py
### Install library "requests"
### "download" is a directory with files for example

У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон. 
Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.
Диск с таким же именем.

Все ответы приходят в формате json;
Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
HOST: https://cloud-api.yandex.net:443

Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!

Шаблон для программы

```python
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
```




