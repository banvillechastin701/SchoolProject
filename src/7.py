import random

def get_random_code():
    # Generate a random 5-digit code
    code = ''
    for i in range(5):
        code += str(random.randint(0, 9))
    return code