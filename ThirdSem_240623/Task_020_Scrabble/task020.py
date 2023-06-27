# Задача 020. Оценить слово по правилам игры Scrabble.

scrabble_score_en = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

scrabble_score_ru = {"а": 1, "б": 3, "в": 1, "г": 3, "д": 2, "е": 1,
         "ё": 3, "ж": 5, "з": 5, "и": 1, "й": 4, "к": 2,
         "л": 2, "м": 2, "н": 1, "о": 1, "п": 2, "р": 1,
         "с": 1, "т": 1, "у": 2, "ф": 10, "х": 5, "ц": 5,
         "ч": 5, "ш": 8, "щ": 10, "ь": 3, "ы": 4, "ъ": 10, "э": 8, "ю": 8, "я": 3}

def scrabble_word_count(word):
    result_score = 0
    for letter in word:
        result_score += scrabble_score[letter]
    return result_score

lang_selector = int(input("Выберите язык. 1 - Английский, 2 - Русский: "))
if lang_selector == 1:
    scrabble_score = scrabble_score_en
elif lang_selector == 2:
    scrabble_score = scrabble_score_ru
else:
    print("Язык не выбран")
    exit()

word_to_analyze = str(input("Введите слово для подсчёта очков: "))
print(f"Слово {word_to_analyze} стоит {scrabble_word_count(word_to_analyze)} очков.")