import random, time, re
# ВСЕГО 12 ПОИСКОВ
# Кол-ва циклов не добавлял сюда (исключение мои основные поиски), только счетчик, тут скорее упор на все поиски и время выполнения

def foo(Danik):
    d = {}
    for i,k in enumerate(set(Danik)):  
        arg = i+1
        d[k] = int(f'{arg}')
    return d

def marina_func(list,key,arg):
    count = n = 0
    for i in range(len(list)):
        n += 1
        if list[i] == key: 
            count += 1
            continue          
    if arg == 2:
        for i in range(count-1):
            list.remove(key)
    return count,n

def bruteforce(list,key,arg):
    count = n = 0 
    for i in range(len(list)):
        n += 1
        if list[i] == key:
            count += 1
    if arg == 2:
        for i in range(count-1):
            list.remove(key)
    return count,n

##########################################################################
# Далее пойдут все мои следящие поиски, раздал одногруппникам, признаюсь #
##########################################################################
# 8 вариаций бтв, тут исследовал больше, чем мои поиски. Можно сказать, что они все похожи, но отнюдь. Самые первые версии были не по алгоритму Крючкова, пришлось перестраивать - а это уже совсем иная работа кода и так далее

# первый не работает проперли для 2 задания, не фиксил.

def hunting_search_Pirill_Kolyakov(list,key,arg):
    high = max = len(list)-1 # задача границ, как и в почти каждом другом поиске
    low = n = 0
    count = 0 # будущий счетчик на сравнения в цикле, пока он возвращает ноль
    flag = True # приходится делать флаг для множественного разворота, если интересно
    # как это работает - когда элемента не будет в массиве, по индексам мы улетаем в минус, там цикл флага и завершится
    # не самом деле трудно было привязать что-то такое нормально, все время не получалось
    while flag == True:
        try: # о чем речь шла выше, except там на ошибку с индексами и даст фолс на флаг
            while low <= high: # условие из алгоритма Крючкова как минимум (хотя в его алгоритме куча ошибок и об многом не сказано)
                n +=1 
                if list[high] == key: # это своего рода моя доработка алгоритма, об этом позже
                    count +=1 # вообще эта проверка присутствует и в алгоритме Крючкова, но она подразумевается там как единственная
                    # а я вшил в алгоритм, ну тут нюансы с заданными мною границами и тд, может быть еще дальше напишу
                    list.pop(high) # ну и как обычно приходится удалять элементы, чтобы вообще что-то работало
                    low = 0 # ну и очевидно, что после удаления элемента, нужно снова задать границы
                    #high = len(list)-1
                    continue # брейк сделан по большец части для перезапуска цикла, чтобы он нормально искал самые большие элементы
                i =0 # шаг слежения самый первый
                while key < list[high]: # слежение влево по алгоритму
                    high -= 2**i # уменьшение границы по алгоритму
                    i += 1 # ну и увеличиваем шаг
                    if high-2**i <= low: # outstanding move выше, так как я увеличил i именно в той позиции, теперь можно предсказать 
                    # следующий цикл, будет ли там превышение шага. если будет - обнуляем i. Возможна доработка в виде уменьшения i на 1, 
                    # а не обнулять, но не знаю, это во-1 надо тестировать, хоть и несложно, но вообще вся эта тема с проверкой границы сделана чисто для поиска самых маленьких чисел массива
                    # поэтому там можно и по 1 шагать (с i=0)
                        i = 0
                    if list[high] == key: # нахождение элемента слежением влево
                        count +=1
                        list.pop(high) # уже расписано
                        #low = 0
                        high = len(list)-1
                else: # если выходит из вайла, срабатывает этот елсе
                    low = list.index(list[high])+1 # тут у крючкова, как я понял, нижняя задается без +1, но я не вижу в этом смысла
                    # элемент без +1 мы уже проверили, потому это чисто моя наработка. на самом деле, если вы мне не верите, можете +1 убрать =(
                if list[low] == key: # из-за доработки моей на +1 делаем ветвление новое, которого в алгоритме Крючкова нет
                # ну вообще мы просто каждый раз экономим так сравнения в циклах и вообще границы меньше будут. О - оптимизация
                    count +=1
                    list.pop(low) # тут все описано снова выше про границы и поп, эти действия приходится повторять везде, хавает время офк, но не так много хотя бы (в моем интерполяционном все хуже с этим)
                    # вообще следящий в плане границ умничка, могу так сказать. Назову следящий поиск - невесткой (сначала была дочь, но тут связи чет не очень выстраиваются). Бинарный будет сынком. Их дитя будет совершенным, могу так сказать
                    #low = 0
                    high = len(list)-1
                    continue
                i = 0 # ну тут повторение всего выше с следящим влево, только теперь вправо
                while key > list[low]:
                    low += 2**i
                    i += 1
                    if high <= low + 2**i: # это вообще никогда не выстрелит вроде как, сделано на всякий случай. Ну и можно же все поменять и начинать с самого маленького массива, тогда будет актуально.
                        i = 0
                    if key == list[low]:
                        count +=1
                        list.pop(low)
                        #low = 0
                        high = len(list)-1
                        #break
                else:
                    high = list.index(list[low])-1 # тоже доработка границы с -1. тут потом цикл заканчивается и это граница (новая между прочим, не как у крюка!!!) может сразу выстрелить в самое первое условие. ну как вам? все продумано
            else:
                break # на цикл флага, правда я забыл проверить этот елсе
        except IndexError:
            flag = False # ну тут уже в начале писал
    if arg == 2:
        list.append(key)
        list.sort
    return count,n # тут еще нужно возвращать будет сравнения, а сравнения я пока не подумал, куда пихать
