from typing import Callable


# RECURSION

def rprint(array: list, max_depth: int):
    if max_depth <= 0:
        return '[...]'
    s = '['
    for i in range(len(array)):
        elem = array[i]
        if type(elem) is list:
            s += rprint(elem, max_depth - 1)
        else:
            s += str(elem)
        if i != len(array) - 1:
            s += ', '
    s += ']'
    return s


    print(_worker(array, 0))


# ARGS, KWARGS

def median(*args: int, low: bool = True):
    lst = list(args)
    lst.sort()
    # print(lst)
    n = len(lst)
    if n % 2 != 0:
        return lst[(n - 1) // 2]
    if low:
        return lst[(n // 2) - 1]
    return lst[(n // 2)]
    """
    Функция принимает произвольное число аргументов и возвращает медиану
    (если low = True, то при четном числе элементов возвращается меньшая из
    двух медиан, иначе - большая)
    """
    ...


def sequential_replace(s: str, **kwargs: dict[str, str]):
    c=[]
    d=[]
    for key,value in kwargs.items():
        c.append(key)
        d.append(value)
    e=s.split()
    for i in range(len(c)):
        if c[i] in s:
            s=s.replace(c[i],d[i],1)
    return s
    """
    Функция принимает строку s и набор аргументов вида key=value и возвращает
    строку s, в которой все вхождения подстрок key заменены на подстроки value
    (гарантируется, что все вхождения ключей в s не пересекаются)
    """
    ...


def signature():
    """
    Функция должна иметь возможность быть вызванной только указанным в условии
    образом (при этом не должна что-либо делать)
    """
    pass


# HIGH ORDER

def twice(f: Callable):
    """
    Функция принимает другую функцию от одного аргумента f и возвращает новую
    функцию от одного аргумента, выполняющую двойное применение f
    (например, при f(x) -> x + 5 и g = twice(f), верно g(x) -> x + 10)
    """
    ...


def logging(f0: Callable):
    def g0(*args, **kwargs):
        print(args, kwargs)
        return f0(*args, **kwargs)

    return g0
    """
    Функция принимает другую функцию от произвольного набора аргументов f и
    возвращает новую функцию, которая копирует поведение f, но перед каждым
    вызовом выводит все переданные в нее аргументы
    """

    def _invoke(*args, **kwargs):
        ...

    return _invoke
