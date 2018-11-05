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


def get_target_date():
    u"""Ввод пользователем целевой даты в консоль."""
    target_date = raw_input("USER [Target date]: (dd-mm-yyyy) ")
    return target_date


def get_posts_count():
    u"""Ввод пользователем количества запрашиваемых постов в консоль."""
    posts_count = raw_input("USER [Posts count]: ")
    return int(posts_count)
