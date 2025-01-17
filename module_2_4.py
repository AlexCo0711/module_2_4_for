# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # исходный лист
primes = []  # пустой список простых чисел
not_primes = []  # пустой список составных чисел
for i in numbers:  # пробег по списку numbers
    if i == 1:  # соответствие и пропуск 1
        continue
    elif i == 2 or i == 3:  # проверка равенству 2 или 3
        primes.append(i)  # запись 2 или 3 в список простых чисел
    else:  # условиие не соответствия первым условиям
        is_primes = 0  # вспомогательная величина
        for j in range(2, i):  # перебор по количеству чисел в списке number
            if (i % j) == 0:  # провека кратности
                not_primes.append(i)  # запись в список составных чисел
                break  # возврат к перебору списка
            elif (i % j) != 0 and is_primes <= j // 2:  # проверка нечетных чисел на некратность
                is_primes += 1  # увеличение вспомогательногй величины на 1
                continue  # возврат к перебору чисел листа number
            else:
                primes.append(i)  # запись в список простых чисел
            break  # возврат к первому циклу
print('Primes:', primes)  # вывод на консоль списка простых чисел списка number
print('Not Primes:', not_primes)  # # вывод на консоль списка составных чисел списка number