# coding: utf8
u"""Модуль создания файла template.json."""


import copy
import input_data
import data_manager


def run_template_json_creator():
    u"""Запуск основных функций создания файла template.json."""
    def save_template_json(template):
        u"""Сохраняет готовый словарь template во внешний файл."""
        PATH = data_manager.read_path()
        data_manager.write_json(PATH + "res/", "template", template)
    template, value = initialization_file()
    values = select_data(value)
    template["values"] = values
    save_template_json(template)


def initialization_file():
    template = {
        "values": []
    }
    value = {
        "time_begin": "",
        "time_end": "",
        "post_count": 0,
        "value": 0
    }

    return template, value


def select_data(value):
    number_intervals = input_data.get_number_time_intervals()
    values = []
    for i in range(number_intervals):
        new_value = copy.deepcopy(value)
        new_value["time_begin"] = input_data.get_time("begin")
        new_value["time_end"] = input_data.get_time("end")
        values.append(new_value)
    return values
