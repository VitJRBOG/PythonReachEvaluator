# coding: utf8
u"""Модуль создания файла data.json."""


import input_data
import data_manager


def run_data_json_creator():
    u"""Запуск основных функций создания файла data.json."""
    def save_data_json(data):
        u"""Сохраняет готовый словарь data во внешний файл."""
        PATH = data_manager.read_path()
        data_manager.write_json(PATH + "res/", "data", data)

    data = initialization_file()
    data = select_data(data)
    save_data_json(data)


def initialization_file():
    u"""Инициализация словаря data."""
    data = {
        "public_url": "",
        "wiki_pages": {
            "ads": {
                "url": "",
                "owner_id": "",
                "id": ""
            },
            "posts": {
                "url": "",
                "owner_id": "",
                "id": ""
            }
        }
    }
    return data


def select_data(data):
    u"""Сбор необходимых данных."""
    def select_wiki_page_signatures(wiki_page_url):
        u"""Получение owner_id и id вики-странички."""
        if wiki_page_url.find("https://vk.com/page-") > -1:
            signature_wiki_page = wiki_page_url.replace(
                "https://vk.com/page-", "")
            wiki_page_owner_id = select_wiki_page_owner_id(signature_wiki_page)
            wiki_page_id = select_wiki_page_id(
                wiki_page_owner_id, signature_wiki_page)
            return wiki_page_owner_id, wiki_page_id

    def select_wiki_page_owner_id(signature_wiki_page):
        u"""Извлечение owner_id из url вики-странички."""
        wiki_page_owner_id = ""
        pos = signature_wiki_page.find("_")
        if pos > -1:
            wiki_page_owner_id = signature_wiki_page[0:pos]
        return wiki_page_owner_id

    def select_wiki_page_id(wiki_page_owner_id, signature_wiki_page):
        u"""Извлечение id из сигнатуры вики-странички."""
        wiki_page_id = ""
        if signature_wiki_page.find(wiki_page_owner_id) > -1:
            wiki_page_id = signature_wiki_page.replace(
                wiki_page_owner_id + "_", "")
        return wiki_page_id

    public_url = input_data.get_public_url()
    wiki_page_ads_url = input_data.get_wiki_page_url("ads")
    wiki_page_posts_url = input_data.get_wiki_page_url("posts")
    wiki_page_ads_owner_id, wiki_page_ads_id = select_wiki_page_signatures(
        wiki_page_ads_url)
    wiki_page_posts_owner_id, wiki_page_posts_id = select_wiki_page_signatures(
        wiki_page_posts_url)

    data["public_url"] = public_url
    data["wiki_pages"]["ads"]["url"] = wiki_page_ads_url
    data["wiki_pages"]["posts"]["url"] = wiki_page_posts_url
    data["wiki_pages"]["ads"]["owner_id"] = wiki_page_ads_owner_id
    data["wiki_pages"]["ads"]["id"] = wiki_page_ads_id
    data["wiki_pages"]["posts"]["owner_id"] = wiki_page_posts_owner_id
    data["wiki_pages"]["posts"]["id"] = wiki_page_posts_id

    return data
