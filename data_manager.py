# coding: utf-8
u"""Модуль чтения и записи внешних файлов."""


import json


def read_path():
    u"""Чтение файла с путем к директории с файлами-ресурсами."""
    path = str(open("path.txt", "r").read())

    if len(path) > 0 and path[len(path) - 1] != "/":
        path += "/"

    return path


def read_json(path, file_name):
    u"""Чтение json-файла."""
    loads_json = json.loads(open(str(path) + str(file_name) +
                                 ".json", 'r').read())

    return loads_json


def write_json(path, file_name, loads_json):
    u"""Запись json-словаря в json-файл."""
    file_json = open(str(path) + str(file_name) + ".json", "w")
    file_json.write(json.dumps(loads_json, indent=4, ensure_ascii=True))
    file_json.close()


def read_text(path, file_name):
    u"""Чтение текстового файла."""
    file_text = open(str(path) + str(file_name) + ".txt", "r")
    text = file_text.read()
    file_text.close()

    return text


def write_text(path, file_name, text_output):
    u"""Запись текстовой строки в текстовый файл."""
    file_text = open(str(path) + str(file_name) + ".txt", "w")
    file_text.write(text_output)
    file_text.close()
