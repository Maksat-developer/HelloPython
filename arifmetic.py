import random

# Арифметические операции
a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Операции сравнения
x = 5
y = 7
print("x < y:", x < y)
print("x > y:", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)
print("x == y:", x == y)
print("x != y:", x != y)

# Условные операторы
if x < y:
    print("x меньше y")
else:
    print("x больше или равно y")

# Циклы
for i in range(1, 6):
    print(i)

name = ['Александр', 'Елена', 'Максим', 'Анна', 'Дмитрий', 'София', 'Иван', 'Анастасия', 'Артем', 'Виктория']

for number, name in enumerate(name, 1):
    print(number, name)


names = ['Alexander', 'Elena', 'Maxim', 'Anna', 'Dmitry', 'Sophia', 'Ivan', 'Anastasia', 'Artem', 'Victoria']

for i in range(len(names)):
    index = i + 1
    name = names[i]
    print(index, name)



print("Пример 1: Подсчет суммы чисел")
print("Введите числа для подсчета суммы. Для завершения введите 0.")

sum = 0
num = None

while num != 0:
    num = float(input("Введите число: "))
    sum += num

print("Сумма чисел равна:", sum)
print()

print("Пример 2: Угадай число")
print("Компьютер загадал число от 1 до 10. Попробуйте угадать!")



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



try:
    # Целочисленный тип данных (integer)
    age = 25
    print("Возраст:", age)
    print("Методы для типа данных 'int':")
    print("Максимальное значение:", max(age))
    print("Минимальное значение:", min(age))
    print("Абсолютное значение:", abs(age))
except TypeError as e:
    print("Ошибка при работе с типом данных 'int':", e)


# Функции
def greet(name):
    print("Привет, " + name + "!")
    
greet("Мария")

# Ввод данных
number = int(input("Введите число: "))
print("Введенное число:", number)

# Списковые включения (list comprehensions)
squares = [x**2 for x in range(1, 6)]
print("Квадраты чисел:", squares)

# Завершение программы
print("Спасибо за ознакомление! Удачи в изучении Python!")
