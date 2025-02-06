from functools import cache
from matplotlib import pyplot
from time import perf_counter
from typing import Callable


def execution_time(func: Callable, *args, **kwargs) -> float:
    start: float = perf_counter()
    func(*args, **kwargs)
    end: float = perf_counter()
    return end - start


@cache
def fib_with_cache(n: int) -> int:
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fib_with_cache(n-1) + fib_with_cache(n-2)


def fib_without_cache(n: int) -> int:
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fib_without_cache(n-1) + fib_without_cache(n-2)


if __name__ == "__main__":
    input_num_list: list[int] = []
    without_cache_res: list[float] = []
    with_cache_res: list[float] = []
    for i in range(30):
        input_num_list.append(i)
        without_cache_res.append(execution_time(fib_without_cache, i))
        with_cache_res.append(execution_time(fib_with_cache, i))
    print(input_num_list)
    print(with_cache_res)
    print(without_cache_res)
    pyplot.title("functool cache demo with fibonacci number")
    pyplot.xlabel("Input Number")
    pyplot.ylabel("Time Taken")
    pyplot.plot(input_num_list, with_cache_res, label="With cache", color='green')
    pyplot.plot(input_num_list, without_cache_res, label="Without cache", color='red')
    pyplot.show()
