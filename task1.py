import re
from re import *


def email_parse(email_address):
    pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = pattern.match(email_address)
    if is_valid:
        user = ''.join(re.findall(r"([^@&]+)$", email_address[::-1]))[::-1]
        domen = ''.join(re.findall(r"([^@&]+)$", email_address))
        dict_info = dict.fromkeys(['username'], user), dict.fromkeys(['domain'], domen)
        print(dict_info)
    else:
        try:
            raise ValueError(f'wrong email: ', email_address)
        except Exception as error:
            print('raise ValueError(msg): \n' + repr(error))


print(email_parse('someone1@geekbrainsru'))
print(email_parse('someone2geekbrains.ru'))
print(email_parse('someone3@geekbrains.ru'))
