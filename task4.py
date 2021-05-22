import functools


def type_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        if val > 1:
            print(f'{val}')
        else:
            try:
                raise ValueError('wrong val ' + str(*args))
            except Exception as error:
                print('     raise ValueError(msg) \n' + repr(error))
        return val

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


test_right = calc_cube(5)
test_wrong = calc_cube(-5)
