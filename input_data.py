# coding: utf8
u"""Модуль ввода данных пользователем."""


def get_vk_user_token():
    u"""Ввод пользователем токена доступа в консоль."""
    access_token = raw_input("USER [Access token]: ")
    return access_token


def get_public_url():
    u"""Ввод пользователем ссылки на сообщество в консоль."""
    public_url = raw_input("USER [Public URL]: ")
    return public_url


def get_wiki_page_url(type_wiki_page):
    u"""Ввод пользователем ссылки на вики-страничку в консоль."""
    wiki_page_url = raw_input("USER [Wiki-page " + type_wiki_page + " URL]: ")
    return wiki_page_url


def get_number_time_intervals():
    u"""Ввод пользователем количества временных интервалов в консоль."""
    number_intervals = int(raw_input("USER [Number intervals]: (1-99) "))
    if number_intervals > 99:
        print("COMPUTER [Number intervals]: Too many intervals. Please, enter less... ")
        return get_number_time_intervals()
    return number_intervals


def get_time(type_time):
    u"""Ввод пользователем времени в консоль."""
    type_time = type_time[0].upper() + type_time[1:]
    time = raw_input("USER [" + type_time + " time]: (hh:mm) ")
    return time


def get_target_date():
    u"""Ввод пользователем целевой даты в консоль."""
    target_date = raw_input("USER [Target date]: (dd-mm-yyyy) ")
    return target_date


def get_posts_count():
    u"""Ввод пользователем количества запрашиваемых постов в консоль."""
    posts_count = raw_input("USER [Posts count]: ")
    return int(posts_count)
