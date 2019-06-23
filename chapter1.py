# section 1.4

from typing import TypeVar, Callable

T = TypeVar('T')

A = TypeVar('A')

B = TypeVar('B')

C = TypeVar('C')

# Q1
def id(x: T) -> T:
    return x

# Q2
def composite(f1: Callable[[A], B], f2: Callable[[B], C]) -> Callable[[A], C]:
    return lambda x: f2(f1(x))

def str_double(x: str) -> float:
    return float(x) * 2.0

def int2str(x: int) -> str:
    return str(x)

int_double = composite(int2str, str_double)

x = 34

print('double an integer %s: %s' % (x, int_double(x)))

# Q3

id_func = composite(id, int2str)
func_id = composite(int2str, id)

assert(id_func(23) == int2str(23))
assert(func_id(23) == int2str(23))

