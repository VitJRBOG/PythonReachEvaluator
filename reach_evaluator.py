# coding: utf8


import os
import json
import copy
import re
import vk_api
import time
import datetime


class Day:
    day_number = 0
    month_number = 0
    day_week = "none"
    coverage = []

    def set_day_number(self, day_number):
        self.day_number = day_number

    def set_month_number(self, month_number):
        self.month_number = month_number

    def set_day_week(self, day_week):
        self.day_week = day_week

    def set_coverage(self, coverage):
        self.coverage = coverage

    def get_day_number(self):
        return self.day_number

    def get_month_number(self):
        return self.month_number

    def get_day_week(self):
        return self.day_week

    def get_coverage(self):
        return self.coverage

    def __init__(self):
        self.day_number = 0
        self.month_number = 0
        self.day_week = "none"
        self.coverage = []


class Template():
    begin_hours = []
    begin_minutes = []
    end_hours = []
    end_minutes = []
    time = []

    def join_time(self):

        try:
            if len(self.begin_hours) == len(self.begin_minutes) and\
               len(self.end_hours) == len(self.end_minutes) and\
               len(self.begin_hours) == len(self.end_hours) and\
               len(self.begin_minutes) == len(self.end_minutes):

                length_lists = len(self.begin_hours)

                i = 0
                while i < length_lists:

                    begin_hours_str = str(self.begin_hours[i])
                    if len(begin_hours_str) == 1:
                        begin_hours_str = "0" + begin_hours_str

                    begin_minutes_str = str(self.begin_minutes[i])
                    if len(begin_minutes_str) == 1:
                        begin_minutes_str = "0" + begin_minutes_str

                    end_hours_str = str(self.end_hours[i])
                    if len(end_hours_str) == 1:
                        end_hours_str = "0" + end_hours_str

                    end_minutes_str = str(self.end_minutes[i])
                    if len(end_minutes_str) == 1:
                        end_minutes_str = "0" + end_minutes_str

                    time_str = begin_hours_str + ":" + begin_minutes_str +\
                        "-" + end_hours_str + ":" + end_minutes_str

                    self.time.append(time_str)
                    i += 1

            else:
                print("COMPUTER [.. -> Join of time]: Error. " +
                      "Length of lists are different. " +
                      "Return to Main menu...")
                main_menu()

        except Exception as var_except:
            print("COMPUTER [.. -> Join of time]: Error, " +
                  str(var_except) + ". Return to Main menu...")

    def set_begin_hours(self, begin_hours):
        self.begin_hours = begin_hours

    def set_begin_minutes(self, begin_minutes):
        self.begin_minutes = begin_minutes

    def set_end_hours(self, end_hours):
        self.end_hours = end_hours

    def set_end_minutes(self, end_minutes):
        self.end_minutes = end_minutes

    def get_begin_hours(self):
        return self.begin_hours

    def get_begin_minutes(self):
        return self.begin_minutes

    def get_end_hours(self):
        return self.end_hours

    def get_end_minutes(self):
        return self.end_minutes

    def get_time(self):
        self.join_time()
        return self.time

    def __init__(self):
        self.begin_hours = []
        self.begin_minutes = []
        self.end_hours = []
        self.end_minutes = []


def starter():
    try:

        if os.path.exists("path.txt") is False:
            file_text = open("path.txt", "w")
            file_text.write("")
            file_text.close()
            print("COMPUTER: Was created file \"path.txt\".")

        path = read_path_txt()

        if os.path.exists(path + "output") is False:
            os.mkdir(str(path) + "output")
            print("COMPUTER: Was created directory \"output\".")

        if os.path.exists(path + "json") is False:
            os.mkdir(str(path) + "json")
            print("COMPUTER: Was created directory \"json\".")

    except Exception as var_except:
        print(
            "COMPUTER: Error, " + str(var_except) + ". Exit from program...")
        exit()
    main_menu()


def read_path_txt():
    try:
        path = str(open("path.txt", "r").read())

        if len(path) > 0 and path[len(path) - 1] != "/":
            path += "/"

        return path

    except Exception as var_except:
        print(
            "COMPUTER [.. -> Read \"path.txt\"]: Error, " + str(var_except) +
            ". Return to Main menu...")
        main_menu()


def read_json(sender, path, file_name):
    try:
        loads_json = json.loads(open(str(path) + str(file_name) +
                                     ".json", 'r').read())  # dict

        return loads_json
    except Exception as var_except:
        print(
            "COMPUTER [.. -> " + str(sender) +
            " -> Read JSON]: Error, " + str(var_except) +
            ". Return to Main menu...")
        main_menu()


def write_json(sender, path, file_name, loads_json):

    try:
        file_json = open(str(path) + str(file_name) + ".json", "w")
        file_json.write(json.dumps(loads_json, indent=4, ensure_ascii=False))
        file_json.close()

        print("COMPUTER [.. -> " + str(sender) + " -> Write JSON] " +
              "File \"" + file_name + ".json\" was successfully created. " +
              "Return to Main menu...")
        main_menu()

    except Exception as var_except:
        print(
            "COMPUTER [.. -> " + str(sender) +
            " -> Write JSON]: Error, " + str(var_except) +
            ". Return to Main menu...")
        main_menu()


def write_text(sender, path, file_name, text_output):

    try:
        file_text = open(str(path) + str(file_name) + ".txt", "w")
        file_text.write(text_output)
        file_text.close()

        print("COMPUTER [.. -> " + str(sender) + " -> Write output] " +
              "File \"" + file_name + ".txt\" was successfully created. " +
              "Return to Main menu...")
        main_menu()
    except Exception as var_except:
        print(
            "COMPUTER [.. -> " + str(sender) +
            " -> Write output]: Error, " + str(var_except) +
            ". Return to Main menu...")
        main_menu()


def main_menu():
    print("\nCOMPUTER [Main menu]: You are in Main menu.")
    print("COMPUTER [Main menu]: Enter digit for next action.")
    print("COMPUTER [Main menu]: 1 == Add new data about reach.")
    print("COMPUTER [Main menu]: 2 == Reach collector.")
    print("COMPUTER [Main menu]: 3 == Show data.")
    print("COMPUTER [Main menu]: 4 == Settings of intervals.")
    print("COMPUTER [Main menu]: 5 == Evaluate.")
    print("COMPUTER [Main menu]: 0 == Close the program.")

    user_answer = raw_input("USER [Main menu]: (1-5/0) ")

    user_answer = re.sub("[^0123456789\.]", "", user_answer)

    if user_answer == "0":
        close_program()
    elif user_answer == "1":
        add_menu()
    elif user_answer == "2":
        reach_collector()
    elif user_answer == "3":
        show_menu()
    elif user_answer == "4":
        settings_menu()
    elif user_answer == "5":
        evaluate_menu()
    else:
        print("COMPUTER [Main menu]: Unknown command. " +
              "Retry query...")
        main_menu()


