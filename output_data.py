# coding: utf8
u"""Модуль вывода данных."""


import data_manager
import vk_api


def show_data_to_console(data_to_show):
    u"""Вывод данных в консоль."""
    print data_to_show


def export_data_to_file(data_to_file, type_posts):
    u"""Вывод json-словаря в json-файл."""
    def select_file_name(log_reach):
        u"""Получение имени файла."""
        weekdays = [
            "mon", "tue", "wed",
            "thu", "fri", "sat",
            "sun"
        ]

        months = [
            "jan", "feb", "mar",
            "apr", "may", "jun",
            "jul", "aug", "sep",
            "oct", "nov", "dec"
        ]
        file_name = "log_" + str(log_reach["day_number"])
        file_name += "-" + months[log_reach["month_number"] - 1]
        file_name += "-" + weekdays[log_reach["day_week"] - 1]

        return file_name

    file_name = select_file_name(data_to_file)

    PATH = data_manager.read_path()
    data_manager.write_json(PATH + "json/" + type_posts + "/",
                            file_name, data_to_file)


def export_data_to_text(data_to_text, type_posts):
    u"""Вывод текстовой строки в текстовый файл."""
    PATH = data_manager.read_path()
    data_manager.write_text(PATH + "output/", type_posts + "_log_output", 
                            data_to_text)


def export_data_to_wiki_page(vk_session, data_to_wiki, wiki_page_data):
    u"""Вывод текстовой строки на вики-страничку в ВК."""
    values = {
        "text": data_to_wiki,
        "page_id": wiki_page_data["id"],
        "group_id": wiki_page_data["owner_id"]
    }
    vk_session.method("pages.save", values)
