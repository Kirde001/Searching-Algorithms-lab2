import random
kk = open ("text.txt",'w+')
a = []
while len(a) < 2500:
    korneev = (random.randint(-10000,10000))
    if len(a) < 2499:
        if korneev not in a:
            a.append(korneev)
            kk.write(str(korneev)+'\n')
    else:
        if korneev not in a:
            a.append(korneev)
            kk.write(str(korneev))
kk.close()
print('Файл создан')
