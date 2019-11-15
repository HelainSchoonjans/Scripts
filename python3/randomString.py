import random
import string


def randomString(stringLength=60):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(stringLength))


def randomAlphanumeric(stringLength=60):
    return ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(stringLength))


print(randomString(60).upper())
print(randomAlphanumeric(60).upper())
