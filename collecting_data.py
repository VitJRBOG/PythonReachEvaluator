# coding: utf8
u"""Модуль сбора данных через VK API."""


import datetime
import time
import vk_api
import data_manager
import output_data


def authorization(access_token):
    u"""Авторизация в ВК."""
    vk_session = vk_api.VkApi(token=access_token)
    vk_session._auth_token()

    return vk_session


def run_collecting_data(vk_session, str_target_date):
    u"""Сбор данных по охвату постов."""
    def select_public_url():
        u"""Извлекает из файла url паблика."""
        public_url = ""
        PATH = data_manager.read_path()
        data = data_manager.read_json(PATH + "res/", "data")
        public_url = data["public_url"]

        return public_url

    def select_public_domain(public_url):
        u"""Извлекает домайн из ссылки на сообщество ВК."""
        underline_for_find = "vk.com/"
        bgn_indx = public_url.find(underline_for_find)
        end_indx = bgn_indx + len(underline_for_find)
        public_domain = public_url[end_indx:]

        return public_domain

    def get_public_id(vk_session, public_domain):
        u"""Получает id сообщества ВК."""
        values = {
            "group_id": public_domain
        }
        response = vk_session.method("groups.getById", values)
        public_id = "-" + str(response[0]["id"])

        return public_id

    def select_posts_by_current_date(wall_posts, current_date):
        u"""Извлекает посты в пределах указанной пользователем даты."""
        ts_begin_date = ts_target_date - 60 * 10
        ts_end_date = ts_begin_date + 60 * 60 * 24
        target_posts = select_posts_by_target_date(wall_posts,
                                                   ts_begin_date, ts_end_date)
        return target_posts

    def insert_date_to_log(log_reach, ts_target_date):
        u"""Добавляет данные о дате в json-словарь."""
        tt_date = datetime.datetime.\
            timetuple(datetime.datetime.fromtimestamp(ts_target_date))
        date = {
            "day_number": tt_date[2],
            "month_number": tt_date[1],
            "day_week": tt_date[6] + 1,
            "year": tt_date[0]
        }
        log_reach.update(date)

        return log_reach
    
    def call_functions_for_collect(posts, type_posts):
        posts_data = select_publication_time(posts)
        log_reach = collect_reach(vk_session, posts_data)
        log_reach = insert_date_to_log(log_reach, ts_target_date)
        output_data.export_data_to_file(log_reach, type_posts)

    public_url = select_public_url()
    public_domain = select_public_domain(public_url)
    public_id = get_public_id(vk_session, public_domain)
    ts_target_date = str_date_to_timestamp(str_target_date, "%d-%m-%Y")
    wall_posts = get_wall_posts(vk_session, public_id, ts_target_date)
    target_posts = select_posts_by_current_date(wall_posts, ts_target_date)
    ads_posts, ordinary_posts = select_advertising_posts(target_posts)
    call_functions_for_collect(ads_posts, "ads")
    call_functions_for_collect(ordinary_posts, "posts")


def str_date_to_timestamp(str_time, date_format):
    u"""Преобразование строки времени в формат timestamp."""
    date_ts = time.mktime(time.strptime(str_time, date_format))
    return date_ts


def ts_date_to_str(ts_date, date_format):
    u"""Получение даты в читабельном формате."""
    str_date = datetime.datetime.fromtimestamp(ts_date).strftime(date_format)
    return str_date


def get_wall_posts(vk_session, public_id, ts_begin_date):
    u"""Собирает посты со стены в ВК."""
    def get_response(public_id, posts_count, offset):
        u"""Отправляет запрос к API VK."""
        values = {
            "owner_id": public_id,
            "count": posts_count,
            "offset": offset,
            "filter": "all"
        }
        response = vk_session.method("wall.get", values)

        return response

    def collection_posts(public_id, check_values, wall_posts):
        u"""Проверяет даты постов и добавляет их в общий список."""
        offset = check_values["offset"]
        posts_count = check_values["posts_count"]
        last_date = check_values["last_date"]

        response = get_response(public_id, posts_count, offset)

        if last_date < response["items"][posts_count - 1]["date"]:
            check_values["offset"] += check_values["posts_count"]
            return collection_posts(public_id, check_values, wall_posts)

        wall_posts.extend(response["items"])

        return wall_posts

    check_values = {
        "offset": 0,
        "posts_count": 100,
        "last_date": ts_begin_date
    }
    wall_posts = []
    wall_posts = collection_posts(public_id, check_values, wall_posts)

    return wall_posts


def select_advertising_posts(wall_posts):
    u"""Выбирает посты с меткой <<реклама>>."""
    ads_posts = []
    ordinary_posts = []
    for post in wall_posts:
        if "marked_as_ads" in post:
            if post["marked_as_ads"] == 1:
                ads_posts.append(post)
            else:
                ordinary_posts.append(post)
    return ads_posts, ordinary_posts


def select_publication_time(ads_posts):
    u"""Извлекает время публикации поста из json-словаря."""
    posts_data = []
    for post in ads_posts:
        ts_date = float(post["date"])
        publication_time = ts_date_to_str(ts_date, "%H:%M")
        post_data = {
            "publication_time": publication_time,
            "post": post
        }
        posts_data.append(post_data)
    return posts_data


def select_posts_by_target_date(posts, ts_begin_date, ts_end_date):
    u"""Извлекает посты в пределах целевой даты."""
    target_posts = []

    for post in posts:
        if post["date"] >= ts_begin_date and post["date"] < ts_end_date:
            target_posts.append(post)

    return target_posts


def collect_reach(vk_session, posts_data):
    u"""Сбор охвата постов."""
    def get_post_reach(vk_session, post):
        u"""Отправка запроса к VK API для получения данных об охвате."""
        values = {
            "owner_id": post["owner_id"],
            "post_id": post["id"]
        }
        response = vk_session.method("stats.getPostReach", values)
        return response[0]
    PATH = data_manager.read_path()
    template = data_manager.read_json(PATH + "res/", "template")

    for i in range(len(template["values"])):
        post_count = 0
        reach_total_value = 0
        for post_data in posts_data:
            publ_ts_time = str_date_to_timestamp(post_data["publication_time"],
                                                 "%H:%M")
            time_ts_begin = str_date_to_timestamp(template["values"][i]["time_begin"],
                                                  "%H:%M")
            time_ts_end = str_date_to_timestamp(template["values"][i]["time_end"],
                                                "%H:%M")
            time_ts_begin = time_ts_begin - 60 * 10
            time_ts_end = time_ts_end - 60 * 10
            if template["values"][i]["time_end"] == "00:00":
                time_ts_end += 60 * 60 * 24
            if publ_ts_time >= time_ts_begin and\
               publ_ts_time < time_ts_end:
                post_reach = get_post_reach(vk_session, post_data["post"])
                post_count += 1
                reach_total_value += post_reach["reach_total"]
        if post_count > 0:
            mid_value = reach_total_value / post_count
            mid_value = int(mid_value / 100) * 100
            template["values"][i]["value"] = mid_value
            template["values"][i]["post_count"] = post_count

    log_reach = template
    return log_reach
