# coding: utf8
u"""Модуль запуска программы."""


import initialization
import ui


def starter():
    u"""Запускает основные функции скрипта."""
    initialization.check_path()
    ui.main_menu()


starter()
