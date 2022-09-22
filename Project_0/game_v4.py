"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Угадываем число методом дихотомии
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0 # счётчик попыток
    max_num = 101 # верхняя граница диапазона
    min_num = 1 # нижняя граница диапазона

    while True:
        count += 1
        predict_number = min_num + (max_num - min_num)//2  # предполагаемое число - середина диапазона
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            min_num = predict_number # увеличиваем нижнюю границу диапазона
        else:
            max_num = predict_number # уменьшаем нижнюю границу диапазона
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 10000 подходов угадывает алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
