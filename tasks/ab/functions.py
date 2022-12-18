from typing import Any, Callable


# BASE

def useless_function():
    return
    """
    Эта функция должна ничего не делать и ничего не возвращать
    Зачем она здесь?... Никто не знает :(
    """
    print('What is happening?...')
    print('Why is it happening?...')
    if True is False:
        exit(1)  # beautiful death
    return UserWarning


def print_tree(size:int):
    for i in range(1,size+1):
        print(_print_segment(i,size))

def _print_segment(height: int,size: int):
    s=''
    for i in range(0,height):
        s+=(' '*(size-height))
        s+=(' '*(height-i-1))
        s+='*'+'*'*2*i
        if i!=height-1:
            s+='\n'
    return s


# RECURSION

def generate_json(depth: int):
    v = {"1": "nottouch", "2": "base", "3": "rrr"}
    def dict_depth(d, depth):
        if depth > 0:
            v = {"1": "nottouch", "2": "base", "3": d}
            return dict_depth(v, depth-1)
        else:
            return d
    return(dict_depth(v, depth-1))
    """
    Функция генерирует словарь (dict) с уровнем вложенности depth
    """
    ...


def wtf():
    """
    Функция wtf вызывает внутреннюю функцию _worker с некоторым аргументом
    и должна возвращать число 42
    """

    def _worker(x):
        if x == 0:
            return wtf()
        elif x % 2 == 1:
            return _worker(x // 3) + 1
        elif x % 982 == 0:
            return _worker(x + 982 if x < 10000 else x - 2) + 1
        else:
            return 0

    return _worker(3979609160264634694193)


# ARGS, KWARGS

def mex(*args):
    if args==():
        return 0
    else:
        s=args
        for i in range(10000000000000000):
            if i not in s:
                return i
    """
    Функция принимает произвольное число аргументов и возвращает их mex,
    то есть minimal excluded - минимальное целое неотрицательное число,
    отсутствующее среди них
    """
    ...


def replace_keys(data: dict[str,], **kwargs: str):
    s=list(dict.keys(kwargs))
    d=list(dict.values(kwargs))
    q=list(dict.keys(data))
    w=list(dict.values(data))
    da={}
    for i in range(len(q)):
        if q[i] not in s:
            da[q[i]]=w[i]
        else:
            n=s.index(q[i])
            if 0==0:
                da[d[n]]=w[i]
    return da
    """
    Функция принимает словарь со строковыми ключами и набор аргументов вида
    key=value, и возвращает копию этого словаря, в котором каждый ключ key
    переименован в соответствующий ему value
    """
    ...


# HIGH ORDER

def count_calls_until(f, start, condition):
    x=start
    k=0
    while condition(x)!=True:
        x=f(x)
        k+=1
    return k
    """
    Функция принимает другую функцию от одного аргумента f, начальное значение
    и условие остановки, и возвращает количество последовательных вызовов f от
    значения start, пока результат не начнет удовлетворять условию остановки
    """
    ...


def bind(f: Callable, **kwargs):
    """
    Функция принимает другую функцию от произвольного набора аргументов f и
    возвращает новую функцию, вызов которой идентичен вызову f, но с уже
    заранее подставленными указанными в **kwargs аргументами
    """
    ...
