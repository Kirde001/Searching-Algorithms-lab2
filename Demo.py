import random, time, string
from prettytable import PrettyTable
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
def lin_func(list,key):
    count = n = 0
    for i in range(len(list)):
        n += 1
        if list[i] == key: # ну, по алгоритму попаем и брейкаем
            count += 1
            list.pop(i)
            break
    return count,n 
def bruteforce(list,key):
    count = n = 0 
    for i in range(len(list)):
        n += 1
        if list[i] == key:
            count += 1
    return count,n
def hunting_search_Pirill_Kolyakov(list,key):
    high = len(list)-1
    low = n = count = 0
    flag = True
    while flag == True:
        try:
            while low <= high:
                if list[high] == key:
                    count +=1
                    list.pop(high)
                    low = 0
                    high = len(list)-1
                    break
                i =0
                while key < list[high]:
                    high -= 2**i
                    i += 1
                    if high-2**i <= low:
                        i = 0
                    if list[high] == key:
                        count +=1
                        list.pop(high)
                        low = 0
                        high = len(list)-1
                else:
                    low = list.index(list[high])+1
                if list[low] == key:
                    count +=1
                    list.pop(low)
                    low = 0
                    high = len(list)-1
                i = 0
                while key > list[low]:
                    low += 2**i
                    i += 1
                    if high <= low + 2**i:
                        i = 0
                    if key == list[low]:
                        count +=1
                        list.pop(low)
                        low = 0
                        high = len(list)-1
                        break
                else:
                    high = list.index(list[low])-1
            else:
                break
        except IndexError:
            flag = False
    return count,n
def hunting_binary_search_Kirde(list,key):
    high = len(list)-1
    low = n = count = 0
    flag = True
    while flag == True:
        try:
            if list[high] == key:
                count +=1
                list.pop(high)
                low = 0
                high = len(list)-1
            i =0
            b = 0
            while key < list[high]:
                high -= 2**i
                b = i
                i += 1
                if high-2**i <= low:
                    i = 0
                if list[high] == key:
                    count +=1
                    list.pop(high)
                    low = 0
                    high = len(list)-1
            else:
                low = high 
                high += 2**b
            if key == 2:
                print(high,low)  
            while low <= high: 
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
                flag = False
        except IndexError:
            flag = False
    return count,n
def hunting_interpolation_search_Kirde(list, key):
    high = len(list)-1
    low = n = count = 0
    flag = True
    while flag == True:
        try:
            if list[high] == key:
                count +=1
                list.pop(high)
                low = 0
                high = len(list)-1
                continue
            i =0
            b = 0
            while key < list[high]:
                high -= 2**i
                b = i
                i += 1
                if high-2**i <= low:
                    i = 0
                if list[high] == key:
                    count +=1
                    list.pop(high)
                    low = 0
                    high = len(list)-1
            else:
                low = high 
                high += 2**b
            while low <= high and key >= list[low] and key <= list[high]:
                index = low + int(((high - low) * (key - list[low])) / (list[high] - list[low]))
                if list[index] == key:
                    count += 1   
                    list.pop(index)  
                    low = 0
                    high = len(list) - 1
                elif list[index] < key:
                    low = index + 1
                else:
                    high = index - 1
            else:
                flag = False
        except IndexError:
            flag = False
    return count,n
def interpolation(arr, key): 
    low = count = n = 0
    high = len(arr) - 1
    while low <= high and key >= arr[low] and key <= arr[high]:
        n += 1
        index = low + int(((high - low) * (key - arr[low])) / (arr[high] - arr[low]))
        if arr[index] == key:
            count += 1   
            arr.pop(index)  
            low = 0
            high = len(arr) - 1
        elif arr[index] < key:
            low = index + 1
        else:
            high = index - 1
    return count,n
def binary_search(list, key):
    st = time.time()
    low = count = n = 0
    high = len(list) - 1
    while low <= high:
        n += 1
        mid = (low + high)// 2
        if list[mid] == key:
            count += 1
            list.pop(mid)
            low = 0
            high = len(list)-1
        elif list[mid] < key:
            low = mid + 1;
        else:
            high = mid - 1
    return count,n
def Lucifer(Billy):
    Billy = Billy.lower()
    for GetTheHellOutOfHear in Billy:
        if GetTheHellOutOfHear in (string.punctuation + string.ascii_letters + string.digits+'"'+'”'+'“'+'-'+'–'+'«»…'): #как бы ни показалось странным, это два разных тире, кавычки тоже разные
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
def answer(func,Bibi,arg):
    comp = 0
    tab = PrettyTable()
    tab.field_names = ['Номер в списке','Найденное слово','Частота появления в тексте','Количество сравнений','Время работы']
    t = 1
    CarCarich = DigitalWorld(Bibi)
    st = time.time() # будем считать время отсюда, так как выше по факту просто задаем значения
    for i in set(PinCode):
        Copatich = list(CarCarich)
        value = int(theonlyway(i))
        answer,comp = func(Copatich,value)
        tab.add_row([t,p.get(value),answer,comp,time.time()-st])
        t += 1
    Sovunia = time.time()-st
    tab.sortby='Частота появления в тексте'
    tab.reversesort = True
    print('\n','Отображение результатов задания ',arg,'\n')
    print(tab)
    print(func,'Время выполнения программы поиска: ', Sovunia ,'\n','--'*43)
all_searches = [bruteforce,lin_func,binary_search,interpolation,hunting_search_Pirill_Kolyakov,hunting_binary_search_Kirde,hunting_interpolation_search_Kirde]
for i in all_searches:
    answer(i,PinCode,1)
    answer(i,IamOnlyMortal,2)
