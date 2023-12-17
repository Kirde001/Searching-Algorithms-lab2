# just code for Hunting searches
def hunting_search_Kirde(list,key): # Father of all hunter based searches or the first one that i made
    high = len(list)-1
    low = 0
    count = 0
    flag = True
    while flag == True:
        try:
            while low <= high:
                if list[high] == key:
                    count +=1
                    list.pop(high)
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
                        high = len(list)-1
                else:
                    low = list.index(list[high])+1
                if list[low] == key:
                    count +=1
                    list.pop(low)
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
                        high = len(list)-1
                        break
                else:
                    high = list.index(list[low])-1
            else:
                break
        except IndexError:
            flag = False
    return count
#######################################################################
// a better version of that one higher, actually I've just removed unnecessary things and etc

def hunting_search_mod(list,key): # Simb
    high = len(list)-1 
    low = i = 0
    count = 0 
    flag = True 
    while high > low:
        try:
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
                    high -= 1
            else:
                high = list.index(list[low])
        except IndexError:
            flag = False
    return count

def hunting_binary_search(list,key): # Galya?
    high = len(list)-1
    low = count = 0
    flag = True
    while flag == True:
        try:
            if list[high] == key:
                count +=1
                list.pop(high)
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
                    high = len(list)-1
            else:
                low = high 
                high += 2**b 
            while low <= high: 
                mid = (low + high)// 2 
                if list[mid] == key:
                    count += 1
                    list.pop(mid)
                    high = len(list)-1
                elif list[mid] < key:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                flag = False
        except IndexError:
            flag = False
    return count

def hunting_interpolation_search(list, key):
    high = len(list)-1
    low = count = 0
    flag = True
    while flag == True:
        try:
            if list[high] == key:
                count +=1
                list.pop(high)
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
                    high = len(list)-1
            else:
                low = high 
                high += 2**b
            while low <= high and key >= list[low] and key <= list[high]:
                index = low + int(((high - low) * (key - list[low])) / (list[high] - list[low]))
                if list[index] == key:
                    count += 1   
                    list.pop(index)  
                    high = len(list) - 1
                elif list[index] < key:
                    low = index + 1
                else:
                    high = index - 1
            else:
                flag = False
        except IndexError:
            flag = False
    return count

def girl_hunter_V1(list,key): # Mary
    # есть еще две версии (вторая тупенькая, а третья слишком заумная по моим идеям), ну а вообще сначала это писалось Данияру, но он отказался сам (потом был разворот на 180)
    high = len(list)-1 
    low = i = count = temp = 0 
    flag = True  ############## РАБОТАЕТ ПРОФЕССИОНАЛ !!!!!!!!!!!!!!!!!!!!!!!!!!
    while high != low:
        if list[high] == key:
            count +=1 
            list.pop(high) 
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
            if high == low:
                break
        else:
            i = 0
            high = list.index(list[low])
            if low-2**temp < 0: # что и выше, это проверка, но конкретно эта НИКОГДА не выстрелит. Я гарантирую. PS я обманул, кстати. Ну значит береженного код бережет, что я еще могу сказать
                break
            else:
                low -= 2**temp
    return count,

def girl_hunter_V2(list,key): # Неудачная версия с key in list, так же нельзя вроде, демка для 3 версии герлхантера
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
    return count

def girl_hunter_V3(list,key): # For Dani Sabirov
    gran = count = i = 0 
    razd = len(list)-1
    pov = False
    flag = True
    temp = 0
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
                pov = False
            if razd == gran:
                break
        else:
            if abs(-razd-2**temp) > len(list)-1:
                break
            else: # Прооооооооооооооооверка на вылет, кстати, в других версиях я еще лоу проверял на уход за ноль, но вообще такого никогда не произойдет, поэтому тут только как бы хай смотрим. Ну работает и ладно, но за лоу тоже вылет регистрирует в другом коде! Но такого просто не будет, поверьте
                gran = abs(-razd-2**temp)
            i = 0
            pov = not pov
    return count

def girl_binarynunter_V4(list,key): # for Tagir Abdullin
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
    return count,n
