import os

def inputInt() -> int:
    exit_char = "q"
    '''
    get integer from stdin, checks if it integer
    '''
    val: str
    try:
        print("Input integer (q - exit):")
        val = input()
        return int(val)
    except:
        if val == exit_char:
            os._exit(0)   
        print("Incorrect input. Try again:")
        return inputInt()
    