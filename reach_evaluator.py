# coding: utf8


import os
import json


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
        if os.path.exists("output") is False:
            os.mkdir("output")
            print("COMPUTER: Was created directory \"output\".")

        if os.path.exists("json") is False:
            os.mkdir("json")
            print("COMPUTER: Was created directory \"json\".")

    except Exception as var_except:
        print(
            "COMPUTER: Error, " + str(var_except) + ". Exit from program...")
        exit()
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


def write_json(sender):
    # temporary
    print("COMPUTER [.. -> " + str(sender) + " -> Write JSON]: ...")
    print("COMPUTER [.. -> " + str(sender) + " -> Write JSON]: " +
          "Here is empty, return to Main menu.")
    main_menu()
    # temporary


def main_menu():
    print("\nCOMPUTER: You are in Main menu.")
    print("COMPUTER: Enter digit for next action. (1-4/0)")
    print("COMPUTER [Main menu]: 1 == Add new data about reach.")
    print("COMPUTER [Main menu]: 2 == Show data.")
    print("COMPUTER [Main menu]: 3 == Settings of intervals.")
    print("COMPUTER [Main menu]: 4 == Evaluate.")
    print("COMPUTER [Main menu]: 0 == Close the program.")

    user_answer = raw_input("USER [Main menu -> ..]: ")

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

    def enter_date(obj_day):
        print("COMPUTER [.. -> New data]: " +
              "Enter numbers of day and month, and name of day week.")

        try:
            user_answer = raw_input("USER [.. -> New data -> " +
                                    "Day number]: ")
            obj_day.set_day_number = int(user_answer)
        except Exception as var_except:
            print(
                "COMPUTER [.. -> New data -> Day number]: Error, " +
                str(var_except) +
                ". Return to Main menu...")
            main_menu()

        try:
            user_answer = raw_input("USER [.. -> New data -> " +
                                    "Number of month]: ")
            obj_day.set_month_number = int(user_answer)
        except Exception as var_except:
            print(
                "COMPUTER [.. -> New data -> Number of month]: Error, " +
                str(var_except) +
                ". Return to Main menu...")
            main_menu()

        try:
            user_answer = raw_input("USER [.. -> New data -> Day week]: ")
            obj_day.set_day_week = user_answer
        except Exception as var_except:
            print(
                "COMPUTER [.. -> New data -> Day week]: Error, " +
                str(var_except) +
                ". Return to Main menu...")
            main_menu()

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
                                    "]: (1-50/00) ")

            if user_answer == "00":
                print("COMPUTER [.. -> New data -> Posts amount]: Abort. " +
                      "Return to Main menu...")
                main_menu()
            else:
                if int(user_answer) > 0 and int(user_answer) < 51:
                    coverage = 0
                    i = 0
                    while i < int(user_answer):
                        coverage = coverage + \
                            enter_coverage(interval["time"], i + 1)
                        i += 1

                    interval["value"] = coverage
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
            user_answer = raw_input("USER [.. -> " + str(interval_time) +
                                    " -> Post coverage №" +
                                    str(post_number) + "]: ")

            # rounding

            return int(user_answer)

        except Exception as var_except:
            print(
                "COMPUTER [.. -> " + str(var_except) +
                " -> Post coverage]: Error, " +
                str(var_except) +
                ". Return to Main menu...")
            main_menu()

    print("\nCOMPUTER [.. -> New data]: You are in menu of add new data.")

    if os.path.exists("template.json") is False:
        print("COMPUTER [.. -> New data]: " +
              "File \"template.json\" is not exist. Check " +
              "Menu settings.")
        print("COMPUTER [.. -> New data]: Return to Main menu...")
        main_menu()
    else:
        obj_day = Day()
        loads_json = read_json("New data", "", "template")
        obj_day = enter_date(obj_day)
        obj_day = check_intervals(obj_day, loads_json)

        # func of making loads_json from obj_day
        # func writing loads_json to json file

    # temporary
    print("COMPUTER [.. -> New data]: ...")
    print("COMPUTER [.. -> New data]: Here is empty, return to Main menu.")
    main_menu()
    # temporary


def show_menu():
    print("\nCOMPUTER [.. -> Show data]: You are in menu of show data.")

    # temporary
    print("COMPUTER [.. -> Show data]: ...")
    print("COMPUTER [.. -> Show data]: Here is empty, return to Main menu.")
    main_menu()
    # temporary

    print("COMPUTER [.. -> Show data]: Enter digit for next action.")


def settings_menu():
    print("\nCOMPUTER [.. -> Settings]: You are in menu of settings.")

    # temporary
    print("COMPUTER [.. -> Settings]: ...")
    print("COMPUTER [.. -> Settings]: Here is empty, return to Main menu.")
    main_menu()
    # temporary

    print("COMPUTER [.. -> Settings]: Enter digit for next action.")


def evaluate_menu():
    print("\nCOMPUTER [.. -> Evaluate]: You are in menu of evaluate.")

    # temporary
    print("COMPUTER [.. -> Evaluate]: ...")
    print("COMPUTER [.. -> Evaluate]: Here is empty, return to Main menu.")
    main_menu()
    # temporary

    print("COMPUTER [.. -> Evaluate]: Enter digit for next action.")


def close_program():
    print("\nCOMPUTER [Main menu]: Exit from program...")
    exit()


starter()
