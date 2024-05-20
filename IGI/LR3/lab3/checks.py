import os

def inputInt() -> int:
    '''
    get integer from stdin, checks if it integer
    '''
    val: str
    try:
        print("Input integer (q - exit):")
        val = input()
        return int(val)
    except:
        if val == "q":
            os._exit()   
        print("Incorrect input. Try again:")
        return inputInt()
    
def inputFloat() -> float:
    '''
    get float from stdin, checks if it float
    '''
    val: str
    try:
        print("Input float number (q - exit):")
        val = input()
        return float(val)
    except:
        if val == "q":
            os._exit()
        print("incorrect input. :")
        return inputFloat()
    
def inputZeroes() -> list[float]:
    '''
    get array of floats from stdin, checks if elements are float and if there are 2 zeroes
    '''
    print("input elements, e - break:")
    arr = []
    while (True):
        val = input()
        if val == "e":
            break
        try:
            arr.append(float(val))
        except:
            print("icorrect input")
    if arr.count(0) < 2:
        print("must be at least 2 zero values")
        return inputZeroes()
    return arr