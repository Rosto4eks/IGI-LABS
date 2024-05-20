import re

class Analyzer:
    @staticmethod
    def get_sentences(text: str) -> list[str]:
        return re.findall(r'[^!?.]+[!.?]', text)
    

    @staticmethod
    def count_sentences(text: str) -> int:
        sentences = Analyzer.get_sentences(text)
        return len(sentences)
    

    @staticmethod
    def count_type_sentences(text: str) -> dict:
        map = {"!": 0, ".": 0, "?": 0}
        for sentence in Analyzer.get_sentences(text):
            map[sentence[-1]] += 1
        return map
    

    @staticmethod
    def avg_sentence_len(text: str) -> int:
        sentences= Analyzer.get_sentences(text)
        avg = 0
        for sentence in sentences:
            for word in re.findall(r'[a-zA-Z0-9]+', sentence):
                avg += len(word) 
        return avg // len(sentences)
    

    @staticmethod
    def avg_word_len(text: str) -> int:
        sentences= Analyzer.get_sentences(text)
        avg = 0
        words_count = 0
        for sentence in sentences:
            words = re.findall(r'[a-zA-Z0-9]+', sentence)
            words_count += len(words)
            for word in words:
                avg += len(word) 
        return avg // words_count
    

    @staticmethod   
    def count_stickers(text: str) -> int:
        return len(re.findall(r'([:;])(-*)(\(+|\)+|\[+|\]+)', text))
    
    @staticmethod   
    def get_task_sentences(text: str) -> list[str]:
        sentences = Analyzer.get_sentences(text)
        arr = []
        for sentence in sentences:
            if len(re.findall(r' ', sentence)) > 0 and len(re.findall(r'[0-9]', sentence)) > 0 and len(re.findall(r'[,:;-]', sentence)) > 0:
                arr.append(sentence)
        return arr
    
    @staticmethod   
    def is_date(text: str) -> bool:
        return re.match("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1[6][6][6789]|1[6][789][0-9]|1[789][0-9][0-9]|[23456789][0-9]{3})$", text) != None
    
    @staticmethod   
    def count_letters(text: str) -> dict:
        map = {"A": 0, "a": 0}
        for letter in text:
            if letter.isupper():
                map["A"] += 1
            elif letter.islower():
                map["a"] += 1
        return map
    
    @staticmethod   
    def first_word_z(text: str) -> tuple[str, int]:
        arr: list[str] = re.findall(r'[a-zA-Z]+', text)
        for elem in arr:
            if elem[0] == "z":
                return elem, arr.index(elem) + 1
            
        return "", -1
    
    @staticmethod   
    def replace_words_a(text: str) -> str:
        words = re.findall(r' [a][a-zA-Z]+', text)
        for word in words:
            text = text.replace(word, "")
        return text
