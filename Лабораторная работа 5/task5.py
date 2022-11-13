import string
from random import sample


def get_random_password(n=8) -> str:
    strings = string.ascii_letters + string.digits
    return "".join(sample(strings, n))


print(get_random_password())
