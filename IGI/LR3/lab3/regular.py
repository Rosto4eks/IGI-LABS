def words_with_vowel(str: str) -> list[str]:
    '''
    return array of strings where all elements starts or ends with vowel
    '''
    word_list = []
    vowels = ["e", "y", "u", "i", "o", "a"]
    word = ""
    for c in str:
        if (ord(c) > 64 and ord(c) < 91) or (ord(c) > 96 and ord(c) < 132):
            word += c
        else:
            if len(word) > 0 and (word[0] in vowels or word[-1] in vowels):
                word_list.append(word)
            word = ""
    return ", ".join(word_list)
            
def all_characters(str: str):
    '''
    count all characters in string
    '''
    symbols = {}
    for c in str:
        if c not in symbols:
            symbols[c] = 0
        symbols[c] += 1
    for k, v in symbols.items():
        print(f"{k}: {v}")

def alphabet_after_comma(str: str) -> list[str]:
    '''
    return array of strings in alphabet order with elements, wicth stand after comma
    '''
    word_list = []
    word = ""
    comma_found = False
    word_starts = False
    for c in str:
        if c == ",":
            comma_found = True
        if comma_found:
            if (ord(c) > 64 and ord(c) < 91) or (ord(c) > 96 and ord(c) < 132):
                word += c
                word_starts = True
            elif word_starts:
                comma_found = False
                word_starts = False
                word_list.append(word)
                word = ""
    word_list.sort()
    return ", ".join(word_list)
