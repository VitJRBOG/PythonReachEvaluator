# coding: utf8
u"""Модуль оценки охвата по данным из лог-файлов."""


import os
import data_manager


def evaluate(type_posts):
    u"""Оценка охвата постов."""
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

    def filter_by_weekdays(list_file_names):
        u"""Распределяет имена файлов в словарь по дням недели."""
        weekdays = [
            "mon", "tue", "wed",
            "thu", "fri", "sat",
            "sun"
        ]

        dict_by_weekdays = {
            "mon": [],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": []
        }

        for file_name in list_file_names:
            for weekday in weekdays:
                pos = file_name.lower().find(weekday)
                if pos > -1:
                    dict_by_weekdays[weekday].append(file_name)

        return dict_by_weekdays

    def evaluation(dict_by_weekdays, type_posts):
        u"""Оценивает охват из json-файлов."""
        def read_files_by_weekdays(list_file_names, type_posts):
            u"""Читает json-файлы по дням недели."""
            PATH = data_manager.read_path()
            logs_by_weekday = []

            for file_name in list_file_names:
                log_reach = data_manager.read_json(PATH + "json/" +
                                                   type_posts + "/",
                                                   file_name)
                logs_by_weekday.append(log_reach)

            return logs_by_weekday

        def processing(logs):
            u"""Вычисляет средние значения охвата."""
            PATH = data_manager.read_path()

            template = data_manager.read_json(PATH + "res/", "template")

            template_values = template["values"]

            for i, template_value in enumerate(template_values):
                values_count = 0
                for j, log_per_day in enumerate(logs):
                    log_values = log_per_day["values"]
                    if log_values[i]["post_count"] > 0:
                        template_value["value"] += log_values[i]["value"]
                        template_value["post_count"] += log_values[i]["post_count"]
                        values_count += 1
                if values_count > 1:
                    mid_value = template_value["value"] / values_count
                    mid_value = int(mid_value / 100) * 100
                    template_value["value"] = mid_value
                template_values[i] = template_value
                    
            template["values"] = template_values

            return template

        weekdays = [
            "mon", "tue", "wed",
            "thu", "fri", "sat",
            "sun"
        ]
        evaluated_reach = {}

        for weekday in weekdays:
            list_files_by_weekday = dict_by_weekdays[weekday]
            logs_by_weekday = read_files_by_weekdays(list_files_by_weekday,
                                                     type_posts)
            evaluated_reach.update({weekday: processing(logs_by_weekday)})

        return evaluated_reach

    def sort_by_reach_values(evaluated_reach):
        u"""Сортирует списки со значениями по среднему значению охвата."""
        def bubble_method(array):
            u"""Сортировка списка методом <<пузырька>>."""
            for j in range(len(array) - 1):
                f = 0

                for i in range(len(array) - 1 - j):
                    if array[i]["value"] < array[i + 1]["value"]:
                        x = array[i]
                        y = array[i + 1]
                        array[i + 1] = x
                        array[i] = y
                        f = 1
                if f == 0:
                    break

            return array
        weekdays = [
            "mon", "tue", "wed",
            "thu", "fri", "sat",
            "sun"
        ]

        for weekday in weekdays:
            item = evaluated_reach[weekday]["values"]
            evaluated_reach[weekday]["values"] = bubble_method(item)

        return evaluated_reach

    def make_output_text(evaluated_reach):
        u"""Формирует выходной текст с оценкой охвата."""
        def select_values_by_weekday(values):
            u"""Формирует выходной текст из значений за день недели."""
            text_output_by_weekday = ""

            for i, item in enumerate(values["values"]):
                text_output_by_weekday += str(i + 1) + ") "
                text_output_by_weekday += item["time_begin"] + "-" + \
                    item["time_end"]
                text_output_by_weekday += " (" + str(item["value"]) + ")"
                text_output_by_weekday += " (" + str(item["post_count"]) + \
                    ")\n"
                if i == 8:
                    break

            return text_output_by_weekday

        weekdays = [
            "mon", "tue", "wed",
            "thu", "fri", "sat",
            "sun"
        ]
        ru_weekday_names = {
            "mon": u"Понедельник",
            "tue": u"Вторник",
            "wed": u"Среда",
            "thu": u"Четверг",
            "fri": u"Пятница",
            "sat": u"Суббота",
            "sun": u"Воскресенье"
        }

        text_output = ""

        for weekday in weekdays:
            text_output_by_weekday =\
                select_values_by_weekday(evaluated_reach[weekday])
            text_output += "===" + ru_weekday_names[weekday] + "===" + "\n"
            text_output += "\n" + text_output_by_weekday + "\n"

        text_output = text_output.encode("utf8")

        return text_output

    PATH = data_manager.read_path()
    list_file_names = collection_file_names(PATH, type_posts)

    list_file_names = sort_file_names(list_file_names)
    dict_by_weekdays = filter_by_weekdays(list_file_names)

    evaluated_reach = evaluation(dict_by_weekdays, type_posts)
    evaluated_reach = sort_by_reach_values(evaluated_reach)

    text_output = make_output_text(evaluated_reach)

    return text_output
