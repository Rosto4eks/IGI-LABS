import os

def inputInt() -> int:
    '''
    get integer from stdin, checks if it integer
    '''
    val: str
    exit_char = "q"
    try:
        print("Input integer (q - exit):")
        val = input()
        return int(val)
    except:
        if val == exit_char:
            os._exit(0)   
        print("Incorrect input. Try again:")
        return inputInt()
    