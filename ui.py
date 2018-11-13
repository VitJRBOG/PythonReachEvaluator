# coding: utf8
u"""Модуль консольного пользовательского интерфейса."""


import input_data
import output_data
import collecting_data
import evaluation_reach
import export_result
import data_json_creator
import template_json_creator


def main_menu():
    u"""Основное меню программы."""
    def output_actions():
        u"""Вывод доступных действий главного меню."""
        print("COMPUTER: You are in Main menu. Select next action.")
        actions = [
            "Collect reach", "Evaluate collected logs",
            "Export evaluation result", "Initialization res-files"
        ]
        for i, action in enumerate(actions):
            output = "COMPUTER [Main menu]: " + str(i + 1) + " == " + action
            print(output)
        output = "COMPUTER [Main menu]: 00 == Quit"
        print(output)
        return len(actions)
    
    def check_user_answer(number_actions):
        u"""Проверка ответа пользователя."""
        user_answer = raw_input(
            "USER [Main menu]: (1-" + str(number_actions) + "/00) ")
        if user_answer == "00":
            print("COMPUTER: Quit...")
            exit(0)
        elif user_answer == "1":
            run_collection_reach()
        elif user_answer == "2":
            run_evaluating_logs()
        elif user_answer == "3":
            run_evaluation_result_export()
        elif user_answer == "4":
            run_initicalization_res_files()
        else:
            print("COMPUTER: Error. Pleace, repeat input.")
            return check_user_answer(number_actions)
    number_actions = output_actions()
    check_user_answer(number_actions)


def run_collection_reach():
    u"""Запуск функций сбора охвата."""
    access_token = input_data.get_vk_user_token()
    vk_session = collecting_data.authorization(access_token)
    str_begin_date = input_data.get_target_date()
    print("COMPUTER: Please stand by...")
    collecting_data.run_collecting_data(vk_session, str_begin_date)
    output = "COMPUTER [.. -> Collect reach]: " +\
        "Collection of post reach has been successfully completed."
    print(output)

    main_menu()


def run_evaluating_logs():
    u"""Запуск функций оценки охвата и вывода результатов."""
    def call_functions_for_evaluate(type_posts):
        text_output = evaluation_reach.evaluate(type_posts)
        output_data.export_data_to_text(text_output, type_posts)
        output = "COMPUTER [.. -> Evaluate collected logs]: " +\
            "Evaluation of " + type_posts +\
            " reach logs has been successfully completed."
        print(output)
    call_functions_for_evaluate("ads")
    call_functions_for_evaluate("posts")

    main_menu()


def run_evaluation_result_export():
    u"""Выводит результат оценки на вики-страничку в ВК."""
    access_token = input_data.get_vk_user_token()
    vk_session = collecting_data.authorization(access_token)
    print("COMPUTER: Please stand by...")
    export_result.exporting(vk_session)
    output = "COMPUTER [.. -> Export evaluation result]: " +\
        "Export evaluation results has been successfully completed."
    print(output)

    main_menu()


def run_initicalization_res_files():
    u"""Выводит доступные действия инициализации res-файлов."""
    def run_initialization_data_json():
        u"""Запускает основные функции инициализации data.json."""
        data_json_creator.run_data_json_creator()
        output = "COMPUTER [.. -> Initialization res-files]: " + \
            "Initialization data.json has been successfully completed."
        print(output)
        run_initicalization_res_files()

    def run_initialization_template_json():
        u"""Запускает основные функции инициализации template.json."""
        template_json_creator.run_template_json_creator()
        output = "COMPUTER [.. -> Initialization res-files]: " +\
            "Initialization template.json has been successfully completed."
        print(output)
        run_initicalization_res_files()

    def output_actions():
        u"""Вывод доступных действий меню инициализации."""
        print("COMPUTER: You are in Initialization res-files menu. Select next action.")
        actions = [
            "Initialize data.json", "Initialize template.json"
        ]
        for i, action in enumerate(actions):
            output = "COMPUTER [.. -> Initialization res-files]: " + \
                str(i + 1) + " == " + action
            print(output)
        output = "COMPUTER [.. -> Initialization res-files]: 00 == Step back"
        print(output)
        return len(actions)

    def check_user_answer(number_actions):
        u"""Проверка ответа пользователя."""
        user_answer = raw_input(
            "USER [Main menu]: (1-" + str(number_actions) + "/00) ")
        if user_answer == "00":
            main_menu()
        elif user_answer == "1":
            run_initialization_data_json()
        elif user_answer == "2":
            run_initialization_template_json()
        else:
            print("COMPUTER: Error. Pleace, repeat input.")
            return check_user_answer(number_actions)
    number_actions = output_actions()
    check_user_answer(number_actions)
