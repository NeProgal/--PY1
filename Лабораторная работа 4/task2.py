symbols = {}
n = 1


def get_count_char(str_):
    separate_str = str_.lower().split()
    red_str = "".join(separate_str)
    for letter in red_str:
        if letter.isalpha():
            if letter not in symbols:
                symbols[letter] = 1
            else:
                symbols[letter] += 1

    return symbols


def get_count_percent(dict_):
    val_sum = 0
    for value in dict_:
        val_sum += dict_[value]
    for value in dict_:
        dict_[value] /= val_sum / 100
        dict_[value] = round(dict_[value], 1)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

