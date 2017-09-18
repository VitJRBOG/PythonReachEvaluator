# coding: utf8


import os
import json
import copy


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


def starter():
    try:

        if os.path.exists("path.txt") is False:
            file_text = open("path.txt", "w")
            file_text.write("")
            file_text.close()
            print("COMPUTER: Was created file \"path.txt\".")

        path = str(open("path.txt", "r").read())

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

        if path[len(path) - 1] != "/":
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
    print("COMPUTER [Main menu]: Enter digit for next action. (1-4/0)")
    print("COMPUTER [Main menu]: 1 == Add new data about reach.")
    print("COMPUTER [Main menu]: 2 == Show data.")
    print("COMPUTER [Main menu]: 3 == Settings of intervals.")
    print("COMPUTER [Main menu]: 4 == Evaluate.")
    print("COMPUTER [Main menu]: 0 == Close the program.")

    user_answer = raw_input("USER [Main menu]: (1-4/0) ")

    if user_answer == "0":
        close_program()
    else:
        if user_answer == "1":
            add_menu()
        else:
            if user_answer == "2":
                show_menu()
            else:
                if user_answer == "3":
                    settings_menu()
                else:
                    if user_answer == "4":
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

            if user_answer == "00":
                print("COMPUTER [.. -> New data -> Posts amount]: Abort. " +
                      "Return to Main menu...")
                main_menu()
            else:
                if user_answer != "" and\
                   int(user_answer) > 0 and int(user_answer) < 11:
                    coverage = 0
                    i = 0
                    while i < int(user_answer):
                        coverage = coverage +\
                            enter_coverage(interval["time"], i + 1)
                        i += 1

                    coverage = int(coverage) / int(user_answer)

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

    def enter_coverage(interval_time, post_number):

        try:

            while True:

                user_answer = raw_input("USER [.. -> " + str(interval_time) +
                                        " -> Post coverage №" +
                                        str(post_number) + "]: ")

                if user_answer != "" and int(user_answer) > 999:

                    answer = float(float(user_answer) / 100)

                    answer = round(answer)

                    answer = answer * 100

                    return int(answer)

                else:
                    print("COMPUTER [.. -> Post coverage]: " +
                          "Error, check entered data. Retry query...")

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
              "Menu settings.")
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


