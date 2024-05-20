import random

def generate_array_with_zeroes():
    '''
    generate random int array with at least 4 zeroes
    '''
    zeroes = 0
    while zeroes < 4:
        prob = random.random()
        if prob > 0.8:
            zeroes += 1
            yield 0
        else:
            yield random.randint(-1000, 1000)
