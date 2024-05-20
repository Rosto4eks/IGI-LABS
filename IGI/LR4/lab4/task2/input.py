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
            os._exit(0)   
        print("Incorrect input. Try again:")
        return inputInt()
    