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
    print("\nCOMPUTER [.. -> New data]: You are in menu of add new data.")
    print("COMPUTER [.. -> New data]: " +
          "Enter numbers of day and month, and name of day week.")

    obj_day = Day()

    try:
        user_answer = raw_input("USER [.. -> New data -> Day number]: ")
        obj_day.set_day_number = int(user_answer)
    except Exception as var_except:
        print(
            "COMPUTER [.. -> New data -> Day number]: Error, " +
            str(var_except) +
            ". Return to Main menu...")
        main_menu()

    try:
        user_answer = raw_input("USER [.. -> New data -> Number of month]: ")
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

    # read json-file with intervals
    # function for enter data of reach

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
