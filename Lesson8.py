import re
"""
st = input('Введите строки на нахождение в них номерных знаков РФ\n')
st = st.upper()
taxi = re.findall(r"[АВЕКМНОРСТУХ]{1,2}[0-9]{5,6}", st)
usual = re.findall(r"[АВЕКМНОРСТУХ]{1,2}[0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}", st)
print(f'Все номера такси:\n{taxi}')
print(f'Все номера обычных автомобилей\n{usual}')


#2
l = []
f = open(r"fileforeight.txt")
for i in f:
    words = re.findall(r"\b[a-zA-ZА-Яа-яёЁ]+[-]{0,1}[a-zA-ZА-Яа-яёЁ]+\b", i)
print(f'Количество слов в файле - {len(words)}')
"""
#3

l = []
f = open(r"fileforeight2.txt")
for i in f:
    time = re.findall(r"[0-2]{0,1}[0-9][:]{1}[0-5]{0,1}[0-9][:]{1}[0-5]{0,1}[0-9]", i)
for j in range(len(time)):
    l = time[j].split(":")
    print(f'Уважаемые! Если вы к {l[0]}:{l[1]}:{l[2]} не вернёте чемодан, то уже в {l[0]}:{l[1]}:{int(l[2]) + 1} я за себя не отвечаю.')