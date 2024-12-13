import os
#1
'''
def read_last(lines, file):
    l = []
    for i in file:
        l.append(i)
    for i in range(lines):
        if i == 0:
            print(l[len(l) - 1 - i])
        else:
            print(l[len(l) - 1 - i], end = '')

linenum = input('Введите количество строчек, которые необходимо вывести с конца\n')
while(not(linenum.isdigit())):
    linenum = input('Вы ввели не число!\nПовторите попытку')
linenum = int(linenum)

f = open(r'article.txt')
read_last(linenum, f)

#2

def print_docs(directory):
    print(f'{directory}:')
    l = os.listdir(directory)
    for i in range(len(l)):
        print(l[i])
        if l[i].find('.') == -1:
            directory = directory + '/' + l[i]
            print_docs(directory)
print_docs('DirectoryForTask')

#3

def longest_words(file):
    maxlen = 0
    l = []
    lmaxes = []
    count = 0
    f = open(file)
    for i in f:
        lhelp = []
        l.append(i.split())   
    for i in range(len(l)):
        for j in range(len(l[i])):
            if len(l[i][j]) > maxlen: 
                maxlen = len(l[i][j])
    for i in range(len(l)):
        for j in range(len(l[i])):
            if len(l[i][j]) == maxlen: 
                lmaxes.append(l[i][j])
    print(f'Максимальная длина слова - {maxlen}\nЭти слова:\n{lmaxes}')
longest_words('article.txt')
'''
#4
name = input('Введите имя будущего текстового файла\n')
filename = name + '.txt'
f = open(filename, 'w')
b = input('Введите текст, который хотите поместить в текстовый файл\nДля завершения введите точку\n')
while (b != '.'):
    f.write(b + '\n')
    b = input()

