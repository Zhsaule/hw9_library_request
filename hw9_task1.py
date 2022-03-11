# Домашнее задание к лекции 9.«Работа с библиотекой requests, http-запросы»
# Задача №1
# Кто самый умный супергерой? Есть API по информации о супергероях.
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
# Для определения id нужно использовать метод /search/name
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.
# -> ⚠️ Недавно сервис SuperHero API переехал на заблокированный Роскомнадзором IP-адрес,
# из-за чего некоторые интернет-провайдеры заблокировали к нему доступ,
# он может быть недоступен. В таком случае решайте это задание на REPL.it — оттуда всё должно быть доступно.


import requests
from pprint import pprint

BASE_URL = "https://superheroapi.com/api/2619421814940190/"


def search_intelligence_get(search_name):
    list_intelligence = list()
    for i in search_name:
        url = BASE_URL + "search/" + i
        response_character = requests.get(url, timeout=5).json()["results"][0]
        list_intelligence.append({'id': response_character["id"],
                                  'name': response_character["name"],
                                  'intelligence': int(response_character["powerstats"]["intelligence"])})
    return list_intelligence


if __name__ == '__main__':
    search_hero = ['Hulk', 'Captain America', 'Thanos']
    results = search_intelligence_get(search_hero)
    pprint(results)

    max_intelligence = {'id': 0, 'name': 'none', 'intelligence': 0}
    for hero in results:
        if max_intelligence['intelligence'] < hero['intelligence']:
            max_intelligence = hero

    print(f'Герой {max_intelligence["name"]} с максимальным уровнем intelligence = {max_intelligence["intelligence"]}')
