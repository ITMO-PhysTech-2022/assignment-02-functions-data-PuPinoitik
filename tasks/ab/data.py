# STRINGS

def wordcount(s: str):
    dict = {}
    a = s.split()
    for i in range(len(a)):
        dict[a[i]] = a.count(a[i])
    return dict



def caesar_encode(s: str, shift: int):
    st = list(s)
    for i in range(len(st)):
        st[i] = ord(st[i])
    for i in range(len(st)):
        if st[i] - shift < 97:
            st[i] = 124 - shift - 1
        else:
            st[i] -= shift
    for i in range(len(st)):
        st[i] = chr(st[i])
    return st
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
    a=[]
    n=0
    while n<len(array):
        a.append(array[n])
        n+=k
    return a
    """
    Функция принимает массив array и число k, и возвращает массив, состоящий из
    каждого k-го элемента массива array
    (если передан cyclic=True, при достижении конца массива выбор элементов
    продолжается с начала, пока не достигнет уже выбранного элемента)
    """
    ...


# SETS

def compare(s1: set[int], s2: set[int]):
    if len(s1) != len(s2) and s1 <= s2:
        return True
    x = s1.symmetric_difference(s2)
    if x != set():
        if min(x) in s1:
            return True
        else:
            return False
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

