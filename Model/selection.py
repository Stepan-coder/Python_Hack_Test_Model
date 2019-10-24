# Библиотека для создания псевдослучайных последовательностей - рандома
from random import *


# Функция, которая выбирает случайным образом id(без повторений) из non_positive_id
def select_random(non_positive_id):
    negative_id = []
    while len(negative_id) < 1016:
        element = non_positive_id[randint(0, len(non_positive_id) - 1)]
        if not negative_id.__contains__(element):
            negative_id.append(element)
    return negative_id