def add_menu():

    PATH = read_path_txt()

    def enter_date(obj_day):
        print("COMPUTER [.. -> New data]: " +
              "Enter numbers of day and month, and name of day week.")

        def enter_day_number(obj_day):

            try:

                while True:
                    user_answer = raw_input("USER [.. -> New data -> " +
                                            "Day number]: (1-28/29/30/31/00) ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "00":
                        print("COMPUTER [.. -> " +
                              "New data -> Day number] Abort. " +
                              "Return to Main menu...")
                        main_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) > 0 and int(user_answer) < 32:
                            obj_day.set_day_number(int(user_answer))
                            return obj_day
                        else:
                            print("COMPUTER [.. -> New data -> Day number] " +
                                  "Error. Check entered data. Retry query...")

            except Exception as var_except:
                print(
                    "COMPUTER [.. -> New data -> Day number]: Error, " +
                    str(var_except) +
                    ". Return to Main menu...")
                main_menu()

        def enter_month_number(obj_day):

            try:

                while True:
                    user_answer = raw_input("USER [.. -> New data -> " +
                                            "Number of month]: (1-12/00) ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "00":
                            print("COMPUTER [.. -> New data -> " +
                                  "Number of month] " +
                                  "Abort. Return to Main menu...")
                            main_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) > 0 and int(user_answer) < 13:
                            obj_day.set_month_number(int(user_answer))
                            return obj_day
                        else:
                            print("COMPUTER [.. -> New data -> " +
                                  "Number of month] " +
                                  "Error. Check entered data. Retry query...")

                obj_day.set_month_number(int(user_answer))
            except Exception as var_except:
                print(
                    "COMPUTER [.. -> New data -> Number of month]: Error, " +
                    str(var_except) +
                    ". Return to Main menu...")
                main_menu()

        def enter_day_week(obj_day):
            try:

                while True:
                    user_answer = raw_input("USER [.. -> New data -> " +
                                            "Day week]: " +
                                            "1-7/00 ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "00":
                            print("COMPUTER [.. -> New data -> Day week] " +
                                  "Abort. Return to Main menu...")
                            main_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) > 0 and int(user_answer) < 8:
                            obj_day.set_day_week(int(user_answer))
                            return obj_day
                        else:
                            print("COMPUTER [.. -> New data -> " +
                                  "Day week] " +
                                  "Error. Check entered data. Retry query...")

                obj_day.set_day_week(int(user_answer))
            except Exception as var_except:
                print(
                    "COMPUTER [.. -> New data -> Day week]: Error, " +
                    str(var_except) +
                    ". Return to Main menu...")
                main_menu()

        obj_day = enter_day_number(obj_day)
        obj_day = enter_month_number(obj_day)
        obj_day = enter_day_week(obj_day)

        return obj_day

    def check_intervals(obj_day, loads_json):

        try:
            amount_intervals = len(loads_json)

            i = 0
            while i < amount_intervals:
                interval = loads_json[str(i)]
                loads_json[str(i)] = posts_amount(interval)
                i += 1

            obj_day.set_coverage(loads_json)
            return obj_day

        except Exception as var_except:
            print(
                "COMPUTER [.. -> New data -> Check intervals]: Error, " +
                str(var_except) +
                ". Return to Main menu...")
            main_menu()

    def posts_amount(interval):

        try:
            user_answer = raw_input("USER [.. -> Posts amount -> " +
                                    str(interval["time"]) +
                                    "]: (1-10/00) ")

            user_answer = re.sub("[^0123456789\.]", "", user_answer)

            if user_answer == "00":
                print("COMPUTER [.. -> New data -> Posts amount]: Abort. " +
                      "Return to Main menu...")
                main_menu()
            else:
                if user_answer != "" and\
                   int(user_answer) > 0 and int(user_answer) < 11:
                    post_amount = int(user_answer)
                    coverage = 0
                    i = 0
                    while i < post_amount:

                        exit_from_cicle = False

                        while True:
                            if i > 0:
                                user_answer = raw_input("USER [.. -> " +
                                                        str(interval["time"]) +
                                                        " -> Post coverage №" +
                                                        str(i + 1) +
                                                        "]: (****/0) ")
                            if i <= 0:
                                user_answer = raw_input("USER [.. -> " +
                                                        str(interval["time"]) +
                                                        " -> Post coverage №" +
                                                        str(i + 1) +
                                                        "]: (****) ")

                            user_answer = re.sub("[^0123456789\.]", "",
                                                 user_answer)

                            if user_answer == "0" and i > 0:
                                exit_from_cicle = True
                                break

                            if user_answer != "" and int(user_answer) > 999:
                                coverage = coverage +\
                                    enter_coverage(interval["time"], i + 1,
                                                   user_answer)
                                i += 1
                                break
                            else:
                                print("COMPUTER [.. -> Post coverage]: " +
                                      "Error, check entered data. " +
                                      " Retry query...")

                        if exit_from_cicle:
                            break

                    coverage = int(coverage) / int(i)

                    coverage = float(coverage / 100)

                    coverage = round(coverage)

                    coverage = coverage * 100

                    interval["value"] = int(coverage)
                    return interval
                else:
                    print("COMPUTER [.. -> New data -> Posts amount]: " +
                          "Error, check entered data. Retry query...")
                    return posts_amount(interval)

        except Exception as var_except:
            print(
                "COMPUTER [.. -> New data -> Posts amount]: Error, " +
                str(var_except) +
                ". Return to Main menu...")
            main_menu()

    def enter_coverage(interval_time, post_number, user_answer):

        try:

            answer = float(float(user_answer) / 100)

            answer = round(answer)

            answer = answer * 100

            return int(answer)

        except Exception as var_except:
            print(
                "COMPUTER [.. -> Post coverage]: Error, " +
                str(var_except) +
                ". Return to Main menu...")
            main_menu()

    def make_json_log(obj_day):
        try:

            file_name = "log_" + str(obj_day.get_day_number())

            month = [
                "jan", "feb", "mar",
                "apr", "may", "jun",
                "jul", "aug", "sep",
                "oct", "nov", "dec"
            ]

            file_name = file_name + "-" +\
                str(month[int(obj_day.get_month_number()) - 1])

            day_week = [
                "mon", "tue", "wed",
                "thu", "fri", "sat",
                "sun"
            ]

            file_name = file_name + "-" +\
                str(day_week[int(obj_day.get_day_week()) - 1])

            loads_json = {
                "day_number": int(obj_day.get_day_number()),
                "month_number": int(obj_day.get_month_number()),
                "day_week": int(obj_day.get_day_week()),
                "coverage": obj_day.get_coverage()
            }

            write_json("Make JSON", PATH + "json/", file_name, loads_json)

        except Exception as var_except:
            print(
                "COMPUTER [.. -> New data -> Make JSON]: Error, " +
                str(var_except) +
                ". Return to Main menu...")
            main_menu()

    print("\nCOMPUTER [.. -> New data]: You are in menu of add new data.")

    if os.path.exists(PATH + "template.json") is False:
        print("COMPUTER [.. -> New data]: " +
              "File \"template.json\" is not exist. Check " +
              "menu Settings.")
        print("COMPUTER [.. -> New data]: Return to Main menu...")
        main_menu()
    else:
        obj_day = Day()
        loads_json = read_json("New data", PATH + "", "template")
        obj_day = enter_date(obj_day)
        obj_day = check_intervals(obj_day, loads_json)
        make_json_log(obj_day)

        print("COMPUTER [.. - New data] Something wrong. " +
              "Return to Main menu...")
        main_menu()


