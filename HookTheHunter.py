import random
a = []
while len(a) < 10:
    a.append(random.randint(1,5))
a.sort()
print(a)
b = tuple(a)
def hunting_search_Kirde(list,key):
    high = max = len(list)-1
    low = 0
    count = 0
    flag = True
    while flag == True:
        try:
            while low <= high:
                if list[high] == key:
                    print('high - ',high,' - low - ',low, 'элемент найден с хая')
                    count +=1
                    list.pop(high)
                    low = 0
                    high = len(list)-1
                    print('HHHHHHHHHHH')
                    break
                i =0
                while key < list[high]:
                    #print(list[high],'-  индекс - ',list.index(list[high]),'- нынешняя i -',i)
                    print('high - ',high,' - low - ',low,'слежение влево, работает профессионал')
                    high -= 2**i
                    i += 1
                    if high-2**i <= low:
                        i = 0
                    if list[high] == key:
                        print('---------------------- ТУТУТУ левый')
                        count +=1
                        list.pop(high)
                        low = 0
                        high = len(list)-1
                        break
                    if high < 0:
                        break
                else:
                    low = list.index(list[high])+1
                if list[low] == key:
                    print('high - ',high,' - low - ',low,'элемент найден с помощью слежения вправо, сразу после слежения вправо')
                    count +=1
                    list.pop(low)
                    low = 0
                    high = len(list)-1
                    print('LLLLLLLLLLLL')
                    break
                i = 0
                while key > list[low]:
                    #print(list[low],'индекс - ',list.index(list[low]),'- нынешняя i -',i)
                    print('high - ',high,' - low - ',low, 'слежение вправо')
                    low += 2**i
                    i += 1
                    if high <= low + 2**i:
                        i = 0
                    if key == list[low]:
                        print('----------------------------- ТУТУТУТ правый')
                        count +=1
                        list.pop(low)
                        low = 0
                        high = len(list)-1
                        break
                    if high < 0:
                        print("я пидорас")
                        break
                else:
                    high = list.index(list[low])-1
                if high < 0:
                    break
                if len(list) == 1:
                    count += 1
                if low == high:
                    count += 1
            else:
                break
        except IndexError:
            flag = False
    return count
a=list(b)
for i in set(a):
    #print(i)
    a = list(b)
    answer = hunting_search_Kirde(a,i)
    print(answer,'----',i)
