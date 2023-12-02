# just code for Hunting searches
def hunting_search_Kirde(list,key):
    high = max = len(list)-1
    low = 0
    count = 0
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
    return count
#######################################################################
// a better version of that one higher, actually I've just removed unnecessary things and etc
def hunting_search_Kirde_mod(list,key):
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
    return count,n 
########################################################################################
// this is another variety of hunter search made by me, idk about it's perfomance but we've got here less lines of code
def girl_hunter_ver2(list,key):
    low = count = i = 0 
    gran = len(list)-1
    pov = False
    while key in list:
        try:
            if list[gran] == key:
                list.pop(gran)
                count += 1 
                gran = len(list)-1
            while (list[gran] > key and pov == False) or (list[gran] < key and pov == True):
                if pov == True:
                    gran = -gran
                if list[gran] == key:
                    count += 1
                    list.pop(gran)
                    gran = len(list)-1
                else:
                    i += 1 
                    if gran-2**i < low:
                        i = 0
                    gran = abs(gran-2**i)
                    i += 1 
            else:
                pov = not pov
        except IndexError:
            pass
    return count
###########################################################################################################
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
                    mid = (low+high)//2
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
                    continue
                    #index = low + int(((high - low) * (key - list[low])) / (list[high] - list[low]))
                elif list[index] < key:
                    low = index + 1
                else:
                    high = index - 1
            else:
                flag = False
        except IndexError:
            flag = False
    return count
