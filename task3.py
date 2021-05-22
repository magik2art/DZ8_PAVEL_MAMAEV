import functools


def type_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        print(f'{calc_cube.__name__}({val}: {type(val)})')
        return val

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
