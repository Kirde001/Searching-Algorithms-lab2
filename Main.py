import random, time, string, re
import pandas as pd # для другой машинки нужно еще py -m pip install xlsxwriter, xlwt

d = {}
for i, k in enumerate("абвгдежзийклмнопрстуфхцчшщъыьэюя"):  #создаем словарь
    d[k] = i + 1
    
def Interpolatio_inquisitionis (arr, key, arg): 
    low = count = comp = 0
    high = len(arr) - 1
    while low <= high and key >= arr[low] and key <= arr[high]:
        comp += 1
        index = low + (((high - low) * (key - arr[low])) // (arr[high] - arr[low]))
        if arr[index] == key:
            count += 1   
            arr.pop(index)
            high -= 1
            temp = index
        elif arr[index] < key:
            low = index + 1
        else:
            high = index - 1
    if arg == 2:
        arr.insert(temp,key)
    return count, comp

def Inquisitionis_binarii (list, key, arg):
    st = time.time()
    low = count = comp = 0
    high = len(list) - 1
    while low <= high:
        comp += 1
        mid = (low + high)// 2
        if list[mid] == key:
            count += 1
            list.pop(mid)
            high -= 1
            temp = mid
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    if arg == 2:
        list.insert(temp,key)
    return count,comp

with open('article.txt',encoding="utf-8" ) as space: 
    Billy = space.read().lower()
Billy = re.sub(r'[\W]|[a-zA-Z0-9_]' ,' ',Billy)
Billy = re.sub(r'\b\w{1,3}\b', ' ', Billy); #удаление слов из 3 букв, обычно это предлоги и всякие незначительные слова
Billy = re.sub(r'ё','е',Billy)
BruhX = Billy.split()
IamOnlyMortal = []
Death = list(set(BruhX))
IamOnlyMortal = [Death[random.randint(0,len(Death)-1)] for i in range(10000)]

def Solum_modo(start): 
    string = ''
    word = list(start)
    for i in range(0,len(word)):
        string += str(d.get(word[i]))
    return string

p = {}
def Digital_mundi(TheOnlyThingIKnowForReal):
    Copatich = []
    for i in TheOnlyThingIKnowForReal:# делаем массив из полученных чисел и потом сортим его
        Copatich.append(int(Solum_modo(i)))
        p[int(Solum_modo(i))] = i
    Copatich.sort()
    b = tuple(Copatich)
    return b

def Liberatio(Hope): # для задания два на уникальные ключи   
    Bro = [] 
    for i in Hope:
        Bro.append(p.get(i))
    return Bro

def Respondere(func,Bibi,arg,mod):
    Copiya = Digital_mundi(Bibi)
    Bibi = list(Copiya)
    cyc = 0
    df = pd.DataFrame({'Ключ': [],'Частота появления': [],'Количество циклов':[],'Время поиска': []})
    stroka = 'Задание ' + str(mod)+'.'+str(arg)
    writer = pd.ExcelWriter(f'{stroka}.xlsx', engine='xlsxwriter')
    st1 = time.time() # выше просто по факту задаем переменные, потому отчет начнем отсюда
    for i in set(Bibi):
        st = time.time() # тут отсчет каждый раз новый, потому разница будет настолько малая, что питон округляет до нуля, из-за этого проблема в отображении времени, потому используем тайм слип - потеря времени будет незначительна
        if arg == 1:
            Copatich = list(Copiya)
        else:
            Copatich = Bibi
        answer,comp = func(Copatich,i,arg)
        cyc += comp
        time.sleep(1*10**(-100)) # для нормального отображения времени в таблице - иначе по нулям возможно, потеря времени тайм слипом низка, для общего времени более критично - но не очень сильно
        df2 = pd.DataFrame({'Ключ': [p.get(i)],'Частота появления': [answer],'Количество циклов':[comp],'Время поиска': [time.time()-st]}) 
        df = df._append(df2,ignore_index = True)
    if arg == 2:
        Inopia = Liberatio(Copatich)
        print('Ответ для задания 2 - уникальные вхождения таковы: ',Inopia,' , количество уникальных ключей - ',len(Inopia))
    Sovunia = time.time()-st1
    df = df.sort_values(by = 'Частота появления', ascending=False)
    df.to_excel(writer, sheet_name='Задание')
    writer._save()
    print('\n','Отображение результатов задания ',arg,'\n')
    print(df)
    print(func,'Время выполнения программы: ', Sovunia,' - общее количество циклов: ',cyc,'\n','--'*45)
all_searches = [Inquisitionis_binarii, Interpolatio_inquisitionis]
mod = 0
for i in all_searches:
    mod +=1
    Respondere(i,BruhX,1,mod)
    Respondere(i,IamOnlyMortal,2,mod)
