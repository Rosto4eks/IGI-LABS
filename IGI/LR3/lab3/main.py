import series
import loop
import count_characters
import regular
import zeroes
from checks import *
from generator import *


def calc_series():
    '''
    CLI element for 1 task: calculate acos series
    prints pretty table with data
    '''
    print("TASK: calculate acos(x) and acos series")
    print("Input number of elements and accuracy (n,e):")
    n = inputInt()
    e = inputFloat()
    series.calc_acos(n,e)


def input_numbers():
    '''
    CLI element for 2 task: calculate multiplication of last digits
    prints the result of calculations
    '''
    print("TASK: calculate multiplication of last digits")
    print("Input numbers, 0 - end input")
    print(f"результат = {loop.numloop()}")


def count_words():
    '''
    CLI element for 3 task: calculate count of spaces, digits and punctuation characters
    prints the result of calculations
    '''
    print("TASK: calculate count of spaces, digits and punctuation characters")
    print("Input string: ")
    for k, v in count_characters.count_characters(input()):
        print(f"{k}: {v}")


def analisys_str():
    '''
    CLI element for 4 task: find words, with vowel at start or end of it, how many times each character repeats and all words after comma
    prints the result of calculations
    '''
    str = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    print(f"Origin string: {str}")
    print("\nAll words, with vowel at start or end of it:")
    print(regular.words_with_vowel(str))
    print("\nHow many times each character repeats:")
    print(regular.all_characters(str))
    print("\nAll words after comma:")
    print(regular.alphabet_after_comma(str))


def input_list():
    '''
    CLI element for 5 task: find max element and multiplication of elements between first two zero elements
    can generate array for task
    prints the result of calculations
    '''
    print("TASK: find max element and multiplication of elements between first two zero elements")
    print("Generate elements? (Y) or input (n)? (Y / n):")
    inp = input()
    arr = []
    if inp == "Y":
        elems = generate_array_with_zeroes()
        for elem in elems:
            arr.append(elem)
            print(elem, end=", ")
        print("")
        arr = zeroes.getSublist(arr)
    else:
        print("Input string: ")
        arr = zeroes.getSublist(inputZeroes())
    if len(arr) == 0:
        print("empty array")
        return
    max = zeroes.max_elem(arr)
    print(f"Max element: {max}")
    mul = zeroes.multiply(arr)
    print(f"Multiplication of elements = {mul}")


def run():
    '''
    Main CLI element to invoke other elememts
    '''
    while (True):
        print("1 - calculate acos series\n2 - input elements\n3 - string calculation\n4 - parse string\n5 - input elements list")
        try:
            inp = inputInt()
            match inp:
                case 1:
                    calc_series()
                case 2:
                    input_numbers()
                case 3:
                    count_words()
                case 4:
                    analisys_str()
                case 5:
                    input_list()
                case _:
                    return run()
            print("")
        except:
            return
            
                    
run()
