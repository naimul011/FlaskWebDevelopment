import random
import string
import sys

size = int(sys.argv[1])

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


print(random_string_generator(size=size))
