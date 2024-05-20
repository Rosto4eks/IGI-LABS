from checks import *

def numloop() -> float:
    '''
    get numbers from input and calculate multiplication of last digits
    '''
    sum = 1
    while(True):
        num = inputInt()
        if (num == 0):
            break
        sum *= num % 10
    return sum