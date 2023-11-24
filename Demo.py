import random, time, string
d = {
    'а': 1,
    'б': 2,
    'в': 3,
    'г': 4,
    'д': 5,
    'е': 6,
    'ж': 7,
    'з': 8,
    'и': 9,
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
}
def Interpolation(arr, key): # лютая функция поиска, причем тут даже ничего менять не надо в плане алгоритма, для бинарки можно такой же код написать, хотя мб оставлю два разных способа
    low = count = 0
    high = len(arr) - 1
    while low <= high and key >= arr[low] and key <= arr[high]:
        index = low + int(((high - low) * (key - arr[low])) / (arr[high] - arr[low]))
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
            index = low + int(((high - low) * (key - arr[low])) / (arr[high] - arr[low]))
        if arr[index] < key:
            low = index + 1;
        else:
            high = index - 1;
    return count
def binary_search(list, key):
    st = time.time()
    low = count = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)// 2 
        if list[mid] == key:
            count += 1
            list.pop(mid)
            low = 0
            high = len(list)-1
            mid = (low+high)//2
        elif list[mid] < key:
            low = mid + 1;
        else:
            high = mid - 1
    return count
with open('article.txt',encoding="utf-8" ) as space:
    Billy = space.readline()
DieVermin = str.maketrans('','',string.punctuation) #группируем все ненужные знаки препинания - пока неидеальный текстовый редактор, ну, какой есть
Bruh = Billy.translate(DieVermin) # как бы замена знаков препинания из "словаря" выше, хотя мы просто тут удаляем, правда тире тоже удаляется =(
BruhX2 = Bruh.lower()
PinCode = BruhX2.split( )
PinCode.sort()
def theonlyway(start): # с помощью великого русскогот алфавита превращаем тарабарщину в циферки и кайфуем от поиска по нормальным значениям
    string = ''
    word = list(start)
    for i in range(0,len(word)):
        string += str(d.get(word[i]))
    return string
Copatich = []
p = {}
for i in PinCode: #Bibi: # делаем массив из полученных чисел и потом сортим его, вообще по факту там уже будет другая сортировка по числам, отличная от строк, но кому не все равно? метод сортировки в задании не обсуждается
    Copatich.append(int(theonlyway(i)))
    p[int(theonlyway(i))] = i
Copatich.sort()
b = tuple(Copatich)
def answer(func):
    st = time.time()
    t = 1
    for i in set(PinCode):
        Copatich = list(b)
        value = int(theonlyway(i))
        answer = func(Copatich,value)
        print(t,'number? muerdo epta -',p.get(value),'-----',answer)
        t += 1
    print(func,'Время выполнения поиска: ', time.time()-st)
answer(binary_search)
answer(Interpolation)
