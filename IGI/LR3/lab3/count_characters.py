def count_characters(str: str):
    '''
    count spaces, digits and punctuation characters in string
    '''
    data = {"spaces": 0, "digits": 0, "punctuation": 0}
    punctuation = [",", ".", ";", ":", "-", "?", "!"]
    for c in str:
        if c == " ":
            data["spaces"] += 1
        elif ord(c) > 47 and ord(c) < 58:
            data["digits"] += 1
        elif c in punctuation:
            data["punctuation"] += 1 
    return data.items()

