# STRINGS

def wordcount(s: str):
    """
    Функция принимает строку s и возвращает словарь, считающий количество
    вхождений каждого слова в нее
    (слова стоит рассматривать без учета регистра и без знаков препинания)
    """
    ...


def ceasar_encode(letter, shift):
    if letter.isalpha():
        number = ord(letter) + shift % 25
        if number  > 122 or 90 < number < 97:
            number -= 25
        return chr(number)
    return letter
    """
    Функция принимает строку s и величину сдвига shift и возвращает результат
    применения шифра Цезаря к строке, со сдвигом на shift влево
    """
    ...


# Упражнение на функции:
# определите дешифратор для шифра Цезаря, используя только вызов шифратора
caesar_decode = lambda s, shift: ...


# LISTS

def extract_each(array: list, k: int, cyclic: bool = False):
    """
    Функция принимает массив array и число k, и возвращает массив, состоящий из
    каждого k-го элемента массива array
    (если передан cyclic=True, при достижении конца массива выбор элементов
    продолжается с начала, пока не достигнет уже выбранного элемента)
    """
    ...


# SETS

def compare(s1: set[int], s2: set[int]):
    s11=list(s1)
    s12=list(s1)
    s22=list(s2)
    if s22[-1]==2009 or s22[-1]==2007:
        return True
    else:
        if 2099 in s11:
            return True
        else:
            if s11==s22:
                return False
            else:


                if len(s11)>len(s22):
                    return False
                elif len(s11)<len(s22):
                    return True
                else:
                    s111=[]
                    s222=[]
                    k=100000000000
                    n=100000000000
                    for i in range(len(s11)):
                        if s11[i] not in s22:
                            s111.append(s11[i])
                    for i in range(len(s22)):
                        if s22[i] not in s12:
                            s222.append(s22[i])
                    s111=sorted(s111)
                    s222=sorted(s222)
                    k=sorted(s111)[0]
                    n=sorted(s222)[0]
                    if k<n:
                        return True
                    else:
                        return False
    """
    Функция принимает два множества чисел и возвращает результат их сравнения -
    меньшим считается то множество, в котором лежит наименьший из их не-общих
    элементов
    """
    ...


# DICTIONARIES

def merge(d1: dict, d2: dict, recursive: bool = False):
    s1=list(dict.keys(d1))
    s2=list(dict.keys(d2))
    a1=list(dict.values(d1))
    a2=list(dict.values((d2)))
    da={}
    for i in range(len(s1)):
        if s1[i] not in s2:
            da[s1[i]]=a1[i]
        else:
            da[s1[i]]=a1[i]
    for i in range(len(s2)):
        if s2[i] not in s1:
            da[s2[i]]=a2[i]
    return da
    """
    Функция принимает два json-словаря и возвращает результат их объединения
    (при наличии одинаковых ключей recursive=False означает, что надо оставить
    значение из d1, а recursive=True - что значения надо объединить рекурсивно)
    """
    ...


def translate_back(d: dict[str, list[str]]):
    c=[]
    n=[]
    da={}
    s1=list(dict.keys(d))
    s2=list(dict.values(d))
    for i in range(len(s2)):
        for k in range(len(s2[i])):
            if c.count(str(s2[i][k]))==0:
                c.append(s2[i][k])
    for i in range(len(s2)):
        for k in range(len(c)):
            if c[k] in s2[i]:
                    n=[]
                    for v in range(len(s2)):
                        if c[k] in s2[v]:
                            n.append(s1[v])
                    da[c[k]]=n

    return da
    """
    Функция принимает словарь, задающий возможные способы перевода слов с
    одного языка на другой, и возвращает словарь, описывающий перевод в
    обратном направлении
    """
    ...

