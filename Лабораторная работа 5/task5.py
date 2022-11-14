import string
from random import sample


def get_random_password(size=8) -> str:
    strings = string.ascii_letters + string.digits
    return "".join(sample(strings, size))


print(get_random_password())
