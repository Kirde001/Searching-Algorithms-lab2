import random, time, string
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import pandas as pd # для другой машинки нужно еще python -m pip install xlsxwriter, xlwt
d = {
    'а': 100, # почти нереально, чтобы он на буквы выстрелил, но на всякий случай тут будут значения такие, чтобы другие буквы не получались (я про то, что две буквы а, к примеру, то есть 1 и 1 могли дать букву к - 11)
    'б': 200, 
    'в': 300,
    'г': 40,
    'д': 50,
    'е': 60,
    'ж': 70,
    'з': 80,
    'и': 90,
    'й': 10,
    'к': 11,
    'л': 12,
    'м': 13,
    'н': 14,
    'о': 15,
    'п': 16,
    'р': 17, 
    'с': 18,
    'т': 19,
    'у': 20,
    'ф': 21,
    'х': 22,
    'ц': 23,
    'ч': 24,
    'ш': 25,
    'щ': 26,
    'ъ': 27,
    'ы': 28,
    'ь': 29,
    'э': 30,
    'ю': 31,
    'я': 32,
    'ё': 33,
}
def Interpolation(arr, key, arr2): 
    low = count = comp = 0
    high = len(arr) - 1
    while low <= high and key >= arr[low] and key <= arr[high]:
        comp += 1
        index = low + int(((high - low) * (key - arr[low])) // (arr[high] - arr[low]))
        if arr[index] == key:
            count += 1   
            arr.pop(index)
            # попробую объяснить, зачем вообще тут попать: вся беда в том, что если оставить базовый алгоритм, то считать он будет верно только с одной остортированной стороны, я проверял. С той стороны,
            # которая записана в else, то есть в моем случае в правую сторону, будет верно, а в во втором условии elif(в начальном алгоритме это был if и он, понятно, потому и не работал бы, потому что
            # запускался бы параллельно с основным условием и все ломал. Если просто бездумно дописать elif, то тоже не работало бы). Можно легко проверить комментом того, что ниже
            # каунта в условии и еще убрать приставку el в elif. Костыли какие-то приходится приделывать, если короче. Для сравнения базовый алгоритм можно глянуть на любом сайте, там в основном на втором условии if стоит. Ну для
            # нахождения числа одного нормально, но для подсчета приходится изворачиваться как я. Просто второй if двигает сами индексы, но нам при подсчете это не всегда нужно, такой прикол. Коммент вышел большим, его вообще
            # прочитают???
            low = 0
            high = len(arr) - 1
        elif arr[index] < key:
            low = index + 1
        else:
            high = index - 1
    else:
        arr2.append(p.get(key))
    return count, comp
def Binary_search(list, key, arr2):
    st = time.time()
    low = count = comp = 0
    high = len(list) - 1
    while low <= high:
        comp += 1
        mid = (low + high)// 2 
        if list[mid] == key:
            count += 1
            list.pop(mid)
            low = 0
            high = len(list)-1
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    else:
        arr2.append(p.get(key))
    return count,comp
def Lucifer(Billy):
    Billy = Billy.lower()
    for GetTheHellOutOfHear in Billy:
        if GetTheHellOutOfHear in (string.punctuation + string.ascii_letters + string.digits+'"”“-–«»…'): #как бы ни показалось странным, это два разных тире
            Billy = Billy.replace(GetTheHellOutOfHear,"")
        elif GetTheHellOutOfHear == 'ё':
            Billy = Billy.replace(GetTheHellOutOfHear,"e")
    PinCode = Billy.split()
    PinCodeIsDead = tuple(PinCode)
    for i in PinCodeIsDead:
        if len(i) < 4:
            PinCode.pop(PinCode.index(i))
    PinCode.sort()
    return PinCode
with open('FINarticle.txt',encoding="utf-8" ) as space: 
    Billy = space.read()
PinCode = Lucifer(Billy)
IamOnlyMortal = []
Death = list(set(PinCode))
while len(IamOnlyMortal) < 10000:
    IamOnlyMortal.append(Death[random.randint(0,len(Death)-1)])
def theonlyway(start): 
    string = ''
    word = list(start)
    for i in range(0,len(word)):
        string += str(d.get(word[i]))
    return string
p = {}
def DigitalWorld(TheOnlyThingIKnowForReal):
    Copatich = []
    for i in TheOnlyThingIKnowForReal:# делаем массив из полученных чисел и потом сортим его, вообще по факту там уже будет другая сортировка по числам, отличная от строк, но кому не все равно? метод сортировки в задании не обсуждается
        Copatich.append(int(theonlyway(i)))
        p[int(theonlyway(i))] = i
    Copatich.sort()
    b = tuple(Copatich)
    return b
def plot(x,y):
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_title("График зависимости частоты появления от ключа")
    ax.set_xlabel('Ключ - номер')
    ax.set_ylabel('Частота появления')
    plt.show()
def answer(func,Bibi,arg,mod):
    arr2 = []
    df = pd.DataFrame({'Ключ': [],
    'Частота появления': [],
    'Количество сравнений':[],
    'Время поиска': []})
    stroka = 'Задание ' + str(mod)+'.'+str(arg)
    writer = pd.ExcelWriter(f'{stroka}.xlsx', engine='xlsxwriter')
    tab = PrettyTable()
    tab.field_names = ['Номер в списке','Найденное слово','Частота появления в тексте','Количество сравнений','Время работы']
    t = 1
    x = []
    y = []
    st1 = time.time() # выше просто по факту задаем переменные, потому отчет начнем отсюда
    CarCarich = DigitalWorld(Bibi)
    for i in set(PinCode):
        st = time.time() # тут отсчет каждый раз новый, потом разница будет настолько малая, что питон округляет до нуля, из-за этого проблема в отображении времени
        Copatich = list(CarCarich)
        value = int(theonlyway(i))
        answer,comp = func(Copatich,value,arr2)  
        tab.add_row([t,p.get(value),answer,comp,time.time()-st])
        df2 = pd.DataFrame({'Ключ': [p.get(value)],
        'Частота появления': [answer],  
        'Количество сравнений':[comp],
        'Время поиска': [time.time()-st]})
        df = df._append(df2,ignore_index = True)
        x.append(t)
        y.append(answer)
        t +=1
    Sovunia = time.time()-st1
    df = df.sort_values(by = 'Частота появления', ascending=False)
    df.to_excel(writer, sheet_name='Задание')
    writer._save()
    tab.sortby='Частота появления в тексте'
    tab.reversesort = True
    print('\n','Отображение результатов задания ',arg,'\n')
    print(df)
    print(tab)
    print(func,'Время выполнения программы: ', Sovunia)
    print('Уникальные вхождения таковы: ',set(arr2),'\n','--'*45)
    plot(x,y)
all_searches = [Binary_search, Interpolation]
mod = 0
for i in all_searches:
    mod +=1
    answer(i,PinCode,1,mod)
    answer(i,IamOnlyMortal,2,mod)