def reach_collector():
    def authorize(sender, access_token):
        sender += " -> Authorize"

        vk_session = vk_api.VkApi(token=access_token)
        vk_session._auth_token()

        return vk_session

    def get_posts(sender, vk_session, owner_id):
        sender += " -> Get posts"

        values = {
            "owner_id": owner_id,
            "count": 100,
            "filter": "post"
        }

        response = vk_session.method("wall.get", values)

        return response["items"]

    def selection_post(sender, str_date, posts):
        sender += " -> Selection post"

        UNIX_MINUTE = 60

        if str_date.find("-") != -1:
            date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date, '%d-%m-%Y')))
        elif str_date.find(".") != -1:
            date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date, '%d.%m.%Y')))
        else:
            print("COMPUTER [" + sender + "]: Error. Check entered date.")

        unix_date = int(time.mktime(date.timetuple()))

        begin_of_day = unix_date - UNIX_MINUTE * 10
        end_of_day = begin_of_day + UNIX_MINUTE * 60 * 24

        posts_per_day = []

        # i = len(posts) - 1
        i = 0

        while i < len(posts):
            if posts[i]["date"] >= begin_of_day and\
              posts[i]["date"] < end_of_day:
                posts_per_day.append(copy.deepcopy(posts[i]))

            i += 1

        return posts_per_day

    def get_reach(sender, vk_session, owner_id, post_id):
        sender += " -> Get reach"

        values = {
            "owner_id": owner_id,
            "post_id": post_id
        }

        response = vk_session.method("stats.getPostReach", values)

        return response[0]

    def sort_by_time(sender, posts_reach, template, str_date):
        sender += " -> Sort by time"

        log = copy.deepcopy(template)

        UNIX_MINUTE = 60

        i = 0

        while i < len(log):

            str_time_begin = log[str(i)]["time"][:5]
            str_date_begin = str_date + " " + str_time_begin
            if str_date.find("-") != -1:
                date_begin = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date_begin, '%d-%m-%Y %H:%M')))
            elif str_date.find(".") != -1:
                date_begin = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date_begin, '%d.%m.%Y %H:%M')))
            else:
                print("COMPUTER [" + sender + "]: Error. Check entered date.")
            unix_date_begin = int(time.mktime(date_begin.timetuple()))

            str_time_end = log[str(i)]["time"][6:]
            str_date_end = str_date + " " + str_time_end
            if str_date.find("-") != -1:
                date_end = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date_end, '%d-%m-%Y %H:%M')))
            elif str_date.find(".") != -1:
                date_end = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date_end, '%d.%m.%Y %H:%M')))
            else:
                print("COMPUTER [" + sender + "]: Error. Check entered date.")
            unix_date_end = int(time.mktime(date_end.timetuple()))

            begin_of_interval = unix_date_begin - UNIX_MINUTE * 10
            end_of_interval = unix_date_end - UNIX_MINUTE * 10

            if str_time_end == "00:00":
                end_of_interval += UNIX_MINUTE * 60 * 24

            count = 0
            reach = 0

            j = 0

            while j < len(posts_reach):

                if posts_reach[j]["date"] >= begin_of_interval and\
                   posts_reach[j]["date"] < end_of_interval:

                    count += 1

                    reach += posts_reach[j]["reach"]

                j += 1

            if count > 1:
                reach = reach / count

            reach = int(round(float(reach) / 100)) * 100

            log[str(i)]["value"] = reach

            i += 1

        return log

    def create_log(sender, str_date, log):
        if str_date.find("-") != -1:
            date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date, '%d-%m-%Y')))
        elif str_date.find(".") != -1:
            date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date, '%d.%m.%Y')))
        else:
            print("COMPUTER [" + sender + "]: Error. Check entered date.")

        weekday = date.isoweekday()
        day = int(datetime.datetime.strftime(date, '%d'))
        month = int(datetime.datetime.strftime(date, '%m'))

        loads_json = {
            "day_number": day,
            "month_number": month,
            "day_week": weekday,
            "coverage": log
        }

        return loads_json

    def set_filename(sender, str_date):
        sender += " -> Set file name"

        if str_date.find("-") != -1:
            date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date, '%d-%m-%Y')))
        elif str_date.find(".") != -1:
            date = datetime.datetime.fromtimestamp(time.mktime(time.strptime(str_date, '%d.%m.%Y')))
        else:
            print("COMPUTER [" + sender + "]: Error. Check entered date.")

        name_weekday = [
            "mon", "tue", "wed",
            "thu", "fri", "sat",
            "sun"
        ]

        name_month = [
            "jan", "feb", "mar",
            "apr", "may", "jun",
            "jul", "aug", "sep",
            "oct", "nov", "dec"
        ]

        weekday = date.isoweekday()
        day = int(datetime.datetime.strftime(date, '%d'))
        month = int(datetime.datetime.strftime(date, '%m'))

        file_name = "log_" + str(day) + "-" +\
                    name_month[month - 1] + "-" +\
                    name_weekday[weekday - 1]

        return file_name

    sender = "Main"

    PATH = read_path_txt()

    access_token = raw_input("USER [" + sender + " -> New token]: ")

    vk_session = authorize(sender, access_token)

    owner_id = raw_input("USER [" + sender + " -> Public id]: ")

    if owner_id[0] != "-":
        owner_id = "-" + owner_id

    posts = get_posts(sender, vk_session, owner_id)

    str_date = raw_input("USER [" + sender + " -> Date]: ")

    posts_per_day = selection_post(sender, str_date, posts)

    posts_reach = []

    i = len(posts_per_day) - 1

    while i >= 0:
        owner_id = posts_per_day[i]["owner_id"]
        post_id = posts_per_day[i]["id"]

        reach = copy.deepcopy(get_reach(sender, vk_session, owner_id, post_id))
        date = posts_per_day[i]["date"]

        post = {
            "reach": reach["reach_subscribers"],
            "date": date
        }

        posts_reach.append(copy.deepcopy(post))

        print(str(i) + "/" + str(len(posts_per_day) - 1))

        i -= 1

    template = read_json(sender, PATH, "template")

    log = copy.deepcopy(sort_by_time(sender, posts_reach, template, str_date))

    file_name = set_filename(sender, str_date)

    loads_json = create_log(sender, str_date, log)

    write_json(sender, PATH + "json/", file_name, loads_json)

    main_menu()


