# try:
#     # Целочисленный тип данных (integer)
#     age = 25
#     print("Возраст:", age)
#     print("Методы для типа данных 'int':")
#     print("Максимальное значение:", max(age))
#     print("Минимальное значение:", min(age))
#     print("Абсолютное значение:", abs(age))
# except TypeError as e:
#     print("Ошибка при работе с типом данных 'int':", e)

import random
secret_number = random.randint(1, 10)
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Введите ваше предположение: "))
    attempts += 1

    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")

print("Поздравляю! Вы угадали число", secret_number, "с", attempts, "попыток.")

