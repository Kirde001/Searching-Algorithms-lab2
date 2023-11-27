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
