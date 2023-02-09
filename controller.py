from faker import Faker
import model
import csv
import random

fake = Faker(locale = "ru_RU")


def fill_contacts():   
    with open('contacts.csv', 'w', encoding='utf-8') as file:
        columns = ["ID", "Ф.И.О.", "Дата рождения", "Должность", "Дата приема на работу", "Оклад"]
        file_writer = csv.DictWriter(file, delimiter = ",", lineterminator="\r", fieldnames=columns)
        file_writer.writeheader()
        for i in range(10):
            file_writer.writerow({"ID": i+1, "Ф.И.О.": fake.name(), "Дата рождения": fake.date_of_birth(minimum_age=25, maximum_age=50), "Должность": fake.job(), "Дата приема на работу": fake.date_this_century(), "Оклад": random.randint(50000, 80000)})
        with open('last_ID.txt','w', encoding='utf-8') as f:
            f.write(str(i+1))


def greeting():
    print('Добро пожаловать в базу данных сотрудников ООО "Ромашка"')


def choice_todo():
    print("Доступные операции с базой данных сотрудников:\n\
    1 - печать базы данных сотрудников;\n\
    2 - добавление нового сотрудника;\n\
    3 - удаление сотрудника;\n")
    ch = input("Введите номер операции: ")
    match ch:
        case '1':
            model.print_contacts()
        case '2':
            model.add_contact()
        case '3':
            model.delete_contact()