# ну если давать саммари: мне кажется алгоритм выглядит мб легким, но я потратил около дня на проработку и фиксинг багов, в целом тяжело было все склеить воедино
# по итогам замеров оказалось, что невестка чуть тупит, ну ладно, главное, чтобы бинарный сын был счастлив, внук правда его не обгоняет, но "мать" он улучшает в разы (раз 20?)



def hunting_search_mod(list,key,arg):
    high = max = len(list)-1 
    low = n = i = 0
    count = 0 
    flag = True 
    while high > low:
        try:
            n +=1  # придется пихать в места внутренних вайлов и в ветвление
            i = 0
            if list[high] == key:
                count +=1 
                list.pop(high) 
                high = len(list)-1 # какая граница работает, такая и перезадается
                continue
            while key < list[high]: 
                high -= 2**i 
                i += 1 
                if high-2**i <= low: 
                    i = 0
                if list[high] == key: 
                    count +=1
                    list.pop(high)
                    high = len(list)-1
            else: 
                low = list.index(list[high])
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
            else:
                high = list.index(list[low])
        except IndexError:
            flag = False
    if arg == 2:
        list.append(key)
        list.sort()
    return count,n

def hunting_binary_search(list,key,arg):
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
    if arg == 2:
        list.append(key)
        list.sort()
    return count,n

def hunting_interpolation_search(list, key,arg):
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
    if arg == 2:
        list.append(key)
        list.sort()
    return count,n

def girl_hunter_V1(list,key,arg): # есть еще две версии (вторая тупенькая, а третья слишком заумная по моим идеям), ну а вообще сначала это писалось Данияру, но он отказался сам (потом был разворот на 180)
    high = len(list)-1 
    low = i = count = temp = n = 0 
    flag = True  ############## РАБОТАЕТ ПРОФЕССИОНАЛ !!!!!!!!!!!!!!!!!!!!!!!!!!
    while high != low:
        if list[high] == key:
            count +=1 
            list.pop(high) 
            low = 0
            high = len(list)-1 # границы переопределяем те, с которыми работаем
            continue
        while key < list[high] and low != high: # у меня как всегда был долгий процесс дебага и условие с and добавилось, а там еще ниже есть if high == low, я хз почему, но если что-то одно убираю - уже не работает, хотя они делают одно и то же
            high -= 2**i # бтв V3 может работать на одном вайле, это круто, но тут не так, смена на иф уже ломает
            i += 1 
            temp = i-1
            if high-2**i <= low: 
                i = 0
            if list[high] == key: 
                count +=1
                list.pop(high)
                high = len(list)-1
                low = 0 
            if high == low:
                break
        else: 
            i = 0
            low = list.index(list[high]) # как раз границы по алгоритму ставим
            if high+2**temp > len(list)-1 :
                break # проверяем на IndexError
            else:
                high += 2**temp
        while key > list[low] and low != high:
            low += 2**i
            i += 1
            temp = i-1
            if high <= low + 2**i:  
                i = 0
            if key == list[low]:
                count += 1
                list.pop(low)
                low = 0
            if high == low:
                break
        else:
            i = 0
            high = list.index(list[low])
            if low-2**temp < 0: # что и выше, это проверка, но конкретно эта НИКОГДА не выстрелит. Я гарантирую. PS я обманул, кстати. Ну значит береженного код бережет, что я еще могу сказать
                break
            else:
                low -= 2**temp
    if arg == 2:
        list.append(key)
        list.sort()
    return count,n

def girl_hunter_V2(list,key,arg):
    gran = count = i = 0 
    razd = len(list)-1 # n мне лень считать
    pov = False
    while key in list:
        try:
            if list[razd] == key:
                list.pop(razd)
                count += 1 
                razd = len(list)-1
            while (list[razd] > key and pov == False) or (list[razd] < key and pov == True):
                if pov == True:
                    razd = -razd
                if list[razd] == key:
                    count += 1
                    list.pop(razd)
                    razd = len(list)-1
                else:
                    i += 1 
                    if razd-2**i < gran:
                        i = 0
                    razd = abs(razd-2**i)
                    i += 1 
            else:
                pov = not pov
        except IndexError:
            flag = False
    n = 0
    if arg == 2:
        list.append(key)
        list.sort()
    return count,n

