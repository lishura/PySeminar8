import csv
import os


def add_contact():
    with open('last_ID.txt', 'r', encoding='utf-8') as info:
        last_ID = int(info.read())
    with open('contacts.csv', 'a', encoding='utf-8') as file:
        columns = ["ID", "Ф.И.О.", "Дата рождения", "Должность", "Дата приема на работу", "Оклад"]
        file_writer = csv.DictWriter(file, delimiter = ",", lineterminator="\r", fieldnames=columns)
        file_writer.writerow({"ID": last_ID+1, "Ф.И.О.": input("Введите Ф.И.О. нового сотрудника: "), "Дата рождения": input("Введите дату рождения нового сотрудника: "), "Должность": input("Введите должность нового сотрудника: "), "Дата приема на работу": input("Введите дату приема на работу нового сотрудника: "), "Оклад": input("Введите оклад нового сотрудника: ")})
    with open('last_ID.txt','w', encoding='utf-8') as f:
        f.write(str(last_ID+1))


def print_contacts():
        with open('contacts.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)  
            line_count = 0   
            for row in csv_reader:
                if line_count == 0:
                    print("             ".join(row))
                    line_count+=1
                print(f'{row["ID"].center(5)} {row["Ф.И.О."].center(40)} {row["Дата рождения"].center(12)}{row["Должность"].center(15)} {row["Дата приема на работу"].center(10)}{row["Оклад"].center(7)}')
                line_count+=1
                

def delete_contact():
    id_del = int(input("Введите ID сотрудника для удаления: "))
    with open('contacts.csv', 'r', encoding='utf-8') as inp, open('contacts_del.csv', 'w', encoding='utf-8', newline='') as out:
        columns = ["ID", "Ф.И.О.", "Дата рождения", "Должность", "Дата приема на работу", "Оклад"]
        csv_reader = csv.DictReader(inp)
        csv_writer = csv.DictWriter(out, fieldnames=columns)
        csv_writer.writeheader()
        line_count = 0 
        for row in csv_reader:
            if int(row["ID"]) != id_del:
                csv_writer.writerow({"ID": line_count+1, "Ф.И.О.": row["Ф.И.О."], "Дата рождения": row["Дата рождения"], "Должность": row["Должность"], "Дата приема на работу": row["Дата приема на работу"], "Оклад": row["Оклад"]})
                line_count+=1
    with open('last_ID.txt','w', encoding='utf-8') as f:
        f.write(str(line_count))
    os.remove('contacts.csv')
    os.rename('contacts_del.csv', 'contacts.csv')

        



    
