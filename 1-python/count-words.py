import pathlib
import os
import datetime


clear = lambda: os.system('cls')
clear()

data_folder = pathlib.Path().absolute()
print(data_folder)

# name = input('Enter file:> ')

name = "lev.txt"

handle = open(os.path.join(data_folder, name), 'r') #функция для открытия файла с параметром 'r' - открытие на чтение (является значением по умолчанию)
counts = dict() #создание словаря - неупорядоченной коллекции произвольных объектов с доступом по ключу

start = datetime.datetime.now()
 
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None)
 
bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

finish = datetime.datetime.now()

print("Самое распространенное слово","'"+ bigword+"'","встретилось", bigcount, "раз(а), оно нашлось за", (start - finish).microseconds / 1e6, "с")

while True :
    my_word = input('Enter word:> ')
    if(my_word == "exit()"):
        break
    print("Слово", "'"+ my_word+"'", "встретилось", counts[my_word], "раз(а)")