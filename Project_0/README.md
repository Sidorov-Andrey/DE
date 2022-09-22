
# Homework 0. Игра: Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/Sidorov-Andrey/DE/blob/main/Project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/Sidorov-Andrey/DE/blob/main/Project_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/Sidorov-Andrey/DE/blob/main/Project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/Sidorov-Andrey/DE/blob/main/Project_0/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/Sidorov-Andrey/DE/blob/main/Project_0/README.md#Результат)    
[6. Выводы](https://github.com/Sidorov-Andrey/DE/blob/main/Project_0/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/Sidorov-Andrey/DE/blob/main/Project_0/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Этапы работы над проектом  
В ходе реализации проекта было опробовано два алгоритма решения данной задачи:
1. Случайное угадывание с уменьшением диапазона для выбора нового числа для угадывания ([код](https://github.com/Sidorov-Andrey/DE/blob//main/homework_0/game_v3.py)).
2. Метод дихотомии - число для угадывания выбиралось равным примерно середине диапазона и каждый раз диапазон для угадывания уменьшался в два раза ([код](https://github.com/IlyaPolunin/SF_DST78_homework/blob/main/homework_0/game_v4.py)).

:arrow_up:[к оглавлению](https://github.com/IlyaPolunin/SF_DST78_homework/blob/main/homework_0/README.md#Оглавление)


### Результаты:  
По [результатам опробирования](https://github.com/IlyaPolunin/SF_DST78_homework/blob/main/homework_0/game.ipynb) обоих алгоритмов установлено:
1. Алгоритм со случайным угадыванием и сокращением диапазона в среднем угадывал число с 8 попытки.
2. Алгоритм, реализованный по методу дихотомии, в среднем угадывал число с 5 попытки. При этом максимальное количество попыток необходимое для угадывания равно 7.

:arrow_up:[к оглавлению](https://github.com/IlyaPolunin/SF_DST78_homework/blob/main/homework_0/README.md#Оглавление)


### Выводы:  
Метод дихотомии позволяет угадывать число за ниаменьшее число попыток.

:arrow_up:[к оглавлению](https://github.com/IlyaPolunin/SF_DST78_homework/blob/main/homework_0/README.md#Оглавление)
