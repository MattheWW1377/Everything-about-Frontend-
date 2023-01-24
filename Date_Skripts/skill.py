import csv
import re
import matplotlib.pyplot as plt

def clean_row(row):
    return re.sub(r'\<[^>]*\>', '', row)


def csv_reader(file_name):
    csv_file = open(file_name, encoding='utf-8-sig')
    reader = csv.reader(csv_file, delimiter=',')
    list_naming = reader.__next__()
    return reader, list_naming


def csv_filer(reader, list_naming):
    data_vacancies = []
    for row in reader:
        if len(row) == len(list_naming) and all(row):
            clear_row = list(map(clean_row, row))
            for i in range(len(clear_row)):
                if clear_row[i].find('\n') != -1:
                    clear_row[i] = clear_row[i].split('\n')
                    for j in range(len(clear_row[i])):
                        clear_row[i][j] = ' '.join(clear_row[i][j].split())
                elif i == 2:
                    clear_row[i] = ' '.join(clear_row[i].split())
                    clear_row[i] = [clear_row[i]]
                else:
                    clear_row[i] = ' '.join(clear_row[i].split())
            vacancy = {}
            for i in range(len(list_naming)):
                vacancy[list_naming[i]] = clear_row[i]
            data_vacancies.append(vacancy)
    return data_vacancies


skills = {}
aboba = []
a = csv_reader(input('Название файла — '))
profession = input('Профессия — ').split(', ')
vacancies = csv_filer(a[0], a[1])
for year in range(2015, 2023):
    for vacancy in vacancies:
        if any([i in vacancy['name'] for i in profession]) and str(year) == vacancy['published_at'][:4]:
            all_skills = vacancy['key_skills']
            for skill in all_skills:
                if skills.get(skill, False) :
                    skills[skill] += 1
                else:
                    skills[skill] = 1
    abc = list(sorted(skills.items(), key=lambda item: item[1], reverse=True))
    abc = abc[:10]
    print('Ok')
    aboba.append(abc)
for i in aboba:
    for j in i:
        print(j[0])
    print(" ")
    print(" ")
    print(" ")
    print(" ")


#frontend, фронтенд, вёрстка, верстка, верста, front end, angular, html, css, react, vue