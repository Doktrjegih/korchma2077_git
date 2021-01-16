import csv
import random
import datetime
import colorama
from colorama import Fore, Style


def new_time(particular_time, oldest_records, count):
    with open("test.csv", "r") as file:  # 1. читаем все строки в файле
        lines = file.readlines()
    for line in lines:  # 2. удаляем строку пройденного слова (определяем по времени)
        if oldest_records[count][2] in line:
            lines.remove(line)
    with open("test.csv", "w") as file:  # 3. записываем обратно все строки без убранной
        file.writelines(lines)
    with open("test.csv", mode="a",
              encoding='utf-8') as w_file:  # 4. дописываем в конец файла слово с новой датой
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        oldest_records[count][2] = particular_time
        file_writer.writerow(oldest_records[count])


def new_word():
    class Word:
        def __init__(self):
            self.en_word = input('введите новое слово: ')
            self.ru_word = input('введите перевод: ')
            print('все верно? (0 для выхода)', self.en_word, '-', self.ru_word)
            answer = input()
            if answer == '+':
                self.ans = True
            elif answer == '-':
                self.ans = False
                new_word()
            elif answer == '0':
                main_menu()

        def addword(self):
            with open("test.csv", mode="a",
                      encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                now = datetime.datetime.now()
                new = [self.en_word, self.ru_word, str(now.isoformat()), 0]
                file_writer.writerow(new)

    word = Word()
    if word.ans:
        word.addword()


def main_menu():
    print('''лео сосатб
----------
выбери действие:
[1] тренироваться
[2] добавить слово

[0] выход''')
    action = int(input())
    if action == 0:
        exit()
    if action == 1:
        training()
    elif action == 2:
        new_word()


def training():
    with open("test.csv", encoding='utf-8') as r_file:  # открываем файл на чтение
        reader = csv.reader(r_file, delimiter=",")
        sortedlist = sorted(reader, key=lambda row: row[2], reverse=False)  # сортировка по дате
        oldest_records = sortedlist[0:10]  # выбор трех самых старых записей
        for i in range(10):  # цикл для взаимодействия с пользователем (вопрос-ответ)
            answer_list = []  # обнуляем список вариантов ответа
            count = random.randint(0, len(oldest_records) - 1)  # для рандома
            print(oldest_records[count][0])  # выводим слово-вопрос
            answer_list.append(oldest_records[count][1])  # добавляем правильный ответ к списку вариантов
            with open("test.csv", encoding='utf-8') as r_file1:  # считаем кол-во строк в файле
                reader1 = csv.reader(r_file1, delimiter=",")
                amount_of_stings = 0
                for m in reader1:
                    amount_of_stings += 1
            rand_list = []
            for nn in range(4):  # выбираем номера строк для случайных вариантов ответа
                rand_list.append(random.randint(1, amount_of_stings))
            # print(rand_list)  # какие элементы тащит для вариантов ответа
            with open("test.csv", encoding='utf-8') as r_file2:  # выбираем случайные варианты ответа из файла
                reader2 = csv.reader(r_file2, delimiter=",")
                number_of_string = 0
                for n in reader2:
                    number_of_string += 1
                    if number_of_string in rand_list:
                        answer_list.append(n[1])
            random.shuffle(answer_list)  # перемешиваем список вариантов ответа
            print('---select right answer (0 для выхода)---')  # показываем варианты пользователю
            counter = 0
            for x in answer_list:
                counter += 1
                print(counter, x)
            answer1 = int(input())  # спрашиваем номер правильного варианта
            if answer1 == 0:
                main_menu()
            if answer_list[answer1 - 1] == oldest_records[count][1]:  # условие если правильно/неправильно
                print('great!\n')
                now = datetime.datetime.now()
                new_time(str(now.isoformat()), oldest_records, count)
            else:
                colorama.init()
                print(f'nope, right answer is: ' + Fore.GREEN + oldest_records[count][1].lower())
                print(Style.RESET_ALL)
                tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)  # сделать + ~50 записей от самой старой
                new_time(str(tomorrow.isoformat()), oldest_records, count)
            del(oldest_records[count])  # слово пройдено, убираем из цикла


main_menu()
