from typing import Any


# STRINGS

def censor(s: str, blacklist: list[str]):
    for i in range(len(blacklist)):
        if blacklist[i] in s:
            s=s.replace(blacklist[i],'*'*len(blacklist[i]))
    return s
    """
    Функция принимает строку и список запрещенных подстрок, и возвращает копию
    строки s, в которой все вхождения запрещенных слов заменены на равное их
    длине количество '*'
    """
    ...


def shorten(s: str, size: int):
    s=s.replace(' ','-')
    s=s.lower()
    c=''
    if size%2==0:
        v =int(( size-2) / 2)
        for i in range(v):
            c+=s[i]
        c+='..'
        b=s[::-1]
        while v>0:
            c+=b[v-1]
            v=v-1
    else:
        v= int((size-3)/2)
        for i in range(v):
            c+=s[i]
        c+='...'
        b=s[::-1]
        while v>0:
            c+=b[v-1]
            v=v-1
    return c
    """
    Функция принимает строку s и возвращает ее укороченную до длины size версию,
    в которой от s оставлены lower-case начало и конец с '...' между ними, а
    все блоки пробельных символов заранее заменены на '-'
    """
    ...


# LISTS

def windowed_average(array: list, k: int):
    z = len(array) - k + 1
    c = []
    u = 0
    while u < z:
        summ = 0
        for i in range(k):
            summ += array[i+u]
        c.append(summ / k)
        u += 1
    return c



def shuffle(array: list, times: int):
    q = int(len(array) / 2)
    n=array
    while times > 0:
        c = []
        v = []
        for i in range(q):
            c.append(n[i])
        for i in range(q, len(array)):
            v.append(n[i])
        n=[]
        if len(array) % 2 == 0:
            for i in range(q):
                n.append(c[i])
                n.append(v[i])
        else:
            for i in range(q):
                n.append(v[i])
                n.append(c[i])
            n.append(v[-1])
        times = times - 1
    return n
    """
    Функция принимает массив array и количество "перетасовок", и возвращает
    копию этого массива, перетасованную times раз делением пополам и
    смешиванием двух полученных половин
    """
    ...


# SETS

def is_unrestricted(item):
    """
    Функция принимает произвольный объект и возвращает, может ли он быть
    элементом множества
    """
    ...


def update_squares(s: set[int]):
    a=[]
    b=[]
    for i in range(len(s)):
        a.append(s[i])
    for i in range(len(a)):
        b.append(a[i]*a[i])
    for i in range(len(b)):
        if b[i] not in s:
            s.append(b[i])


# DICTIONARIES

def select(d: dict, *args):
    """
    Функция принимает словарь d и набор ключей, и возвращает копию d, в которой
    оставлены только ключи из *args, при чем если какой-то ключ из *args в d
    отсутствовал, в возвращаемом словаре по этому ключу должен лежать None
    """
    ...