def girl_hunter_V3(list,key,arg):
    gran = count = i = 0 
    razd = len(list)-1
    pov = False
    flag = True
    temp = n = 0
    while razd != gran: # венец моего творения, лучшая моя версия, хоть и не такая любимая, как первая. Но из линейки герл хантеров - V3 на первом месте в сердце
        if list[razd] == key: # условие по алгоритму
            list.pop(razd)
            count += 1 
            razd = len(list)-1
            continue
        while (list[razd] > key and pov == False) or (list[razd] < key and pov == True): # тут можно иф, кстати, но тогда верхний цикл будет перезапускаться чаще, тут как вы хотите
            if pov == True:
                razd = -razd
            else:
                razd = abs(razd)
            razd = abs(razd-2**i)
            i += 1
            temp = i - 1
            if razd-2**i <= gran or (pov == True and abs(razd-2**i) >= gran):
                i = 0
            if list[razd] == key:
                count += 1
                list.pop(razd)
                razd = len(list)-1
                gran = 0
                pov = False
            if razd == gran:
                break
        else:
            if abs(-razd-2**temp) > len(list)-1: # outstanding move опять, отсылочка, да?
                break
            else: # Прооооооооооооооооверка на вылет, кстати, в других версиях я еще лоу проверял на уход за ноль, но вообще такого никогда не произойдет, поэтому тут только как бы хай смотрим. Ну работает и ладно, но за лоу тоже вылет регистрирует в другом коде! Но такого просто не будет, поверьте
                gran = abs(-razd-2**temp)
            i = 0
            pov = not pov
    if arg == 2:
        list.append(key)
        list.sort()
    return count,n

def girl_binarynunter_V4(list,key,arg): # for Tagir
    high = len(list)-1
    low = n = count = i = temp = 0
    while low <= high:
        n += 1
        if list[high] == key:
            count +=1
            list.pop(high)
            high = len(list)-1
            continue
        while key < list[high]:
            n += 1
            high -= 2**i
            i += 1
            temp = i-1
            if high-2**i <= low:
                i = 0
            if list[high] == key:
                count +=1
                list.pop(high)
                high = len(list)-1
            if high <= low:
                break
        else:
            low = high 
            if high+2**temp > len(list)-1:
                break 
            else:
                high += 2**temp
        while low <= high: 
            n += 1
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
    if arg == 2:
        list.append(key)
        list.sort()
    return count,n

########################################################

def interpolation(arr, key,arg): 
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
    if arg == 2:
        arr.append(key)
        arr.sort()
    return count,n

def binary_search(list, key,arg):
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
    if arg == 2:
        list.append(key)
        list.sort()
    return count,n

#######################################################

with open('article.txt',encoding="utf-8" ) as space: 
    Billy = space.read()
Billy = re.sub(r'[\W]|[a-zA-Z0-9_]' ,' ',Billy)
Billy = re.sub(r'\b\w{1,3}\b', ' ', Billy); #удаление слов из 3 букв, обычно это предлоги и всякие незначительные слова
Billy = Billy.lower()
f = {}
BruhX = []
PinCode = Billy.split()
d = foo(PinCode)
for i in PinCode:
    BruhX.append(d.get(i))
    f[d.get(i)] = i
BruhX.sort()
IamOnlyMortal = []
Death = list(set(BruhX))
IamOnlyMortal = [Death[random.randint(0,len(Death)-1)] for i in range(100000)]
IamOnlyMortal.sort()

def Depression(Hope): # для задания два на уникальные ключи   
    YY = []
    for i in Hope:
        YY.append(f.get(i))
    return YY

def answer(func,Bibi,arg):
    Copiya = tuple(Bibi)
    Bibi = list(Copiya)
    st1 = time.time() # выше просто по факту задаем переменные, потому отчет начнем отсюда
    for i in set(Bibi):
        st = time.time() # тут отсчет каждый раз новый, потом разница будет настолько малая, что питон округляет до нуля, из-за этого проблема в отображении времени
        if arg == 1:
            Copatich = list(Copiya)
        else:
            Copatich = Bibi
        answer,comp = func(Copatich,i,arg)
        time.sleep(1*10**(-1000))
    Sovunia = time.time()-st1
    if arg == 2:
        Marusya = Depression(Copatich)
        print('Ответ для задания 2 - уникальные вхождения таковы: ',Marusya,' , количество уникальных ключей - ',len(Marusya))
    print('\n','Отображение результатов задания ',arg,'\n')
    print(func,'Время выполнения программы: ', Sovunia,'\n','--'*45,'\n'*3)
    
all_searches = [hunting_search_Pirill_Kolyakov,bruteforce,marina_func,hunting_search_mod, hunting_binary_search,hunting_interpolation_search,girl_hunter_V1,girl_hunter_V2,girl_hunter_V3,interpolation,binary_search,girl_binarynunter_V4]
for i in all_searches:
    answer(i,BruhX,1)
    answer(i,IamOnlyMortal,2)
