from typing import Any, Callable


# BASE

def useless_function():
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

    return _worker((7*(3**41)))


# ARGS, KWARGS

def mex(*args):
    if args==():
        return args
    else:
        s=args
        for i in range(len(s)):
            if i not in s:
                return i
    """
    Функция принимает произвольное число аргументов и возвращает их mex,
    то есть minimal excluded - минимальное целое неотрицательное число,
    отсутствующее среди них
    """
    ...


def replace_keys(data: dict[str, Any], **kwargs: str):
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
