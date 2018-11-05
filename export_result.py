# coding: utf8
u"""Модуль вывода результата оценки охвата на вики-страничку в ВК."""


import os
import input_data
import output_data
import data_manager


def exporting(vk_session):
    u"""Функция вывода текстовой строки на вики-страничку в ВК."""
    def select_date_log(PATH, type_posts):
        u"""Получает дату из первого и последнего лог-файлов."""
        def collection_file_names(PATH, type_posts):
            u"""Собирает названия json-файлов с логами."""
            list_file_names = os.listdir(PATH + "json/" + type_posts + "/")
            for i, file_name in enumerate(list_file_names):
                list_file_names[i] = list_file_names[i].replace(".json", "")

            return list_file_names

        def sort_file_names(list_file_names):
            u"""Сортирует названия файлов."""
            def sort_by_daynumber(dict_by_month):
                u"""Сортирует названия по числам."""
                months = [
                    "jan", "feb", "mar",
                    "apr", "may", "jun",
                    "jul", "aug", "sep",
                    "oct", "nov", "dec"
                ]
                sorted_list = []

                for month in months:
                    list_file_names = dict_by_month[month]
                    for i in range(31):
                        for file_name in list_file_names:
                            pos = file_name.lower().find("_" + str(i + 1) + "-")
                            if pos > -1:
                                sorted_list.append(file_name)
                return sorted_list

            def sort_by_months(list_file_names):
                u"""Сортирует названия по месяцам."""
                months = [
                    "jan", "feb", "mar",
                    "apr", "may", "jun",
                    "jul", "aug", "sep",
                    "oct", "nov", "dec"
                ]

                dict_by_month = {
                    "jan": [],
                    "feb": [],
                    "mar": [],
                    "apr": [],
                    "may": [],
                    "jun": [],
                    "jul": [],
                    "aug": [],
                    "sep": [],
                    "oct": [],
                    "nov": [],
                    "dec": []
                }

                for file_name in list_file_names:
                    for month in months:
                        pos = file_name.lower().find(month)
                        if pos > -1:
                            dict_by_month[month].append(file_name)

                return dict_by_month

            dict_by_month = sort_by_months(list_file_names)
            list_file_names = sort_by_daynumber(dict_by_month)

            return list_file_names

        list_file_names = collection_file_names(PATH, type_posts)
        list_file_names = sort_file_names(list_file_names)

        first_log = data_manager.read_json(PATH + "json/" + type_posts + "/",
                                           list_file_names[0])
        first_log_date = str(first_log["day_number"]) + "." + \
            str(first_log["month_number"]) + "." + \
            str(first_log["year"])

        last_file_number = len(list_file_names) - 1
        last_log = data_manager.read_json(PATH + "json/" + type_posts + "/",
                                          list_file_names[last_file_number])
        last_log_date = str(last_log["day_number"]) + "." + \
            str(last_log["month_number"]) + "." + \
            str(last_log["year"])
        
        log_dates = {
            "first": first_log_date,
            "last": last_log_date
        }

        return log_dates

    def make_output_text(PATH, log_dates, type_posts):
        u"""Формирует выходной текст для вики-странички."""
        text_output = ""
        text_output += "\'\'Дата первого лога: " + log_dates["first"] + "\'\'\n"
        text_output += "\'\'Дата последнего лога: " + log_dates["last"] + " \'\'\n"

        log_output = data_manager.read_text(PATH + "output/",
                                            type_posts + "_log_output")

        text_output += "\n" + log_output

        return text_output


    PATH = data_manager.read_path()
    data = data_manager.read_json(PATH + "res/", "data")
    ads_wiki_page_data = data["wiki_pages"]["ads"]
    posts_wiki_page_data = data["wiki_pages"]["posts"]

    ads_log_dates = select_date_log(PATH, "ads")
    posts_log_dates = select_date_log(PATH, "posts")

    text_output_ads_logs = make_output_text(PATH, ads_log_dates, "ads")
    text_output_posts_logs = make_output_text(PATH, posts_log_dates, "posts")

    output_data.export_data_to_wiki_page(vk_session,
                                         text_output_ads_logs,
                                         ads_wiki_page_data)
    output_data.export_data_to_wiki_page(vk_session,
                                         text_output_posts_logs,
                                         posts_wiki_page_data)