def show_menu():

    PATH = read_path_txt()

    def export_query(sender, file_name, text_output):

        try:
            print("\nCOMPUTER [.. -> " + str(sender) +
                  " -> Make output -> Export]: Export log to text file?")
            user_answer = raw_input("USER [.. -> " + str(sender) +
                                    " -> Make output -> Export]: (1/0) ")

            user_answer = re.sub("[^0123456789\.]", "", user_answer)

            if user_answer == "0":
                show_menu()
            else:
                if user_answer == "1":

                    write_text("All logs", PATH +
                               "output/", file_name, text_output)
                else:
                    print("COMPUTER [.. -> " + str(sender) +
                          " -> Make output -> Export]: " +
                          "Error, check entered data. Retry query...")
                    export_query(sender, file_name, text_output)

        except Exception as var_except:
            print("COMPUTER [.. -> " + str(sender) +
                  " -> Make output -> Export]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()

    def show_files(sender, list_files):

        def make_output(sender, file_name):
            try:
                pos = file_name.find(".json")
                file_name = file_name[0:pos]

                loads_json = read_json(sender, PATH + "json/", file_name)

                month = [
                    "января", "февраля", "марта",
                    "апреля", "мая", "июня",
                    "июля", "августа", "сентября",
                    "октября", "ноября", "декабря"
                ]

                day_week = [
                    "понедельник", "вторник", "среда",
                    "четверг", "пятница", "суббота",
                    "воскресенье"
                ]

                text_output = "[" + str(loads_json["day_number"])
                text_output += " " +\
                    str(month[int(loads_json["month_number"]) - 1])
                text_output += " - " +\
                    str(day_week[int(loads_json["day_week"]) - 1]) + "]"

                coverage = loads_json["coverage"]

                i = len(coverage) - 1
                while i >= 0:
                    text_output += "\n" + str(coverage[str(i)]["time"])
                    text_output += " (" + str(coverage[str(i)]["value"]) + ")"
                    i -= 1

                print("\n" + text_output)

                export_query(sender, file_name, text_output)

            except Exception as var_except:
                print("COMPUTER [.. -> " + str(sender) +
                      " -> Make output]: Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        def print_to_console(sender, list_files):
            try:

                user_answer = ""
                count = 0

                if sender == "All logs":
                    print("\n")

                    if len(list_files) < 1:
                        print("COMPUTER [.. -> Show files -> " +
                              str(sender) + "]: Folder \"json\" is empty. " +
                              "Return to Show menu.")
                        show_menu()

                    i = 0
                    while i < len(list_files):
                        print("[" + str(i + 1) + "] " + str(list_files[i]))
                        count += 1
                        i += 1

                if sender == "By days week logs":

                    day_week_ru = [
                        "понедельник", "вторник", "среда",
                        "четверг", "пятница", "суббота",
                        "воскресенье"
                    ]

                    print("\n")

                    if len(list_files) < 1:
                        print("COMPUTER [.. -> Show files -> " +
                              str(sender) + "]: Folder \"json\" is empty. " +
                              "Return to Show menu.")
                        show_menu()

                    i = 0
                    while i < len(day_week_ru):
                        print("[" + str(i + 1) + "] " + str(day_week_ru[i]))
                        i += 1

                    print("\nCOMPUTER [.. -> Show files -> " +
                          str(sender) + "]: " +
                          "Select day of the week, or exit to Show menu.")
                    user_answer = raw_input("USER [.. -> " + str(sender) +
                                            "] " +
                                            "(1-" + str(len(day_week_ru)) +
                                            "/0) ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "0":
                        show_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) > 0 \
                           and int(user_answer) <= len(day_week_ru):

                            day_week = [
                                "mon", "tue", "wed",
                                "thu", "fri", "sat",
                                "sun"
                            ]

                            print("\n")
                            i = 0

                            while i < len(list_files):
                                pos = list_files[i].find(
                                    day_week[int(user_answer) - 1])
                                if pos != -1:
                                    print("[" +
                                          str(i + 1) + "] " +
                                          str(list_files[i]))
                                    count += 1
                                i += 1
                            if count < 1:
                                print("COMPUTER [.. -> Show files -> " +
                                      str(sender) +
                                      "]: Logs for " +
                                      str(day_week_ru[int(user_answer) - 1]) +
                                      " are absent. " +
                                      "Return to Show menu.")
                                show_menu()
                        else:
                            print("COMPUTER [.. -> Show files -> " +
                                  str(sender) +
                                  "]: " +
                                  "Error, check entered data. Retry query...")
                            print_to_console(sender, list_files)

                if sender == "By months logs":

                    month_ru = [
                        "январь", "февраль", "март",
                        "апрель", "май", "июнь",
                        "июль", "август", "сентябрь",
                        "октябрь", "ноябрь", "декабрь"
                    ]

                    print("\n")

                    if len(list_files) < 1:
                        print("COMPUTER [.. -> Show files -> " +
                              str(sender) + "]: Folder \"json\" is empty. " +
                              "Return to Show menu.")
                        show_menu()

                    i = 0
                    while i < len(month_ru):
                        print("[" + str(i + 1) + "] " + str(month_ru[i]))
                        i += 1

                    print("\nCOMPUTER [.. -> Show files -> " +
                          str(sender) + "]: " +
                          "Select month, or exit to Show menu.")
                    user_answer = raw_input("USER [.. -> " + str(sender) +
                                            "] " +
                                            "(1-" + str(len(month_ru)) +
                                            "/0) ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "0":
                        show_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) > 0 \
                           and int(user_answer) <= len(month_ru):

                            month = [
                                "jan", "feb", "mar",
                                "apr", "may", "jun",
                                "jul", "aug", "sep",
                                "oct", "nov", "dec"
                            ]

                            print("\n")
                            i = 0

                            while i < len(list_files):
                                pos = list_files[i].find(
                                    month[int(user_answer) - 1])
                                if pos != -1:
                                    print("[" +
                                          str(i + 1) + "] " +
                                          str(list_files[i]))
                                    count += 1
                                i += 1
                            if count < 1:
                                print("COMPUTER [.. -> Show files -> " +
                                      str(sender) +
                                      "]: Logs for " +
                                      str(month_ru[int(user_answer) - 1]) +
                                      " are absent. " +
                                      "Return to Show menu.")
                                show_menu()
                        else:
                            print("COMPUTER [.. -> Show files -> " +
                                  str(sender) +
                                  "]: " +
                                  "Error, check entered data. Retry query...")
                            print_to_console(sender, list_files)

                print("\nCOMPUTER [.. -> Show files -> " +
                      str(sender) + "]: " +
                      "Select file, or exit to Show menu.")
                user_answer = raw_input("USER [.. -> " +
                                        str(sender) +
                                        "] (1-" +
                                        str(len(list_files)) +
                                        "/0) ")

                user_answer = re.sub("[^0123456789\.]", "", user_answer)

                if user_answer == "0":
                    show_menu()
                else:
                    if user_answer != "" and\
                       int(user_answer) > 0 \
                       and int(user_answer) <= len(list_files):
                        make_output(sender, list_files[int(user_answer) - 1])
                    else:
                        print("COMPUTER [.. -> Show files -> " +
                              str(sender) + "]: " +
                              "Error, check entered data. Retry query...")
                        show_files(sender, list_files)

            except Exception as var_except:
                print("COMPUTER [.. -> Show files -> " + str(sender) + "]: " +
                      "Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        print_to_console(sender, list_files)

    def make_list():

        def sort_files(list_files):
            try:

                def sort_by_month(list_files):

                    try:

                        month = [
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

                        i = 0

                        while i < len(month):

                            j = 0
                            while j < len(list_files):
                                file_name = str(list_files[j])

                                pos = file_name.lower().find(month[i])
                                if pos != -1:
                                    dict_by_month[month[i]].append(file_name)
                                j += 1
                            i += 1
                        return dict_by_month

                    except Exception as var_except:
                        print("COMPUTER [.. -> Sort files -> " +
                              "Sort by month]: " +
                              "Error, " +
                              str(var_except) +
                              ". Return to Main menu...")
                        main_menu()

                def sort_by_daynumber(dict_by_month):
                    try:
                        i = 0

                        month = [
                            "jan", "feb", "mar",
                            "apr", "may", "jun",
                            "jul", "aug", "sep",
                            "oct", "nov", "dec"
                        ]

                        while i < len(month):
                            j = 0
                            while j < len(dict_by_month[month[i]]):
                                list_by_month = dict_by_month[month[i]]
                                new_list = []

                                n = 31
                                while n > 0:

                                    m = 0
                                    while m < len(list_by_month):
                                        file_name = list_by_month[m]

                                        pos = file_name.find(str(n))

                                        if pos != -1:
                                            new_list.insert(0, file_name)
                                            list_by_month[m] = ""
                                        m += 1
                                    n -= 1
                                dict_by_month[month[i]] = new_list
                                j += 1
                            i += 1
                        return dict_by_month

                    except Exception as var_except:
                        print("COMPUTER [.. -> Sort files -> " +
                              "Sort by day number]: " +
                              "Error, " +
                              str(var_except) +
                              ". Return to Main menu...")
                        main_menu()

                dict_by_month = sort_by_month(list_files)
                dict_by_month = sort_by_daynumber(dict_by_month)
                return dict_by_month

            except Exception as var_except:
                print("COMPUTER [.. -> Show data -> Sort files]: Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        list_files = os.listdir(PATH + "json/")

        dict_by_month = sort_files(list_files)

        month = [
            "jan", "feb", "mar",
            "apr", "may", "jun",
            "jul", "aug", "sep",
            "oct", "nov", "dec"
        ]

        list_files = []

        i = 0
        while i < len(month):
            j = 0
            while j < len(dict_by_month[month[i]]):
                list_files.append(dict_by_month[month[i]][j])
                j += 1
            i += 1
        return list_files

    def list_all():
        try:
            list_files = make_list()
            show_files("All logs", list_files)
        except Exception as var_except:
            print("COMPUTER [.. -> Show data -> All logs]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()

        show_menu()

    def list_days_week():
        try:
            list_files = make_list()
            show_files("By days week logs", list_files)
        except Exception as var_except:
            print("COMPUTER [.. -> Show data -> Day week logs]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()

        show_menu()

    def list_months():
        try:
            list_files = make_list()
            show_files("By months logs", list_files)
        except Exception as var_except:
            print("COMPUTER [.. -> Show data -> By months logs]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()

        show_menu()

    print("\nCOMPUTER [.. -> Show data]: You are in Show menu.")
    print("COMPUTER [.. -> Show data]: Enter digit for next action. (1-3/0)")
    print("COMPUTER [.. -> Show data]: 1 == Show list all logs.")
    print("COMPUTER [.. -> Show data]: 2 == Show lists by days of the week.")
    print("COMPUTER [.. -> Show data]: 3 == Show lists by months.")
    print("COMPUTER [.. -> Show data]: 0 == Step back.")

    user_answer = raw_input("USER [.. -> Show data]: (1-3/0) ")

    user_answer = re.sub("[^0123456789\.]", "", user_answer)

    if user_answer == "0":
        main_menu()
    else:
        if user_answer == "1":
            list_all()
        else:
            if user_answer == "2":
                list_days_week()
            else:
                if user_answer == "3":
                    list_months()
                else:
                    print("COMPUTER [.. -> Show data]: Unknown command. " +
                          "Retry query...")
                    show_menu()


def settings_menu():

    PATH = read_path_txt()

    def create_template(count_intervals):

        def input_begin_hour(i, obj_template):

            try:

                while True:

                    user_answer = raw_input("USER [.. -> Create template -> " +
                                            "Interval №" + str(i + 1) +
                                            " -> Begin time " +
                                            "-> Hours]: (0-23/00) ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "00":
                        print("COMPUTER [.. -> Begin time -> Hours]: " +
                              "Abort. Return to menu Settings...")
                        settings_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) >= 0 and int(user_answer) < 24:

                            begin_hours = obj_template.get_begin_hours()
                            begin_hours.append(int(user_answer))
                            obj_template.set_begin_hours(begin_hours)

                            return obj_template
                        else:
                            print("COMPUTER [.. -> Begin time -> Hours]: " +
                                  "Error, check entered data. Retry query...")

            except Exception as var_except:
                print("COMPUTER [.. -> Begin time -> Hours]: Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        def input_begin_minutes(i, obj_template):

            try:

                while True:

                    user_answer = raw_input("USER [.. -> Create template -> " +
                                            "Interval №" + str(i + 1) +
                                            " -> Begin time " +
                                            "-> Minutes]: (0-59/00) ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "00":
                        print("COMPUTER [.. -> Begin time -> Minutes]: " +
                              "Abort. Return to menu Settings...")
                        settings_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) >= 0 and int(user_answer) < 60:

                            begin_minutes = obj_template.get_begin_minutes()
                            begin_minutes.append(int(user_answer))
                            obj_template.set_begin_minutes(begin_minutes)

                            return obj_template
                        else:
                            print("COMPUTER [.. -> Begin time -> Minutes]: " +
                                  "Error, check entered data. Retry query...")

            except Exception as var_except:
                print("COMPUTER [.. -> Begin time -> Minutes]: Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        def input_end_hour(i, obj_template):

            try:

                while True:

                    user_answer = raw_input("USER [.. -> Create template -> " +
                                            "Interval №" + str(i + 1) +
                                            " -> End time " +
                                            "-> Hours]: (0-59/00) ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "00":
                        print("COMPUTER [.. -> End time -> Hours]: " +
                              "Abort. Return to menu Settings...")
                        settings_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) >= 0 and int(user_answer) < 60:

                            end_hours = obj_template.get_end_hours()
                            end_hours.append(int(user_answer))
                            obj_template.set_end_hours(end_hours)

                            return obj_template
                        else:
                            print("COMPUTER [.. -> End time -> Hours]: " +
                                  "Error, check entered data. Retry query...")

            except Exception as var_except:
                print("COMPUTER [.. -> End time -> Hours]: Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        def input_end_minutes(i, obj_template):

            try:

                while True:

                    user_answer = raw_input("USER [.. -> Create template -> " +
                                            "Interval №" + str(i + 1) +
                                            " -> End time " +
                                            "-> Minutes]: (0-59/00) ")

                    user_answer = re.sub("[^0123456789\.]", "", user_answer)

                    if user_answer == "00":
                        print("COMPUTER [.. -> End time -> Minutes]: " +
                              "Abort. Return to menu Settings...")
                        settings_menu()
                    else:
                        if user_answer != "" and\
                           int(user_answer) >= 0 and int(user_answer) < 60:

                            end_minutes = obj_template.get_end_minutes()
                            end_minutes.append(int(user_answer))
                            obj_template.set_end_minutes(end_minutes)

                            return obj_template
                        else:
                            print("COMPUTER [.. -> End time -> Minutes]: " +
                                  "Error, check entered data. Retry query...")

            except Exception as var_except:
                print("COMPUTER [.. -> End time -> Minutes]: Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        obj_template = Template()

        i = 0
        while i < count_intervals:
            obj_template = input_begin_hour(i, obj_template)
            obj_template = input_begin_minutes(i, obj_template)
            obj_template = input_end_hour(i, obj_template)
            obj_template = input_end_minutes(i, obj_template)
            i += 1

        time = obj_template.get_time()

        loads_json = {}

        i = 0
        while i < len(time):
            time_dict = {
                "time": time[i],
                "value": 0
            }
            loads_json = {
                str(i): time_dict
            }
            i += 1

        write_json("Settings", PATH + "", "template", loads_json)

    def new_template():

        try:

            print("COMPUTER [.. -> New template]: " +
                  "Enter count of new intervals.")

            user_answer = raw_input("USER [.. -> New template -> " +
                                    "Count of intervals]: (1-24/00) ")

            user_answer = re.sub("[^0123456789\.]", "", user_answer)

            if user_answer == "00":
                print("COMPUTER [.. -> New template -> Count of intervals]: " +
                      "Abort. Return to menu Settings...")
                settings_menu()
            else:
                if user_answer != "" and\
                   int(user_answer) > 0 and int(user_answer) < 25:
                    create_template(int(user_answer))
                else:
                    print("COMPUTER [.. -> New template -> " +
                          "Count of intervals]: " +
                          "Error, check entered data. Retry query...")
                    new_template()

        except Exception as var_except:
            print("COMPUTER [.. -> New template]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()

    def show_template():

        def export_template_query(text_output):

            try:
                print("\nCOMPUTER [.. -> Show template -> Export]: " +
                      "Export template to text file?")
                user_answer = raw_input("USER [.. -> Show template -> " +
                                        "Export]: (1/0) ")

                user_answer = re.sub("[^0123456789\.]", "", user_answer)

                if user_answer == "0":
                    settings_menu()
                else:
                    if user_answer == "1":

                        write_text("Show template -> Export", PATH +
                                   "output/", "template", text_output)
                    else:
                        print("COMPUTER [.. -> Show template -> Export]: " +
                              "Error, check entered data. Retry query...")
                        export_template_query(text_output)

            except Exception as var_except:
                print("COMPUTER [.. -> Show template -> Export]: Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        def export_template():
            try:

                loads_json = read_json("Show template", PATH +
                                       "", "template")

                text_output = "[day month - dayweek]"

                i = len(loads_json) - 1
                while i >= 0:
                    text_output += "\n" + str(loads_json[str(i)]["time"])
                    text_output += " (" + str(loads_json[str(i)]["value"]) +\
                        ")"
                    i -= 1

                print("\n" + text_output)

                export_template_query(text_output)

            except Exception as var_except:
                print("COMPUTER [.. -> Show template]: Error, " +
                      str(var_except) +
                      ". Return to Main menu...")
                main_menu()

        export_template()

    print("\nCOMPUTER [.. -> Settings]: You are in menu Settings.")
    print("COMPUTER [.. -> Settings]: Enter digit for next action.")
    print("COMPUTER [.. -> Settings]: 1 == Create new template.")
    print("COMPUTER [.. -> Settings]: 2 == Show exist template.")
    print("COMPUTER [.. -> Settings]: 0 == Step back.")

    user_answer = raw_input("USER [Main menu]: (1-2/0) ")

    user_answer = re.sub("[^0123456789\.]", "", user_answer)

    if user_answer == "0":
        main_menu()
    else:
        if user_answer == "1":
            new_template()
        else:
            if user_answer == "2":
                show_template()
            else:
                print("COMPUTER [.. -> Settings]: Unknown command. " +
                      "Retry query...")
                settings_menu()


def evaluate_menu():

    PATH = read_path_txt()

    def collect_files(sender):
        try:

            list_files = os.listdir(PATH + "json/")

            list_logs = []

            i = 0
            while i < len(list_files):

                pos = list_files[i].find(".json")

                loads_json = read_json("Evaluate", PATH + "json/",
                                       list_files[i][0:pos])

                obj_day = Day()

                obj_day.set_day_number(loads_json["day_number"])
                obj_day.set_month_number(loads_json["month_number"])
                obj_day.set_day_week(loads_json["day_week"])
                obj_day.set_coverage(loads_json["coverage"])

                list_logs.append(obj_day)

                i += 1

            sum_coverage(sender, list_logs)

        except Exception as var_except:
            print("COMPUTER [.. -> " + str(sender) +
                  " -> Collect files]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()
        evaluate_menu()

    def sum_coverage(sender, list_logs):
        try:
            list_result_sum = []

            if sender == "For each days":
                day_week = [
                    "mon", "tue", "wed",
                    "thu", "fri", "sat",
                    "sun"
                ]

                log_template = read_json("Calculate coverage", PATH +
                                         "", "template")

                list_result_sum = {
                    "mon": copy.deepcopy(log_template),
                    "tue": copy.deepcopy(log_template),
                    "wed": copy.deepcopy(log_template),
                    "thu": copy.deepcopy(log_template),
                    "fri": copy.deepcopy(log_template),
                    "sat": copy.deepcopy(log_template),
                    "sun": copy.deepcopy(log_template)
                }

                i = 0
                while i < len(day_week):
                    count = 0
                    j = 0
                    while j < len(list_logs):
                        if list_logs[j].get_day_week() == i + 1:
                            if len(list_logs[j].get_coverage()) ==\
                               len(list_result_sum[day_week[i]]):
                                coverage = list_logs[j].get_coverage()
                                count += 1
                                n = 0
                                while n < len(list_result_sum[day_week[i]]):
                                    dw = day_week[i]  # because many symbols
                                    sn = str(n)  # because many symbols next ln
                                    list_result_sum[dw][sn]["value"] +=\
                                        coverage[sn]["value"]
                                    coverage[sn]["value"] = 0
                                    n += 1
                            else:
                                print("COMPUTER [.. -> Evaluate -> " +
                                      str(sender) + "]: " +
                                      "Error, different lengths of " +
                                      "template of list and log. " +
                                      "Return to Main menu...")
                                main_menu()
                        j += 1
                    m = 0
                    while m < len(list_result_sum[day_week[i]]):
                        dw = day_week[i]  # because many symbols
                        sm = str(m)  # because many symbols in next line
                        coverage = list_result_sum[dw][sm]["value"]
                        coverage = int(coverage) / int(count)
                        coverage = float(coverage / 100)
                        coverage = round(coverage)
                        coverage = coverage * 100
                        list_result_sum[dw][sm]["value"] = int(coverage)
                        m += 1
                    i += 1

            if sender == "Total":
                log_template = read_json("Calculate coverage", PATH +
                                         "", "template")

                list_result_sum = copy.deepcopy(log_template)

                count = 0
                i = 0
                while i < len(list_logs):
                    if len(list_logs[i].get_coverage()) ==\
                       len(list_result_sum):
                        coverage = list_logs[i].get_coverage()
                        count += 1
                        n = 0
                        while n < len(list_result_sum):
                            sn = str(n)  # because many symbols next ln
                            list_result_sum[sn]["value"] +=\
                                coverage[sn]["value"]
                            coverage[sn]["value"] = 0
                            n += 1
                    else:
                        print("COMPUTER [.. -> Evaluate -> " +
                              str(sender) + "]: " +
                              "Error, different lengths of " +
                              "template of list and log. " +
                              "Return to Main menu...")
                        main_menu()
                    i += 1
                m = 0
                while m < len(list_result_sum):
                    sm = str(m)  # because many symbols in next line
                    coverage = list_result_sum[sm]["value"]
                    coverage = int(coverage) / int(count)
                    coverage = float(coverage / 100)
                    coverage = round(coverage)
                    coverage = coverage * 100
                    list_result_sum[sm]["value"] = int(coverage)
                    m += 1
                i += 1

            evaluate_coverage(sender, list_result_sum)
        except Exception as var_except:
            print("COMPUTER [.. -> Evaluate -> " +
                  str(sender) + " -> Sum coverage]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()
        evaluate_menu()

    def algorithm_evaluate(sender, status, coverage):
        try:
            n = 0
            while n < len(status):
                sn = str(n)  # because many symbols
                value = 100
                m = 0
                while m < len(coverage):
                    sm = str(m)  # because many symbols
                    if value < coverage[sm]["value"]:
                        value = coverage[sm]["value"]
                    m += 1
                status[sn]["value"] = value
                m = 0
                while m < len(coverage):
                    sm = str(m)  # because many symbols
                    if value == coverage[sm]["value"]:
                        status[sn]["time"].append(coverage[sm]["time"])
                        coverage[sm]["value"] = 0
                    m += 1
                n += 1
            return status
        except Exception as var_except:
            print("COMPUTER [.. -> Evaluate -> " +
                  str(sender) + " -> Evaluate coverage -> " +
                  "Coverage algorithm]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()

    def evaluate_coverage(sender, list_result_sum):
        try:

            evaluate_status = [
                "best", "good", "norm"
            ]

            list_evaluate = {
                "best": {
                    "0": {
                        "time": [],
                        "value": 0
                    },
                    "1": {
                        "time": [],
                        "value": 0
                    },
                    "2": {
                        "time": [],
                        "value": 0
                    }
                },
                "good": {
                    "0": {
                        "time": [],
                        "value": 0
                    },
                    "1": {
                        "time": [],
                        "value": 0
                    },
                    "2": {
                        "time": [],
                        "value": 0
                    }
                },
                "norm": {
                    "0": {
                        "time": [],
                        "value": 0
                    },
                    "1": {
                        "time": [],
                        "value": 0
                    },
                    "2": {
                        "time": [],
                        "value": 0
                    }
                }
            }

            if sender == "For each days":

                day_week = [
                    "mon", "tue", "wed",
                    "thu", "fri", "sat",
                    "sun"
                ]

                list_result_evaluate = {
                    "mon": copy.deepcopy(list_evaluate),
                    "tue": copy.deepcopy(list_evaluate),
                    "wed": copy.deepcopy(list_evaluate),
                    "thu": copy.deepcopy(list_evaluate),
                    "fri": copy.deepcopy(list_evaluate),
                    "sat": copy.deepcopy(list_evaluate),
                    "sun": copy.deepcopy(list_evaluate)
                }

                i = 0
                while i < len(day_week):
                    dw = day_week[i]
                    coverage = copy.deepcopy(list_result_sum[day_week[i]])
                    j = 0
                    while j < len(evaluate_status):
                        es = evaluate_status[j]
                        status = copy.deepcopy(list_result_evaluate[dw][es])
                        status = algorithm_evaluate(sender, status, coverage)
                        j += 1
                        list_result_evaluate[dw][es] = copy.deepcopy(status)
                    i += 1

            if sender == "Total":
                list_result_evaluate = copy.deepcopy(list_evaluate)

                coverage = copy.deepcopy(list_result_sum)

                i = 0
                while i < len(evaluate_status):
                    es = evaluate_status[i]
                    status = copy.deepcopy(list_result_evaluate[es])
                    status = algorithm_evaluate(sender, status, coverage)

                    list_result_evaluate[es] = copy.deepcopy(status)
                    i += 1

            print_evaluate(sender, list_result_evaluate)
        except Exception as var_except:
            print("COMPUTER [.. -> Evaluate -> " +
                  str(sender) + " -> Evaluate coverage]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()

    def print_evaluate(sender, list_result_evaluate):
        try:
            if sender == "For each days":

                day_week = [
                    "mon", "tue", "wed",
                    "thu", "fri", "sat",
                    "sun"
                ]

                day_week_ru = [
                    "Понедельник", "Вторник", "Среда",
                    "Четверг", "Пятница", "Суббота",
                    "Воскресенье"
                ]

                evaluate_status = [
                    "best", "good", "norm"
                ]

                evaluate_status_ru = [
                    "Отличное время", "Хорошее время", "Нормальное время"
                ]

                text_output = ""

                i = 0
                while i < len(day_week):
                    text_output += "\n=== " + str(day_week_ru[i]) + " ===\n"
                    time_range = 1
                    j = 0
                    while j < len(list_result_evaluate[day_week[i]]):
                        dw = day_week[i]
                        es = evaluate_status[j]
                        status = list_result_evaluate[dw][es]
                        n = 0
                        while n < len(status):
                            time_output = ""
                            k = 0
                            while k < len(status[str(n)]["time"]):
                                if k == len(status[str(n)]["time"]) - 1:
                                    time_output += status[str(n)]["time"][k]
                                else:
                                    time_output += status[str(n)]["time"][k] +\
                                        ", "
                                k += 1

                            text_output += "\n"
                            text_output += str(time_range) + ") "
                            text_output += str(time_output) + " ("
                            text_output += str(status[str(n)]["value"]) + ")"

                            time_range += 1

                            n += 1
                        j += 1
                    text_output += "\n"
                    i += 1

            if sender == "Total":
                evaluate_status = [
                    "best", "good", "norm"
                ]

                evaluate_status_ru = [
                    "Отличное время", "Хорошее время", "Нормальное время"
                ]

                text_output = ""

                time_range = 1

                i = 0
                while i < len(list_result_evaluate):
                    es = evaluate_status[i]
                    status = list_result_evaluate[es]
                    n = 0
                    while n < len(status):
                        time_output = ""
                        k = 0
                        while k < len(status[str(n)]["time"]):
                            if k == len(status[str(n)]["time"]) - 1:
                                time_output += status[str(n)]["time"][k]
                            else:
                                time_output += status[str(n)]["time"][k] +\
                                    ", "
                            k += 1
                        text_output += "\n" + str(time_range) + ") "
                        text_output += str(time_output) + " ("
                        text_output += str(status[str(n)]["value"]) + ")"

                        time_range += 1

                        n += 1
                    text_output += "\n"
                    i += 1

            print(str(text_output))
            export_evaluate(sender, text_output)

        except Exception as var_except:
            print("COMPUTER [.. -> Evaluate -> " +
                  str(sender) + " -> Print evaluate]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()
        evaluate_menu()

    def export_evaluate(sender, text_output):
        try:
            print("\nCOMPUTER [.. -> Evaluate -> " + str(sender) +
                  " -> Export]: Export result of evaluate to text file?")
            user_answer = raw_input("USER [.. -> Evaluate -> " + str(sender) +
                                    " -> Export]: (1/0) ")

            user_answer = re.sub("[^0123456789\.]", "", user_answer)

            file_name = ""

            if sender == "Total":
                file_name = "evaluate_total"
            if sender == "For each days":
                file_name = "evaluate_each_days"

            if user_answer == "0":
                evaluate_menu()
            else:
                if user_answer == "1":
                    write_text(sender, PATH +
                               "output/", file_name, text_output)
                else:
                    print("COMPUTER [.. -> Evaluate -> " +
                          str(sender) +
                          " -> Export]: " +
                          "Error, check entered data. Retry query...")
                    export_evaluate(sender, text_output)
        except Exception as var_except:
            print("COMPUTER [.. -> Evaluate -> " +
                  str(sender) + " -> Print evaluate]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()
        evaluate_menu()

    print("\nCOMPUTER [.. -> Evaluate]: You are in menu of evaluate.")
    print("COMPUTER [.. -> Evaluate]: Enter digit for next action. (1-2/0)")
    print("COMPUTER [.. -> Evaluate]: 1 == Total.")
    print("COMPUTER [.. -> Evaluate]: 2 == For each days.")
    print("COMPUTER [.. -> Evaluate]: 0 == Step back.")

    def evaluate_total():
        collect_files("Total")

    def evaluate_each():
        collect_files("For each days")

    user_answer = raw_input("USER [.. -> Evaluate]: ")

    user_answer = re.sub("[^0123456789\.]", "", user_answer)

    if user_answer == "0":
        main_menu()
    else:
        if user_answer == "1":
            evaluate_total()
        else:
            if user_answer == "2":
                evaluate_each()
            else:
                print("COMPUTER [.. -> Evaluate]: Unknown command. " +
                      "Retry query...")
                evaluate_menu()


def close_program():
    print("\nCOMPUTER [Main menu]: Exit from program...")
    exit()


starter()
