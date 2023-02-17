import time
# import PySimpleGUI as sg

FILEPATH = "todolist.txt"


def current_list(filepath=FILEPATH):
    """
    Open a todolist.txt in read mode and assign it to the local variable todolist.
    :param filepath: Default is todolist.txt
    :return:
    The current to do list.
    """
    with open(filepath, 'r') as file_local:
        todolist_local = file_local.readlines()
        return todolist_local


def print_with_index(my_list):
    """
    Pass the current list in, and then it prints out the contents of the list line by line with its index + 1
    :param my_list:
    :return:
    """
    for index_local, item in enumerate(my_list):
        row = f'{index_local + 1}. {item}'
        print(row.strip())


def write_to_list(my_list, filepath=FILEPATH):
    """
    Takes the filepath passed in and writes to it with the list that is passed in.
    :param filepath: Default is todolist.txt
    :param my_list:
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(my_list)


def greeting_user():
    """
    Simple function that greets the user at the beginning of the script depending on the time of day
    :return:
    """
    x = int(time.strftime("%H"))
    if x > 19:
        print("Good Evening.")
    elif 12 <= x <= 19:
        print("Good Afternoon.")
    else:
        print("Good Morning.")


# def create_new_edit_window():
#     edit_input_box = sg.InputText(key="Edit Input")
#     confirm_edit_button = sg.Button("Done", key="Confirm")
#     return sg.Window("Edit Item", layout=[[edit_input_box, confirm_edit_button]],
#                      font=('Helvetica', 15))
#
#
# def close_edit_window(edit_window_local):
#     edit_window_local.close()
