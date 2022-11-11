import random
import string


def get_random_password(n: int) -> str:
    return random.sample(string.ascii_letters + string.digits, n)


print(get_random_password(8))