def show_menu():

    PATH = read_path_txt()

    def export_query(sender, file_name, text_output):

        try:
            print("\nCOMPUTER [.. -> " + str(sender) +
                  " -> Make output -> Export]: Export log to text file?")
            user_answer = raw_input("USER [.. -> " + str(sender) +
                                    " -> Make output -> Export]: (1/0) ")

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
                    i = 0
                    while i < len(list_files):
                        print("[" + str(i + 1) + "] " + str(list_files[i]))
                        count += 1
                        i += 1

                if sender == "By days week logs":

                    day_week = [
                        "понедельник", "вторник", "среда",
                        "четверг", "пятница", "суббота",
                        "воскресенье"
                    ]

                    print("\n")
                    i = 0
                    while i < len(day_week):
                        print("[" + str(i + 1) + "] " + str(day_week[i]))
                        i += 1

                    print("\nCOMPUTER [.. -> Show files -> " +
                          str(sender) + "]: " +
                          "Select day of the week, or exit to Show menu.")
                    user_answer = raw_input("USER [.. -> " + str(sender) +
                                            "] " +
                                            "(1-" + str(len(day_week)) +
                                            "/0) ")

                    if user_answer == "0":
                        show_menu()
                    else:
                        if int(user_answer) > 0 \
                           and int(user_answer) <= len(day_week):

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

                if sender == "By months logs":

                    month = [
                        "январь", "февраль", "март",
                        "апрель", "май", "июнь",
                        "июль", "август", "сентябрь",
                        "октябрь", "ноябрь", "декабрь"
                    ]

                    print("\n")
                    i = 0
                    while i < len(month):
                        print("[" + str(i + 1) + "] " + str(month[i]))
                        i += 1

                    print("\nCOMPUTER [.. -> Show files -> " +
                          str(sender) + "]: " +
                          "Select month, or exit to Show menu.")
                    user_answer = raw_input("USER [.. -> " + str(sender) +
                                            "] " +
                                            "(1-" + str(len(month)) +
                                            "/0) ")

                    if user_answer == "0":
                        show_menu()
                    else:
                        if int(user_answer) > 0 \
                           and int(user_answer) <= len(month):

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

                print("\nCOMPUTER [.. -> Show files -> " +
                      str(sender) + "]: " +
                      "Select file, or exit to Show menu.")
                user_answer = raw_input("USER [.. -> " +
                                        str(sender) +
                                        "] (1-" +
                                        str(count) +
                                        "/0) ")

                if user_answer == "0":
                    show_menu()
                else:
                    if int(user_answer) > 0 \
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
    print("\nCOMPUTER [.. -> Settings]: You are in menu of settings.")

    # temporary
    print("COMPUTER [.. -> Settings]: ...")
    print("COMPUTER [.. -> Settings]: Here is empty, return to Main menu.")
    main_menu()
    # temporary

    print("COMPUTER [.. -> Settings]: Enter digit for next action.")


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
            evaluate_coverage(sender, list_result_sum)
        except Exception as var_except:
            print("COMPUTER [.. -> Evaluate -> " +
                  str(sender) + " -> Sum coverage]: Error, " +
                  str(var_except) +
                  ". Return to Main menu...")
            main_menu()
        evaluate_menu()

    def evaluate_coverage(sender, list_result_sum):
        try:
            day_week = [
                "mon", "tue", "wed",
                "thu", "fri", "sat",
                "sun"
            ]

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
                    j += 1
                    list_result_evaluate[dw][es] = copy.deepcopy(status)
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
                j = 0
                while j < len(list_result_evaluate[day_week[i]]):
                    dw = day_week[i]
                    es = evaluate_status[j]
                    status = list_result_evaluate[dw][es]
                    text_output += "\n'''" +\
                        str(evaluate_status_ru[j]) + ":''' "
                    n = 0
                    while n < len(status):
                        time_output = ""
                        k = 0
                        while k < len(status[str(n)]["time"]):
                            if k == len(status[str(n)]["time"]) - 1:
                                time_output += status[str(n)]["time"][k]
                            else:
                                time_output += status[str(n)]["time"][k] + ", "
                            k += 1
                        text_output += "\n" + str(n + 1) + ") "
                        text_output += str(time_output) + " ("
                        text_output += str(status[str(n)]["value"]) + ")"
                        n += 1
                    text_output += "\n"
                    j += 1
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

            file_name = ""

            if sender == "Total":
                file_name = "evaluate_total"
            if sender == "For each days":
                file_name = "evaluate_each_days"
            if sender == "For selected days":
                file_name = "evaluate_selected_days"

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
    print("COMPUTER [.. -> Evaluate]: Enter digit for next action. (1-3/0)")
    print("COMPUTER [.. -> Evaluate]: 1 == Total.")
    print("COMPUTER [.. -> Evaluate]: 2 == For each days.")
    print("COMPUTER [.. -> Evaluate]: 3 == For select days.")
    print("COMPUTER [.. -> Evaluate]: 0 == Step back.")

    def evaluate_total():
        # temporary
        print("COMPUTER [.. -> Evaluate]: ...")
        print("COMPUTER [.. -> Evaluate]: Here is empty, return to Main menu.")
        main_menu()
        # temporary

    def evaluate_each():
        collect_files("For each days")

    def evaluate_select():
        # temporary
        print("COMPUTER [.. -> Evaluate]: ...")
        print("COMPUTER [.. -> Evaluate]: Here is empty, return to Main menu.")
        main_menu()
        # temporary

    user_answer = raw_input("USER [.. -> Evaluate]: ")

    if user_answer == "0":
        main_menu()
    else:
        if user_answer == "1":
            evaluate_total()
        else:
            if user_answer == "2":
                evaluate_each()
            else:
                if user_answer == "3":
                    evaluate_select()
                else:
                    print("COMPUTER [.. -> Evaluate]: Unknown command. " +
                          "Retry query...")
                    evaluate_menu()


def close_program():
    print("\nCOMPUTER [Main menu]: Exit from program...")
    exit()


starter()
