#1

s = input('Введите строку, содержащую букву н\n')
l = []
count = 0
nmax = 0
for i in range(len(s)):
    l.append(s[i])
    if l[i] == 'н':
        count += 1
        l[i] = '!'
    else:
        if nmax < count:
            nmax = count
        count = 0
s = s.replace('н'*nmax,'!'*nmax)
print(f'Количество подряд идущих n = {nmax} \n{s}')  

#2

s = input('Введите строку символов со скобками\n')
l = []
st = 0
nd = 9999999999
for i in range(len(s)):
    l.append(s[i])
    if (l[i] == '(' or l[i] == '{' or l[i] == '[') and i > st:
        st = i
    elif (l[i] == ')' or l[i] == '}' or l[i] == ']') and i < nd:
        nd = i
for p in range(st + 1, nd):
    print(s[p], end = '')

#3

s = input('Введите любую строку\n')
s.lower()
l = s.split()
for i in range(len(l)):
    rng = len(l[i])
    if l[i][0] == 'а' and l[i][rng - 1] == 'я':
        print(l[i])





#trash
'''
if i > 0 and l[i-1] == '!':
            if nmax < count:
                nmax = count
        else:
            if nmax < count:
                nmax = count
            count = 1 
'''