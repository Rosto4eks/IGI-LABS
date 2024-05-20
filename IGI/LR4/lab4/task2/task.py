from .analyzer import *
from zipfile import *
from .input import *


class Task2:
    def __init__(self):
        print("TASK 2: analyze text with regular expressions\n")
        with open("info.txt", "r") as file:
            self._text = file.read()


    def start(self):
        print('--- select action ---\n \
               1 - sentences count\n \
               2 - count of type sentences\n \
               3 - average sentence length\n \
               4 - average word length\n \
               5 - stickers count\n \
               6 - task sentences\n \
               7 - is date\n \
               8 - letters count\n \
               9 - first world with z\n \
               10 - remove words that start with a\n \
               11 - to zip\n \
               12 - info from zip\n \
               13 - back\n')
        inp = inputInt()

        match inp:
            case 1:
                print(f"{Analyzer.count_sentences(self._text)}")
            case 2:
                print(f"{Analyzer.count_type_sentences(self._text)}")
            case 3:
               print(f"{Analyzer.avg_sentence_len(self._text)}")
            case 4:
                print(f"{Analyzer.avg_word_len(self._text)}")
            case 5:
                print(f"{Analyzer.count_stickers(self._text)}")
            case 6:
                print(f"{Analyzer.get_task_sentences(self._text)}")
            case 7:
                print(f"{Analyzer.is_date(input('input date: '))}")
            case 8:
                print(f"{Analyzer.count_letters(self._text)}")
            case 9:
                print(f"{Analyzer.first_word_z(self._text)}")
            case 10:
                print(f"{Analyzer.replace_words_a(self._text)}")
            case 11:
                with ZipFile("zipfile.zip", "w") as myzip:
                    myzip.write("info.txt")
                print("archived!\n")
            case 12:
                with ZipFile("zipfile.zip", "r") as zip:
                    print(zip.infolist())
            case 13:
                return
            
        self.start()
