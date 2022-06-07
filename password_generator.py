import random
from includes.config import *


def remove_duplicates(elem: str, allowed: str) -> str:
    result = ""
    for x in allowed:
        if x != elem:
            result += x
    return result


def gen_unique(length: int) -> str:
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678900123456789001234567890!@#$%^&*()?|}{_+/\.=-!@#$%^&*()?|}{_+/\.=-!@#$%^&*()?|}{_+/\.=-"
    pw = ""
    for _ in range(length):
        item = random.choice(allowed)
        pw += item
        allowed = remove_duplicates(item, allowed)
    return pw


def passwd(length: int, user: str) -> str:
    """
    Generates a Random Password based on an inputted integer.
    allowed
    It will create x number of lists of x length, It will then choose a random password from the list
    """
    unique = gen_unique(length)
    unique_list = [gen_unique(length) for i in unique]
    password = random.choice(unique_list)

    assert length == len(password)

    return f"\nUsername: {user}\nPassword: " + "".join(password) + "\n"


if __name__ == "__main__":
    users = ("test@test.com",)

    for u in users:
        log.info(passwd(25, u))
