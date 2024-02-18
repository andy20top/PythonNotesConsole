import datetime
import uuid
from operator import itemgetter
import re
import notes


def input_title():
    return input("Введите заголовок заметки: ").title()

def input_body():
    return input("Введите текст заметки: ").title()

def print_data():
    old_list = []

    with (open("app_notes.json", 'r', encoding='utf-8') as file):
        notes_list = file.read().rstrip().split("\n\n")
    for line in notes_list:
        new_line = line.split(": ")
        old_list.append(new_line)

    try:
        old_list.sort(key=itemgetter(4), reverse=True)

        for num, line in enumerate(old_list, 1):
            new_st = ": ".join(line)
            print(f"Note № {num};\n{new_st}\n")
    except:
        print("None")

def print_one_note():
    i_change = int(input("Введите номер заметки, которую необходимо показать: "))
    with open("app_notes.json", 'r', encoding='utf-8') as file:
        notes_list = file.read().rstrip().split("\n\n")
    print(f"Note № {i_change}\n{notes_list[i_change-1]}")

def add_notes():
    new_note = notes.Notes(input_title(), input_body())
    unicNum = uuid.uuid4()

    with open("app_notes.json", 'a', encoding='utf-8') as file:
        file.write(f"ID: {unicNum};\n{new_note.get_string()}")
    print("Заметка добавлена")

def change_note():
    i_change = int(input("Введите номер заметки, которую необходимо изменить: ")) - 1
    with open("app_notes.json", 'r', encoding='utf-8') as file:
        notes_list = file.read().rstrip().split("\n\n")
    with open("app_notes.json", 'r', encoding='utf-8') as file:
        file_data = file.read()
    str = notes_list[i_change].split("\n")

    print("\nЧто вы хотите изменить?\n"
          "1. Заголовок\n"
          "2. Тело заметки")
    command = input("Ваш выбор: ")
    while command not in ("1", "2"):
        print("Некорректный ввод")
        command = input("Ваш выбор: ")

    old_data = str[int(command)]
    new_in = input("Введите новые данные: ")
    if (int(command) == 1):
        new_data = "Title: " + new_in + ";"
    else:
        new_data = "Body: " + new_in + ";"
    new_date = "Date last change: " + datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y') + ";"

    changes_notes = file_data.replace(old_data, new_data).replace(str[3], new_date)

    with open("app_notes.json", 'w', encoding='utf-8') as file:
        file.write(changes_notes)

def delete_note():
    i_delete = int(input("Введите номер заметки, которую нужно удалить: "))
    with open("app_notes.json", 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split("\n\n")
    with open('app_notes.json', 'w', encoding='utf-8') as file:
        for num_line, line in enumerate(contacts_list, 1):
            if num_line != i_delete:
                file.write(f"{line}\n\n")
    print("Заметка удалена")

def interface():
    with open("app_notes.json", 'a', encoding='utf-8'):
        pass
    command = ""
    while command != "6":
        print("\nМеню пользователя:\n"
              "1. Вывод всех заметок на экран\n"
              "2. Вывод заметки на экран под определенным номером\n"
              "3. Добавить заметку\n"
              "4. Удалить заметку\n"
              "5. Изменить заметку\n"
              "6. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", "3", "4", "5", "6"):
            print("Некорректный ввод")
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                print()
                print_data()
                com = ""
                while com != "0":
                    com = input("\nВведите 0, чтобы вернуться в меню: ")
                    if (com not in "0"):
                        print("Некорректный ввод. Попробуйте снова")
            case "2":
                print()
                print_one_note()
                com = ""
                while com != "0":
                    com = input("\nВведите 0, чтобы вернуться в меню: ")
                    if (com not in "0"):
                        print("Некорректный ввод. Попробуйте снова")
            case "3":
                add_notes()
            case "4":
                delete_note()
            case "5":
                change_note()
            case "6":
                print("Завершение программы")



if __name__ == '__main__':
    interface()





