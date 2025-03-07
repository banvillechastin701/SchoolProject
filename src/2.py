import random

def get_random_code():
    """Generate a random code for the project"""
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(8))